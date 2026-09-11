import mistune, re
from mistune.plugins.math import math, math_in_list, math_in_quote

from rich.console import Console

# Matches [[target]], [[target|alias]], ![[target]], ![[target|alias]]
WIKILINK_PATTERN = r'(?P<bang>!)?\[\[(?P<wikiinner>[^\[\]]+)\]\]'

# Matches ^block-id
BLOCK_ID_PATTERN = r'(?:^|(?<=\s))\^(?P<blockid>[0-9a-zA-Z]+)[ \t]*$'

# Matches **הוכחה:** with the end `\end{proof}`
PROOF_PATTERN = r'^\*\*הוכחה:\*\*[ \t]*(?P<proof_body>[\s\S]*?)\n`?\\end\{proof\}`?[ \t]*$'

# Quote:
BLOCK_QUOTE_PATTERN = r'^ {0,3}>(?P<quote_1>.*?)$'
CALLOUT_RE = re.compile(
    r'^[ \t]*\[!(?P<callout_type>[\w-]+)(?:\|(?P<callout_modifier>[^\]]*))?\][ \t]*(?P<callout_title>[^\n]*)$'
)
BLOCK_ID_RE = re.compile(r'\^([0-9a-zA-Z]+)[ \t]*(?:\n|$)')
BLANK_RUN_RE = re.compile(r'(?:[ \t]*\n)+')

def parse_wikilink(inline, m, state):
    bang = m.group('bang')
    inner = m.group('wikiinner')

    if '|' in inner:
        target, alias = inner.split('|', 1)
    else:
        target, alias = inner, None

    # split target into path / heading / block-ref
    link, heading, block_ref = target, None, None
    if '#' in link:
        link, rest = link.split('#', 1)
        if '^' in rest:
            heading, block_ref = rest.split('^', 1)
        else:
            heading = rest
    elif '^' in link:
        link, block_ref = link.split('^', 1)

    token_type = 'wiki_embed' if bang else 'wiki_link'
    state.append_token({
        'type': token_type,
        'raw': alias or target,
        'attrs': {
            'link': link,
            'heading': heading,
            'block_ref': block_ref,
            'alias': alias,
        },
    })
    return m.end()


def wikilink_plugin(md):
    # register before the built-in 'link' rule so [[ ]] wins priority
    md.inline.register('wikilink', WIKILINK_PATTERN, parse_wikilink, before='link')

def parse_block_id(inline, m, state):
    state.append_token({'type': 'block_id', 'raw': m.group('blockid')})
    return m.end()

def block_id_plugin(md):
    md.inline.register('block_id', BLOCK_ID_PATTERN, parse_block_id, before='linebreak')
    
def parse_proof(block, m, state):
    body = m.group('proof_body')
    # recursively parse the captured body as its own nested block content
    child_state = state.child_state(body)
    block.parse(child_state, block.rules)
    state.append_token({'type': 'proof', 'children': child_state.tokens})
    return m.end() + 1  # also swallow the trailing newline (same trick the math plugin uses)

def proof_plugin(md):
    md.block.register('proof', PROOF_PATTERN, parse_proof, before='paragraph')

def proof_in_list(md):
    md.block.insert_rule(md.block.list_rules, 'proof', before='list')

def proof_in_quote(md):
    md.block.insert_rule(md.block.block_quote_rules, 'proof', before='list')

def parse_block_quote(block, m, state):
    text, end_pos = block.extract_block_quote(m, state)
    first_line, _, rest = text.partition('\n')
    callout_match = CALLOUT_RE.match(first_line)

    attrs = {}
    if callout_match:
        token_type = 'callout'
        attrs['callout_type'] = callout_match.group('callout_type')
        modifier = callout_match.group('callout_modifier')
        attrs['numbered'] = modifier != '*'
        attrs['title'] = callout_match.group('callout_title').strip()
        body = rest
    else:
        token_type = 'block_quote'
        body = text

    child = state.child_state(body)
    if state.depth() >= block.max_nested_level - 1:
        rules = list(block.block_quote_rules)
        rules.remove('block_quote')
    else:
        rules = block.block_quote_rules
    block.parse(child, rules)

    # Look ahead for a trailing "^blockid" line (Obsidian block reference).
    # extract_block_quote sometimes auto-consumes the following blank line
    # itself (whenever end_pos is set) -- in that case the block-id, if
    # any, sits immediately at end_pos. Otherwise we still need to skip
    # the blank-line run ourselves before checking.
    if end_pos:
        lookahead_pos = end_pos
    else:
        m_blank = BLANK_RUN_RE.match(state.src, state.cursor)
        lookahead_pos = m_blank.end() if m_blank else None

    if lookahead_pos is not None:
        m_id = BLOCK_ID_RE.match(state.src, lookahead_pos)
        if m_id:
            attrs['block_id'] = m_id.group(1)
            if end_pos:
                if state.tokens and state.tokens[-1]['type'] == 'blank_line':
                    state.tokens.pop()
                end_pos = m_id.end()
            else:
                state.cursor = m_id.end()

    token = {'type': token_type, 'children': child.tokens}
    if attrs:
        token['attrs'] = attrs

    if end_pos:
        state.prepend_token(token)
        return end_pos
    state.append_token(token)
    return state.cursor

def callout_plugin(md):
    md.block.register('block_quote', BLOCK_QUOTE_PATTERN, parse_block_quote)

markdown_parser = mistune.create_markdown(
    renderer=None,
    plugins=[
        'strikethrough', 'table', 'task_lists', 'footnotes',
        'def_list', 'url',
        math, math_in_list, math_in_quote,
        proof_plugin, proof_in_list, proof_in_quote,
        wikilink_plugin, block_id_plugin, callout_plugin
    ],
    hard_wrap=True,
)