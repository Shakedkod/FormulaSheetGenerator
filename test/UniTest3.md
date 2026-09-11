---
cssclasses:
  - center-h1
  - center-images
---

> [!definition] פונקציה קדומה
> $F(x)$ נקראת **פונקציה קדומה** של $f(x)$ בקטע $I$ אם $F'(x)=f(x)$.

^85a11d

כלומר, פונקציה קדומה היא הפעולה ההפוכה לנגזרת שלפעמים קוראים לה אנטי-נגזרת.
נגזרת של פונקציה היא יחידה. היא הגבול כפי שראינו ב[[4 - פונקציות#^3a733f|אינפי 1]]. אך הפעולה ההפוכה היא לא יחידה. נניח ויש לנו גרף עם שיפוע מסויים, הזזה של אותו הגרף למעלה תהיה בדיוק עם אותו השיפוע ולכן יהיו להן בדיוק אותה נגזרת.

> [!theorem|*] 
> תהי $F$ פונקציה קדומה של $f$ בקטע $I$.
> אזי, אוסף כל הפונקציות הקדומות של $f$ בקטע $I$ הוא ${\Large\{} F(x)+c|c \in \mathbb{R} \Large\}$

המשפט אומר שני דברים:
1. כל פונקציה כזו היא פונקציה קדומה של $f$.
2. אלו כל הפונקציות הקדומות

כעת, נדרש להוכיח את שניהם.

**הוכחה:**
לכל $c \in \mathbb{R}$ מתקיים $(F(x)+c)'=f(x)$. (לפי כללי גזירה)
בנוסף, תהי $G(x)$ פונקציה קדומה אחרת של $f$.
נסמן: $H=G-F$. אזי,
$$
H'=G'-F'=f-f=0
$$
לכן, לפי מסקנה מלגרנז', $H=c$ עבור איזשהו $c \in \mathbb{R}$. לכן, $G-F=c$. כלומר, $G=F+c$
`\end{proof}`

כלומר, אם לפונקציה יש פונקציה קדומה(ולא לכל הפונקציות יש) אז יש לה $\infty$ פונקציות קדומות.

> [!definition|*] סימון
> אוסף הפונקציות הקדומות של $f$ מסומנן על ידי
> $$
> \int f(x)dx
> $$

צריך לזכור שכאשר רואים את הסימון הזה, לא מדובר בפונקציה אחת אלא במשפחה של פונקציות.

> [!example|*] 
> $$
> \int \cos xdx=\sin x+c \qquad \int \sin xdx=-\cos x+c
> $$
> $$
> \int e^xdx=e^x+c \qquad \int xdx=\frac{x^2}{2}+c \qquad n\neq-1, \int x^ndx=\frac{x^{n+1}}{n+1}+c
> $$
> $$
> \int \frac{1}{1+x^2}dx=\arctan x+c \qquad -1<x<1, \int \frac{dx}{\sqrt{ 1-x^2 }}=\arcsin x+c \qquad x\neq0,\int \frac{1}{x}dx=\ln |x|+c
> $$
> **בדיקה על ידי גזירה:** (תמיד כדאי לעשות)
> $$
> \ln |x|=\begin{cases}
> \ln x  & x> 0 \\
> \ln(-x) & x<0
> \end{cases} \implies (\ln |x|)'=\begin{cases}
> \frac{1}{x} & x> 0 \\
>  \frac{1}{-x}\cdot (-1) & x<0
> \end{cases}=\frac{1}{x}
> $$
> > [!remark|*] 
> > האינטגרלים הנ"ל נקראים **אינטגרלים מידיים** ונראה אותם הרבה בהמשך הקורס וגם נוכיח את חלקם.

> [!theorem|*] ליניאריות
> יהיו $f,g:\mathbb{R}\to \mathbb{R}$ בעלות פונקציות קדומות. אזי:
> $$
> \begin{align}
> 1.\; & \int (f(x)+g(x))dx=\int f(x)dx+\int g(x)dx \\
> 2.\; & \forall \alpha \in \mathbb{R}:\; \int \alpha f(x)dx=\alpha\int f(x)dx
> \end{align}
> $$

**הוכחה:**
נתון כי ל-$f,g$ פונקציות קדומות. נסמנם $F,G$ בהתאמה.
נסמן $H(x)=F(x)+G(x)$ ואז:
$$
H'(x) \underset{\begin{matrix}
\downarrow \\
\R{\text{כללי גזירה}}
\end{matrix}}{=}F'(x)+G'(x)=f(x)+g(x)
$$
$$
\int f(x)dx+\int g(x)dx \underset{\begin{matrix}
\downarrow \\
\R{\text{הגדרת אינטגרל}}
\end{matrix}}{=} F(x)+G(x)=H(x) \underset{\begin{matrix}
\downarrow \\
\R{\text{הגדרת אינטגרל}}
\end{matrix}}{=}\int H'(x)dx=\int (f(x)+g(x))dx
$$

יהי $\alpha \in \mathbb{R}$. נגדיר $K(x)=\displaystyle \alpha F(x)$. אזי:
$$
K'(x)=(\alpha F(x))' \underset{\begin{matrix}
\downarrow \\
\R{\text{כללי גזירה}}
\end{matrix}}{=}\alpha F'(x)=\alpha f(x)
$$
$$
\alpha \int f(x)dx \underset{\begin{matrix}
\downarrow \\
\R{\text{הגדרת אינטגרל}}
\end{matrix}}{=}\alpha F(x)=K(x) \underset{\begin{matrix}
\downarrow \\
\R{\text{הגדרת אינטגרל}}
\end{matrix}}{=} \int K'(x)dx=\int\alpha f(x)dx
$$
`\end{proof}`

> [!example|*] אינטגרל כמעט מיידי
> $$
> \int \frac{x^4}{1+x^2}dx=\int \frac{x^4-1+1}{1+x^2}dx=\int \frac{(x^2-1)(x^2+1)}{x^2+1}+\frac{1}{x^2+1}dx=
> $$
> $$
> \int\frac{(x^2-1)\cancel{ (x^2+1) }}{\cancel{ x^2+1 }}dx+\int \frac{1}{x^2+1}dx=\int x^2dx-\int1dx+\int \frac{1}{1+x^2}dx=\frac{x^3}{3}-x+\arctan x {\; \color{red}+\; c}
> $$

> [!theorem|*] 
> תהי $f(x):\mathbb{R}\to \mathbb{R}$ כך ש-$f(x)\neq 0$. אזי:
> $$
> \int \frac{f'(x)}{f(x)}dx=\ln |f(x)|+c
> $$

נבדוק זאת ע"י גזירה:
$$
(\ln|f(x)|+c)'=\begin{cases}
\frac{f'(x)}{f(x)} & x>0 \\
\frac{-f'(x)}{-f(x)} & x<0
\end{cases}=\frac{f'(x)}{f(x)}
$$

**הוכחה:**
גזירה לפי כלל השרשרת.
$$
(\ln |f(x)|+c)'=\frac{|f'(x)|}{|f(x)|}=\frac{f'(x)}{f(x)}
$$
נסמן $\displaystyle F^*(x)=\int \frac{f'(x)}{f(x)}dx$ ואז:
$$
(F^*(x))'=\frac{f'(x)}{f(x)}=(\ln |f(x)|+c)'
$$
$$
\int \frac{f'(x)}{f(x)}dx=F^*(x)=\int (F^*(x))'dx=\int (\ln |f(x)|+c)'dx=\ln |f(x)|+c
$$
`\end{proof}`


> [!example|*] עוד דוגמה של אינטגרל כמעט מיידי
> $$
> \int \tan xdx=\int \frac{\sin x}{\cos x}dx \underset{\begin{matrix}
> \downarrow \\
> \R{\text{המשפט הנ"ל}}
> \end{matrix}}{=}-\ln |\cos x|+c
> $$

> [!remark|*] 
> לא לכל $f$ יש פונקציה קדומה. לדוגמה:
> ```desmos-graph
> width=200; height=200;
> bottom=-1; top=2
> ---
> f(x)=0 |x<0
> g(x)=1 |x>1
> ```
> לפי משפט דרבו, הפונקציה הנ"ל לא יכולה להיות נגזרת ולכן אין לה פונקציה קדומה.
> הפונקציה הקדומה אינה יכולה להיות הפונקציה הבאה שכן היא(הפונקציה הבאה) לא גזירה ב-$0$.
> ```desmos-graph
> width=200;height=200;
> bottom=-1;top=10
> ---
> f(x)=x |x>0
> g(x)=0 |x<0
> ```

## אינטגרציה בחלקים
יהיו שתי פונקציות $u,v$. אזי לפי נגזרת של מכפלה:
$$
(uv)'=(u(x)\cdot v(x))'=u'v+uv'
$$
נפעיל על שני האגפים אינטגרל(לפי ליניאריות נוכל להגיע לצורה הבאה):
$$
uv+c=\int u'v+\int uv'
$$
$$
\qquad \qquad \qquad \Downarrow - \R{\text{העברת אגפים}}
$$
$$
\int uv'=uv-\int u'v
$$
> [!theorem|*] שהוכחנו הרגע
> יהיו $u,v:\mathbb{R}\to \mathbb{R}$ בעלות פונקציה קדומה וגזירות. אזי:
> $$
> \int uv'=uv-\int u'v
> $$

> [!example|*] 
> $$
> \int xe^xdx \implies \begin{matrix}
> u=x & v'=e^x \\
> u'=1 & v=e^x
> \end{matrix} \implies \int xe^xdx=xe^x-\int e^xdx=xe^x-e^x+c
> $$
> **מומלץ תמיד לרשום מי זה $u$ ומי זה $v$ גם כשכבר סופר מיומנים באינטגרציה בחלקים**.
> נבדוק באמצעות נגזרת:
> $$
> (xe^x-e^x+c)'=e^x+xe^x-e^x=xe^x
> $$
> כנדרש.

> [!example|*] 
> $$
> \int e^x\cos xdx\implies \begin{matrix}
> v'=e^x & u=\cos x \\
> v=e^x & u'=-\sin x
> \end{matrix}\implies \int e^x\cos xdx=e^x\cos x+\int e^x\sin xdx
> $$
> עכשיו יש רגע של התלבטות - קיבלנו משהו שנראה באותה רמת קושי כמו שהתחלנו איתו. בואו ננסה עוד פעם(רק צריך להיזהר מהמלכודת של לעשות את אותו הדבר שוב ושוב כמו בלופיטל)
> $$
> \begin{matrix}
> u=\sin x & v'=e^x \\
> u'=\cos x & v=e^x
> \end{matrix}\implies e^x\cos x+\int e^x\sin xdx=e^x\cos x+e^x\sin x-\int e^x\cos xdx
> $$
> נשים לב כי הגענו לאינטגרל שהתחלנו ממנו. נשים לב בנוסף כי אנחנו יכולים להעביר אגף ולכן:
> $$
> 2\int e^x\cos xdx=e^x\cos x+e^x\sin x+c \implies \int e^x\cos xdx=\frac{e^x\cos x+e^x\sin x}{2}+c
> $$

> [!example|*] 
> $$
> \int \arctan xdx=\int 1\cdot \arctan xdx\implies \begin{matrix}
> v'=1 & u=\arctan x \\
> v=x & u'=\frac{1}{1+x^2}
> \end{matrix}
> $$
> $$
> \int 1\cdot \arctan xdx=x \arctan x-\int \frac{x}{1+x^2}dx=x\arctan x-\frac{1}{2}\ln |1+x^2|+c
> $$
> נבדוק באמצעות גזירה:
> $$
> \left( x \arctan x-\frac{1}{2}\ln |1+x^2|+c \right)'= HW
> $$

## אינטגרל של פונקציה רציונלית
> [!remark|*] 
> בתרגול: אינטגרל של פונקציה רציונלית.
> אני אוסיף את המשפטים מהתרגול פה למטה:

## שיטת ההצבה
> [!example|*] 
> $$
> \int \sin^2x\cos xdx \underset{\begin{pmatrix}
> t=\sin x \\
> \frac{dt}{dx}=\cos x \\
> \Downarrow - \R{\text{ההצדקה במשפט שיבוא}} \\
> dt=\cos xdx
> \end{pmatrix}}{=} \int t^2dt=\frac{t^3}{3}+c=\frac{\sin^3x}{3}+c
> $$
> בואו נשתכנע שזה נכון באמצעות גזירה:
> $$
> \left( \frac{\sin^3x}{3}+c \right)'=\frac{3\sin^2x\cos x}{3}=\sin^2x\cos x
> $$

> [!example|*] 
> $$
> \int 2xe^{x^2}dx \underset{\begin{pmatrix}
> t=x^2 \\
> dt=2xdx
> \end{pmatrix}}{=}\int e^tdt=e^t+c=e^{x^2}+c
> $$

המשפט שנראה, שנקרא שיטת ההצבה, הוא הדואלי של כלל השרשרת(כמו שאינטגרציה בחלקים זה הדואלי של נגזרת של מכפלה)
> [!theorem|*] שיטת ההצבה
> תהי $f:I\to \mathbb{R}$ בעלת פונקציה קדומה ב-$I$ ותהי $x=\varphi(t),\;\varphi:J\to I$ גזירה והפיכה. אזי:
> $$
> \int f(x)dx=\int f(\varphi(t))\varphi'(t)dt
> $$

**הוכחה:**
נסמן ב-$F$ פונקציה קדומה של $f$. 
$$
{\Large(}F(\varphi(t)){\Large)}'=F'(\varphi(t))\cdot \varphi'(t)=f(\varphi(t))\varphi'(t)
$$
נפעיל אינטגרל על שני האגפים:
$$
\int f(\varphi(t))\varphi'(t)dt=F(\varphi(t))+c=F(x)+c=\int f(x)dx
$$
`\end{proof}`

> [!remark|*] 
> אנו דורשים ש-$\varphi$ תהיה הפיכה על מנת שנוכל להשתמש גם בכיוון של $t=\varphi^{-1}(x)$ כפי שעשינו בדוגמות ממקודם.

> [!example|*] 
> $$
> x>0, \int \frac{\sqrt{ x }}{x+1}dx \underset{\begin{matrix}
> \downarrow \\
> \R{\text{שיטת ההצבה}} \\
> \begin{pmatrix}
> t=\sqrt{ x } \\
> x=t^2\; \leftarrow\; \varphi(t) \\
> dx=2tdt
> \end{pmatrix}
> \end{matrix}}{=}\int \frac{t}{t^2+1}2tdt=2\int \frac{t^2}{t^2+1}dt=2\int \frac{t^2-1+1}{t^2+1}dt=
> $$
> זה אותו פעלול שראינו קודם.
> $$
> \int \frac{t^2+1}{t^2+1}dt-\int \frac{1}{t^2+1}dt=t-\arctan t+c
> =2t-2\arctan t+c=2\sqrt{ x }-2\arctan \sqrt{ x }+c
> $$

> [!exercise|*] 
> תעשו את $\int e^{-|x|}dx$. יהיה משהו מאוד דומה בגליון בית.

> [!example|*] 
> $$
> \int \tan xdx=\int \frac{\sin x}{\cos x}dx \underset{\begin{matrix}
> \downarrow \\
> \R{\text{אינטגרציה בחלקים}} \\
> \begin{pmatrix}
> v'=\sin x & u=\frac{1}{\cos x} \\
> v=-\cos x & u'=-\frac{1}{\cos^2x}(-\sin x)
> \end{pmatrix}
> \end{matrix}}{=}-1+\int \frac{\sin x}{\cos x}dx=-1+\int \tan xdx
> $$
> אם ננסה לצמצם כמו ממקודם נקבל ש-$0=-1$ והכל נשבר. רק שבעצם זה בכלל $0+c=-1+c$ שזה נכון כי זו אותה משפחה של פונקציות.

