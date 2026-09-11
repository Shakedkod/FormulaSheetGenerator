---
cssclasses:
  - center-h1
  - center-images
---
עד כה ראינו [[4 - פונקציות|פונקציות]] $f:\mathbb{R}\to \mathbb{R}$. אנו יודעים כי אנו יכולים להחליף את השדה $\mathbb{R}$ בתחום ובטווח לכל מיני דברים שאנו רוצים: $\mathbb{C}$, חבורות, מ"ו שדות וכו'. (עקום שמדי פעם הזכרנו הוא פונקציה $f:\mathbb{R}\to \mathbb{R}^n$)
בקורס זה נתעסק לרוב עם $f:\mathbb{R}^n\to \mathbb{R}$ ובמיוחד עם $f:\mathbb{R}^2\to \mathbb{R}$. המעבר בין $\mathbb{R}^2$ ל-$\mathbb{R}^n$ הוא כמעט שקוף לחלוטין וקל מאוד לעשות אותו.

איך נוכל לדמיין את $\mathbb{R}^2$? נחשוב על איזור ברצפה עליו מוגדרת הפונקציה וציר ה-$z$ בו אנו מקבלים את ערכי התמונה פשוט יהיה מעל הרצפה הזו במרחב.
איך נראית נקודה במרחב? במקום $(x,y)$ כעת יש לנו נקודות שיראו $(x,y,z)$.
![[6 - פונקציות רב מימדיות 2026-06-16 08.37.51.excalidraw|800]]
נרצה להבין למה זה מסובך לצייר.
נניח ואנו רוצים לצייר את $z=f(x,y)=x^2+y^2$ שזוהי הכללה של פרבולה.
איך נוכל לצייר? נוכל לבצע משהו שנקרא _הקפאת משתנים_ - נקח משתנה אחד ונקבע אותו ואז נקבל פונקציה עם משתנה אחד כמו שאנו מכירים.
נניח נקבע $x=0$ אזי נוכל כעת להסתכל על כל הנקודות שעל ציר ה-$y$. במקטע הזה נקבל $z=y^2$. כך יראה הגרף רק עבור נקודות שעל ציר $y$.
כעת, נוכל לבצע את אותו הדבר בקביעת $y=0$ וציור הפרבוצה שיוצאת על ציר ה-$x$.
![[6 - פונקציות רב מימדיות 2026-06-16 08.42.35.excalidraw]]
פה יש הבדלים בין אנשים שונים אשר חלקים יכולים לדמיין את זה בקלות והאחרים לא יכולים להבין דבר גם כשהם רואים את הציור.
מה כעת עוד נוכל לצייר? זוכל לצייר את כל הנקודות שבהן $z=1$. אלו כל הנקודות שבהן $x^2+y^2=1$ שזה בדיוק מעגל היחידה "על הרצפה" שכן זה התחום ומעל הנקודות האלו ערך הפונקציה הוא 1.
לאחר שציירנו את המעגל נוכל לבחור $z$-ים אחרים ולצייר עוד מעגלים וכך לקבל רעיון יותר טוב לצורה שנקבל:
![[6 - פונקציות רב מימדיות 2026-06-16 08.48.51.excalidraw]]
זה נקרא **פרבולואיד** והיא אחת מהצורות שראינו בוובוורקים של ההכנה שעשינו. ("נכון עשיתם?" - צנזור)

עוד דרך שניתן לחשוב על גרפים כאלו הוא בעזרת מפה טופוגרפית אשר יכולה לתאר לנו את הגובה של הפונקציה התלת מימדית בצורה דו מימדית שאנחנו מכירים:
![[6 - פונקציות רב מימדיות 2026-06-16 08.52.47.excalidraw]]
> [!definition] קו גובה
> עקום $\ell$ במישור $(x,y)$ נקרא **קו גובה** של $f(x,y)$ אם ערך הפונקציה על $\ell$ הוא קבוע $c$.

^5ede4156

אזי, איך תראה המפה הטופוגרפית של $f(x,y)=x^2+y^2$? בדיוק כך:
![[6 - פונקציות רב מימדיות 2026-06-16 08.55.33.excalidraw]]

נרצה כעת לצייר מפה טופוגרפית של פונקציה שאנחנו לא מכירים: $z=f(x,y)=xy$.
נסתכל תחילה על $z=0$ ונקבל שקיימים שני ישרים כאלו שכן $xy=0$ אם ורק אם $x=0$ או $y=0$.
מתי $xy=1$? כאשר $y=\frac{1}{x}$ וכש-$x=\frac{1}{y}$ ואז דברים אלו אנו יודעים לצייר.
![[6 - פונקציות רב מימדיות 2026-06-16 08.59.26.excalidraw]]
הצורה הזו נקראת עוקף אשר מייצגת שני הרים באלכסון ושני עמקים באלכסון. קשה מאוד לצייר אותה.

# גבול ב[[5 - העולם הרב מימדי|רב מימד]]
> [!definition] גבול ב-$2D$
> תהי $f:\mathbb{R}^2\to \mathbb{R}$ מוגדרת בסביבה מנוקבת של $(a,b)$.
> נאמר כי $\displaystyle \lim_{ (x,y) \to (a,b) }f(x,y)=L$ אם לכל $\epsilon>0$ קיימת $\delta>0$ כך ש-
> $$
> |f(x,y)-L|<\epsilon \impliedby \underbrace{0<\sqrt{ (x-a)^2+(y-b)^2 } < \delta}_{ \displaystyle 0<d\left(\begin{pmatrix}
> x  \\
> y
> \end{pmatrix},\begin{pmatrix}
> a \\
> b
> \end{pmatrix}\right)< \delta}
> $$

> [!theorem|*] הגדרה שקולה לגבול
> תהי $f:\mathbb{R}^2\to \mathbb{R}$ מוגדרת בסביבה מנוקבת של $(a,b)$.
> נאמר כי $\displaystyle \lim_{ (x,y) \to (a,b) }f(x,y)=L$ אם לכל $\epsilon>0$ קיימת $\delta>0$ כך ש-
> $$
> |f(x,y)-L|<\epsilon \impliedby (x,y) \neq (a,b) \;\;\land\;\; |x-a|<\delta \;\;\land\;\; |y-b|<\delta
> $$

זוהי בעצם הגדרה עם סביבה ריבועית במקום כדורית.

> [!theorem|*] היינה
> $\displaystyle \iff \lim_{ (x,y) \to (a,b) } f(x,y)=L$ לכל סדרה $(a,b)\neq (x_{n},y_{n}) \underset{n\to \infty}{\longrightarrow} (a,b)$ מתקיים:
> $$
> f(x_{n},y_{n}) \underset{n\to \infty}{\longrightarrow} L
> $$

> [!exercise|*] 
> נסחו והוכיחו את **כל** המשפטים:
> - חשבון גבולות
> - יחידות הגבול
> - סנוויץ'
> - חסומה כפול אפסה
> 
> > [!remark|*] 
> > צנזור לא באמת מצפה שנוכיח הכל, הוא מצפה שננסה להוכיח עד שזה בא לנו קל :)
> 

> [!example|*] 
>  $$
> f(x,y)=\begin{cases} x\sin \frac{1}{y}+y\sin \frac{1}{x} & \R{\text{אחרת}} \\ 0 & x=0 \lor y=0\end{cases}
> $$
> איך נראה הגרף? **לא יודע** ("לא יודע זו תשובה טובה" - צנזור)
> מה יהיה הגבול בכל נקודה שבה $x,y$ לא שווים ל-$0$? זו תהיה פשוט פונקציה רציפה.
> איפה משהו יכול להשתבש? על הצירים. נבדוק האם הגבול ב-$(0,0)$ הוא 0.
> יש לנו 3 הגדרות גבול ולכן נדרש לבחור אחת. בדוגמה הזו נבחר את ההגדרה עם הסביבה הריבועית.
> יהי $\epsilon>0$. נגדיר $\delta=\frac{\epsilon}{2}$ ואז אם $x,y$ מקיימים $|x-0|<\delta$ וגם $|y-0|<\delta$ וגם $(x,y)\neq (a,b)$ אזי:
> $$
> |f(x,y)\!-\!0| \!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\underset{\begin{matrix}
> \vert \\
> \downarrow \\
> \epsilon>\R{\text{ זה 0 ולכן}}y=0 \;\lor\; x=0\R{\text{עבור }}
> \end{matrix}}{=}\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \left| x\sin \frac{1}{y}\!+\!y\sin \frac{1}{x} \right| \!\!\!\!\!\!\!\!\!\!\underset{\begin{matrix}
> \downarrow \\
> \R{\text{אי שוויון המשולש}}
> \end{matrix}}{\leq}\!\!\!\!\!\!\!\!\!\! \left| x\sin \frac{1}{y} \right|\!+\!\left| y \sin \frac{1}{x} \right|\leq |x|+|y|=|x-0|+|y-0|< \frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon
> $$

> [!theorem|*] 
> אם קיים $\displaystyle \lim_{ (x,y) \to (a,b) }f(x,y)=L$ אז ערך הפונקציה שואף ל-$L$ לאורך כל מסלול(עקום) ששואף ל-$(a,b)$.

> [!remark|*] 
> אם יש שני מסלולים שונים שמתקרבים ל-$(a,b)$ שלאורכם ערך הפונקציה שואף לשני ערכים שונים או לא קיים, אזי, אין גבול ב-($a,b$)

> [!example|*] 
> $$
> f(x,y)=\begin{cases}
> \displaystyle \frac{xy}{x^2+y^2} & (x,y)\neq (0,0) \\
> 0 & (x,y)=(0,0)
> \end{cases}
> $$
> נראה כי $\displaystyle \lim_{ (x,y) \to (0,0) } f$ לא קיים.
> נתחיל לבדוק מסלולים שמתקרבים לנק' $(0,0)$.
> נסתכל על $y=mx$. על מסלול שכזה הפונקציה תהא: $f(x,mx)$ ואז:
> $$
> f(x,mx)=\frac{xmx}{x^2+m^2x^2}=\frac{m}{1+m^2} \underset{x\to 0}{\longrightarrow} \frac{m}{1+m^2}
> $$
> גילינו פה כי לאורך קו ישר, ערך הפונקציה לא תלוי ב-$x$ והוא שונה לכל שיפוע של קו ישר.
> _מסקנה:_ יש גבולות שונים לערכי $m$ שונים, כלומר עבור מסלולים שונים ולכן $\lim_{ (x,y) \to (0,0) }f(x,y)$ לא קיים לפי שלילת המשפט הנ"ל.

> [!example|*] 
> $$
> f(x,y)=\begin{cases}
> \frac{x^2y}{x^4+y^2} & \R{\text{אחרת}} \\
> 0 & (x,y)=(0,0)
> \end{cases}
> $$
> עבור $y=mx$:
> $$
> f(x,mx)=\frac{x^3m}{x^4+x^2m^2}=\frac{mx}{x^2+m^2} \underset{x\to 0}{\longrightarrow} 0
> $$
> זה לא תלוי ב-$m$(אך לא מתקיים עבור $m=0$ כמובן)
> נבדוק כרגע מה קורה עבור $m=0$:
> $$
> f(x,0)=\frac{0}{x^4}=0 \longrightarrow 0
> $$
> מה גילינו? כי כל המסלולים שהם קווים ישרים הערך שואף ל-0.
> האם זה אומר שהגבול בראשית הוא 0? **לא** - כמה מסלולים נשאר לנו לבדוק? $\infty$.
> מה קורה עבור $y=x^2$?
> $$
> f(x,x^2)=\frac{x^4}{x^4+x^4}=\frac{1}{2} \underset{x\to0}{\longrightarrow} \frac{1}{2} \neq 0
> $$
> _מסקנה:_ אין גבול ב-$(0,0)$.

## גבולות נשנים
> [!definition] גבול נשנה
> $\displaystyle \lim_{ y \to b } {\Large (}\lim_{ x\to a } f(x,y){\Large )}$ נקרא **גבול נשנה**.

זה לא אותו הדבר כמו להשאיף את שני המשתנים בו"ז כפי שראינו קודם.
**אזהרה:** בדרך כלל לא עוזרים, מבלבלים ומטעים. **ראו הוזהרתם**.

> [!theorem|*] 
> אם $\displaystyle \lim_{ (x,y) \to (a,b) }f(x,y)$ קיים ואם קיים גבול נשנה, אז הם שווים.

> [!theorem|*] 
> תהי $f(x,y)$ פונקציה המקיימת $f(r\cos\theta,r\sin\theta)=F(r)\cdot G(\theta)$ כאשר $G(\theta)$ חסומה ו-$F(r) \underset{r\to 0}{\longrightarrow}0$ אזי מתקיים:
> $$
> \lim_{ (x,y) \to (0,0) } f(x,y)=0
> $$

> [!example|*] 
> $$
> f(x,y)=\begin{cases}
> \frac{x^2y^2}{x^2+y^2} & (x,y)\neq (0,0) \\
> 0 & (x,y)=(0,0)
> \end{cases}
> $$
> $$
> f(r\cos \theta,r\sin\theta)=\frac{r^4\cos^2\theta \sin^2\theta}{r^2}=\underbracket{r^2}_{F(r)}\cdot \underbracket{\cos^2\theta \sin^2\theta}_{G(\theta)}
> $$
> נשים לב כי $F(r)$ מתכנסת ל-$0$ כאשר $r\to 0$ ובנוסף $G$ חסומה. לכן, לפי המשפט:
> $$
> \lim_{ (x,y) \to (0,0) } f(x,y)=0
> $$

**הוכחה:**
>[!hw] HW
> איך תראה ההוכחה? צריך להראות את הגדרת הגבול

`\end{proof}`

# רציפות וגזירות
## רציפות
> [!definition] פונקציה רציפה
> נאמר כי $f(x,y)$ רציפה בנקודה $(a,b)$ אם
> $$
> \lim_{ (x,y) \to (a,b) } f(x,y)=f(a,b)
> $$

> [!definition] רציפות בתחום פתוח
> $f$ רציפה בתחום **פתוח** אם היא רציפה בכל נקודה בתחום.

> [!definition] רציפות בנקודת שפה
> $f$ רציפה **בנקודת שפה** אם $|f(x,y)-f(a,b)|<\epsilon \impliedby 0<\sqrt{ (x-a)^2+(y-b)^2 } < \delta$ מתקיים עבור $(x,y) \in D$.

> [!theorem|*] ווירשטראס
> אם $f(x,y)$ רציפה בתחום קומפקטי(סגור וחסום) אז:
> 1. $f$ חסומה.
> 2. $f$ מקבלת מינימום ומקסימום.

ההוכחה היא כמעט אחד לאחד כמו ההוכחה של $W$ במשתנה יחיד.

> [!theorem|*] הרכבה של רציפות היא רציפה
> יהיו $x(t),y(t)$ רציפות בקטע $[a,b]$.
> יהי $D \subseteq \mathbb{R}^2$ תחום (פתוח) המכיל את $(x(t),y(t))$ לכל $t \in[a,b]$ ותהי $f:D\to \mathbb{R}$ רציפה.
> נגדיר $\varphi(t)=f(x(t),y(t))$. אזי, $\varphi$ רציפה ב-$[a,b]$.

ההוכחה סטנדרטית ודומה מאוד להוכחה במשתנה יחיד.

> [!theorem|*] ערך הביניים
> תהי $D \subseteq \mathbb{R}^n$ קבוצה פתוחה וקשירה ותהי $f:D\to \mathbb{R}$ רציפה.
> יהיו $\underline{x}=(x_{1},x_{2},\dots,x_{n}),\underline{y}=(y_{1},y_{2},\dots,y_{n})\in D$ אזי לכל ערך $z_{0}$ בין $f(\underline{x})$ ל-$f(\underline{y})$ קיימת נק' $\underline{w}=(w_{1},\dots,w_{n})\in D$ כך ש-$f(\underline{w})=z_{0}$.

**הוכחה:**
נחבר את $\underline{x}$ ל-$\underline{y}$ ע"י עקום רציף שמוכל ב-$D$ וקיים בהכרח שכן $D$ קבוצה קשירה.
נסמן את העקום ע"י $\gamma(t)$ כאשר $t \in[a,b]$.
$$
f(\underline{x})=f(x_{1},x_{2},\dots,x_{n})=f(x_{1}(a),x_{2}(a),\dots,x_{n}(a))=\varphi(a) \;\;\;\R{\text{בסימוני המשפט הקודם:}}
$$
$$
f(\underline{y})=f(y_{1},y_{2},\dots,y_{n})=f(y_{1}(x_{1}(b),x_{2}(b),\dots,x_{n}(b))=\varphi(b)
$$
לפי המשפט הקודם $\varphi$ רציפה ב-$[a,b]$. לכן, לפי [[4 - פונקציות#^c7dea1|ערך הביניים במשתנה יחיד]], קיים $a<t_{0}<b$ כך ש-$\varphi(t_{0})=z_{0}$.
$$
\varphi(t_{0})=f(x_{1}(t_{0}),x_{2}(t_{0}),\dots,x_{n}(t_{n}))
$$
נסמן $(x_{1}(t_{0}),x_{2}(t_{0}),\dots,x_{n}(t_{0}))=\underline{w}\in D$ כי היא נקודה על העקום.
`\end{proof}`

> [!example|*] 
> תהי $f(x,y)=\begin{cases}\frac{x^2-y^2}{x^2+y^2} & (x,y)\neq(0,0) \\ 0 & (x,y)=(0,0)\end{cases}$ נראה שלא רציפה ב-$0$.
> [להשלים - זה פשוט]

## גזירות
### נגזרות חלקיות
> [!definition] נגזרת חלקית בציר $x_{i}$
> תהי $f:\mathbb{R}^n\to \mathbb{R}$.
> הנגזרת החלקית(נ"ח) שלה בנקודה $\underline{x}^0$ מוגדרת להיות:
> $$
> \parder{f}{x_{1}}(\underline{x}^0)=\lim_{ h \to 0 } \frac{f(x_{1}+h,x_{2},\dots,x_{n})-f(x_{1},x_{2},\dots,x_{n})}{h}
> $$

> [!example|*] 
> עבור פונקציה $f:\mathbb{R}^2\to \mathbb{R}$  המוגדרת $f(x,y)$ הנ"ח בנק' $(x_{0},y_{0})$ תהיה:
> $$
> \parder{f}{x}(x_{0},y_{0})=\lim_{ h \to 0 } \frac{f(x_{0}+h,y_{0})-f(x_{0},y_{0})}{h}
> $$
> $$
> \parder{f}{y}(x_{0},y_{0})=\lim_{ h \to 0 } \frac{f(x_{0},y_{0}+h)-f(x_{0},y_{0})}{h}
> $$

> [!example|*] 
> $$
> f(x,y)=\begin{cases}
> \frac{xy}{x^2+y^2} & \R{\text{אחרת}} \\
> 0 & (0,0)
> \end{cases}
> $$
> $$
> \parder{f}{x}(2,3)=\left.\frac{y(x^2+y^2)-xy(2x)}{(x^2+y^2)^2}\begin{matrix}
> \\ \\ \\ \\
> \end{matrix}\right\vert_{(2,3)}=\frac{15}{169}
> $$
> $$
> \parder{f}{x}(0,0)=\lim_{ h \to 0 } \frac{f(h,0)-f(0,0)}{h}=\lim_{ h \to 0 } \frac{f(h,0)}{h}=\lim_{ h \to 0 } \frac{\frac{0}{h^2}}{h}=\lim_{ h \to 0 } 0=0
> $$

> [!remark|*] 
> 1. $\parder{f}{x}$ ו-$\parder{f}{y}$ הן פונקציות **בשתי משתנים**!!!
> 2. $f$ רציפה בנק' לא גורר שיהיו לה נגזרות חלקיות באותה הנקודה.
> 3. ל-$f$ קיימות נגזרות חלקיות בנק' לא גורר ש-$f$ רציפה באותה הנקודה.

> [!example|*] 
> $$
> f(x,y,z)=e^{xy}+z\cos x
> $$
> נרצה לחשב את הנגזרות החלקיות: (הפונקציה אלמנטרית ולכן נוכל לגזור אותה לפי חוקי גזירה)
> $$
> f_{x}=f'_{x}=\parder{f}{x}(x,y,z)=ye^{xy}-z\sin x
> $$
> $$
> \parder{f}{y}(x,y,z)=xe^{xy} \qquad \qquad \parder{f}{z}(x,y,z)=\cos x
> $$
> בואו נחשב כעת נגזרת שנייה. יש לנו $9$ אפשרויות לנגזרות חלקיות.
> הסימונים מבלבלים מאוד ולכן נסתכל עליהם לרגע:
> $$
> f''_{xy}=(f'_{x})_{y}'=\parder{}{y}\left(\parder{f}{x}\right)=\parder{^2 f}{y \partial x}
> $$
> כעת נבצע את החישוב:
> $$
> \nparder{2}{f}{x}=y^2e^{xy}-z\cos x \qquad \parder{^2f}{y \partial x}=e^{xy}+xye^{xy} \qquad \parder{^2f}{z \partial x}=-\sin x
> $$
> $$
> \parder{^2f}{x \partial y}=e^{xy}+xye^{xy} \qquad \nparder{2}{f}{y}=x^2e^{xy} \qquad \parder{^2f}{z \partial y}=0
> $$
> $$
> \parder{^2f}{x \partial z}=-\sin x \qquad \parder{^2f}{y \partial z}=0 \qquad \nparder{2}{f}{z}=0
> $$
> נגזרות חלקיות מסדר 2 ומעלה הן אולי האובייקט הכי שימושי בפיזיקה ומדעי המחשב (לפי צנזור)

נשים לב כי בדוגמה האחרונה קיבלנו כי חלק מהנ"ח מסדר שני שוות, זה לא במקרה.
> [!theorem|*] שוורץ
> אם $f \in C^2$ (כלומר, קיימות ל-$f$ נ"ח רציפות מסדר $\mathrm{II}$) אז הנ"ח המעורבות שוות.
> כלומר, עבןר $f(x,y)$ מתקיים $f''_{xy}=f''_{yx}$.

> [!example|*] לפונקציות שאינן מקיימות את משפט שוורץ
> $$
> f(x,y)=\begin{cases}
> \frac{x^3}{x^2+y^2} & else \\
> 0 & (0,0)
> \end{cases} \qquad \qquad f(x,y)=\begin{cases}
> xy \frac{x^2-y^2}{x^2+y^2} & else \\
> 0 & (0,0)
> \end{cases}
> $$
> 

### גזירות
> [!remark|*] תזכורת
> $f(x)$ גזירה בנקודה $\iff x_{0}$ קיים $A \in \mathbb{R}$ וקיימת $\alpha(h)\underset{h\to 0}{\longrightarrow}0$ כך ש-$f(x_{0}+h)-f(x_{0})=Ah+\alpha(h)h$.

> [!definition] גזירות ב-$\mathbb{R}^n$
> תהי $f(\underline{x})=f(x_{1},x_{2},\dots,x_{n})$ מוגדרת בסביבה של $\underline{x}^0\in \mathbb{R}^n$.
> נאמר כי $f$ **גזירה** ב-$\underline{x}^0$ אם קיים $\underline{A} \in \mathbb{R}^n$ כך ש:
> $$
> f(\underline{x}^0+\underline{h})-f(\underline{x}^0)=\underline{A}\cdot\underline{h}+\alpha(\underline{h})\left\lVert \underline{h} \right\rVert
> $$
> כאשר $\alpha(\underline{h})\underset{\underline{h}\to \underline{0}}{\longrightarrow}0$.

> [!theorem|*] הגדרה שקולה
> $$
> f(\underline{x}^0+\underline{h})-f(\underline{x}^0)=\underline{A}\cdot\underline{h}+\alpha_{1}(\underline{h})h_{1}+\alpha_{2}(\underline{h})h_{2}+\dots+\alpha_{n}(\underline{h})h_{n}
> $$
> כאשר לכל $i$ מתקיים $\alpha_{i}(\underline{h})\longrightarrow0$.

> [!theorem|*] הגדרה שקולה נוספת
> $$
> \lim_{ \underline{h} \to \underline{0} } \frac{f(\underline{x}^0+\underline{h})-f(\underline{x}^0)-\underline{A}\cdot\underline{h}}{\left\lVert \underline{h} \right\rVert }=0
> $$

> [!remark|*] 
> לפעמים, נניח בשני מימדים, נוכל לראות שבמקום $\underline{h}=(h,k)$ כותבים $\underline{h}=(\Delta x,\Delta y)$ כדי להדגיש שזה שינוי קטן ב-$x$ או ב-$y$ בהתאמה.
> $$
> \Delta f=f(x_{0}+h,y_{0}+k)-f(x_{0},y_{0})=f(x_{0}+\Delta x,y_{0}+\Delta y)-f(x_{0},y_{0})=\cdots
> $$

> [!theorem|*] 
> אם $f$ גזירה ב-$\underline{x}^0\in \mathbb{R}^n$ אז יש לה נ"ח ב-$\underline{x}^0$ ומתקיים:
> $$
> \forall 1\leq i \leq n:\;\; A_{i}=\parder{f}{x_{i}}(\underline{x}^0)
> $$

**הוכחה:** (ב-$\mathbb{R}^2$)
נציב $k=0$ בהגדרת הנגזרת:
$$
f(x_{0}+h,y_{0})-f(x_{0},y_{0})=Ah+\alpha(h,0)|h|\implies \frac{f(x_{0}+h,y_{0})-f(x_{0},y_{0})}{h}=A+\alpha(h,0) \frac{|h|}{h}
$$
נשאיף את $h$ ל-$0$.
$$
\lim_{ h \to 0 } A+\alpha(h,0) \frac{|h|}{h} \underset{\begin{matrix}
\downarrow \\
\R{\text{חסומה כפול אפסה}}
\end{matrix}}{=}A
$$
ולכן:
$$
\parder{f}{x}=\lim_{ h \to \infty } \frac{f(x_{0}+h,y_{0})-f(x_{0},y_{0})}{h}=A
$$
באופן דומה עבור $\parder{f}{y}$.
`\end{proof}`

> [!theorem|*] 
> אם $f$ גזירה ב-$\underline{x}^0\in \mathbb{R}^n$ אז היא רציפה ב-$\underline{x}^0$.

**הוכחה:** (ב-$\mathbb{R}^2$)
$$
\lim_{ (h,k) \to (0,0) } (f(x_{0}+h,y_{0}+k)-f(x_{0},y_{0}))\underset{\begin{matrix}
\downarrow \\
\R{\text{הגדרת הנגזרת}}
\end{matrix}}{=}\lim_{ (h,k) \to (0,0) } \left(Ah+Bk+\alpha(h,k)\sqrt{ h^2+k^2 }\right)=0
$$
לכן, לפי חשבון גבולות:
$$
\lim_{ (h,k) \to (0,0) } f(x_{0}+h,y_{0}+h)=f(x_{0},y_{0})
$$
ולכן, לפי הגדרה, $f$ רציפה ב-$(x_{0},y_{0})$.
`\end{proof}`

> [!theorem|*] 
> אם ל-$f$ יש נ"ח רציפות בסביבת הנקודה $\underline{x}^0\in \mathbb{R}^n$ אז $f$ גזירה ב-$\underline{x}^0$.

**הוכחה:** (ב-$\mathbb{R}^2$)
נתון כי קיימת סביבה של $(x_{0},y_{0})$ בה הנ"ח של $f$ רציפות. כלומר, קיימת $\delta>0$ כך שלכל $(x,y)$ המקיימים  $d((x,y),(x_{0},y_{0}))<\delta$ הנ"ח של $f$ קיימות ורציפות בנק' $(x,y)$. נסמן סביבה זו $U$.
אזי, לכל $(x,y)\in U$ נסמן:
$$
\alpha(x,y)=f(x,y)-f(x_{0},y_{0})-\parder{f}{x}(x_{0},y_{0})\cdot (x-x_{0})-\parder{f}{y}(x_{0},y_{0})\cdot(y-y_{0})
$$
על מנת להוכיח כי $f$ גזירה ב-$(x_{0},y_{0})$ נדרש להוכיח כי $\lim_{ (x,y) \to (x_{0},y_{0}) } \frac{\alpha(x,y)}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }}=0$.
יהי $\epsilon>0$ יהיו $(x,y)\in U$ ואז:
$$
f(x,y)-f(x_{0},y_{0})=f(x,y)-f(x_{0},y)+f(x_{0},y)-f(x_{0},y_{0})
$$
מכיוון שהנ"ח של $f$ בכיוון $y$ קיימת בכל נקודה ב-$U$, אנו מקבלים בפרט כי הפונקציה $f(x_{0},\cdot)$ (במשתנה השני) היא פונקציה גזירה. לכן, ממשפט לגרנז', לכל $y$ כך ש-$(x_{0},y)\in U$ קיים $c_{1}$ בין $y_{0}$ ל-$y$ כך שמתקיים:
$$
f(x_{0},y)-f(x_{0},y_{0})=\parder{f}{y}(x_{0},c_{1})\cdot (y-y_{0})
$$
באופן דומה, לכל $y$ בסביבה מספיק קטנה של $y_{0}$, הפונקציה $f(\cdot,y)$ (במשתנה הראשון) היא פונקציה גזירה.
לכן, ממשפט לגרנז', לכל $x$ כך ש-$(x,y)\in U$ קיים $c_{2}$ בין $x_{0}$ ל-$x$ כך שמתקיים:
$$
f(x,y)-f(x_{0},y)=\parder{f}{x}(c_{2},y)\cdot (x-x_{0})
$$
נציב את המשוואות הנ"ל במשוואה ממקודם:
$$
f(x,y)-f(x_{0},y_{0})=\parder{f}{x}(c_{2},y)\cdot(x-x_{0})+\parder{f}{y}(x_{0},c_{1})\cdot(y-y_{0})
$$
לכן מתקיים:
$$
\begin{align}
\frac{\alpha(x,y)}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }}&= \frac{f(x,y)-f(x_{0},y_{0})-\parder{f}{x}(x_{0},y_{0})\cdot (x-x_{0})-\parder{f}{y}(x_{0},y_{0})\cdot (y-y_{0})}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }} \\
&\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!=\frac{\parder{f}{x}(c_{2},y)\cdot (x-x_{0})+\parder{f}{y}(x_{0},c_{1})\cdot(y-y_{0})-\parder{f}{x}(x_{0},y_{0})\cdot(x-x_{0})-\parder{f}{y}(x_{0},y_{0})\cdot(y-y_{0})}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }} \\
&=\frac{\left( \parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0}) \right)(x-x_{0})+\left( \parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0}) \right)(y-y_{0})}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }}
\end{align}
$$
נסמן $h=x-x_{0}$ ו-$k=y-y_{0}$ ואז:
$$
\begin{align}
\left| \frac{\alpha(x,y)}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }} \right|&\leq \left| \frac{\parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot h \right|+\left| \frac{\parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot k \right|
\end{align}
$$
מכיוון שכאשר $(x,y)$ שואף ל-$(x_{0},y_{0})$ מתקיים כי $(c_{2},c_{1})$ שואף אף הוא ל-$(x_{0},y_{0})$ ומרציפות $\parder{f}{x},\parder{f}{y}$ מתקיים כי:
$$
\begin{matrix}
\displaystyle \lim_{ (x,y) \to (x_{0},y_{0}) } \parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0})=0 \\
\displaystyle \lim_{ (x,y) \to (x_{0},y_{0}) } \parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0})=0
\end{matrix}
$$
בנוסף, נשים לב כי: $|h|\leq \sqrt{ h^2+k^2 }$ ולכן $\displaystyle \left| \frac{h}{\sqrt{ h^2+k^2 }} \right|\leq 1$ ובאותו אופן $\displaystyle \left| \frac{k}{\sqrt{ h^2+k^2 }} \right|<1$ ואז לפי חסומה כפול אפסה נקבל כי:
$$
\left| \frac{\parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot h \right| \rarrowlim{(x,y)\to(x_{0},y_{0})}0 
$$
$$
\left| \frac{\parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot k \right| \rarrowlim{(x,y)\to(x_{0},y_{0})}0
$$
לכן, לפי הגדרה, קיימת $\delta_{1}>0$ כך שלכל $(x,y)$ כך ש-$d((x,y),(x_{0},y_{0}))<\delta_{1}$ מתקיים:
$$
\left| \frac{\parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot h \right|< \frac{\epsilon}{2}
$$
וקיימת $\delta_{2}>0$ כך שלכל $(x,y)$ כך ש-$d((x,y),(x_{0},y_{0}))<\delta_{2}$ מתקיים:
$$
\left| \frac{\parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot k \right|< \frac{\epsilon}{2}
$$
לכן, עבור $\delta=\min\left\{ \delta_{1},\delta_{2} \right\}$, לכל $(x,y)$ כך ש-$d((x,y),(x_{0},y_{0}))<\delta$ מתקיים:
$$
\left| \frac{\alpha(x,y)}{\sqrt{ (x-x_{0})^2+(y-y_{0})^2 }} \right|\!\!\leq\!\! \left| \frac{\parder{f}{x}(c_{2},y)-\parder{f}{x}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot h \right|\!+\!\left| \frac{\parder{f}{y}(x_{0},c_{1})-\parder{f}{y}(x_{0},y_{0})}{\sqrt{ h^2+k^2 }}\cdot k \right|\!<\! \frac{\epsilon}{2}+\frac{\epsilon}{2}\!=\epsilon
$$
ולכן, לפי הגדרה, $\lim_{ (x,y) \to (x_{0},y_{0}) } \frac{\alpha(x,y)}{\sqrt{ h^2+k^2 }}=0$ ולכן, לפי הגדרת גזירות, $f$ גזירה בנקודה $(x_{0},y_{0})$.
`\end{proof}`

> [!example|*] 
> $$
> f(x,y)=\begin{cases}
> (x^2+y^2)\sin \frac{1}{x^2+2y^2} & (x,y)\neq(0,0) \\
> 0 & (x,y)=(0,0)
> \end{cases}
> $$
> לפונקציה הזאת יש נ"ח ב-$(0,0)$ אבל הן לא רציפות ב-$(0,0)$.
> $f$ כן גזירה ב-$(0,0)$.

#### כלל השרשרת
> [!theorem|*] כלל השרשרת $\mathrm{I}$
> יהי $\underline{x} \in \mathbb{R}^n$ ותהי $f(\underline{x})$ גזירה בתחום $D$ ויהיו $x_{1}(t),x_{2}(t),\dots,x_{n}(t)$ גזירות בקטע $I$ כך שלכל $t \in I$ מתקיים $(x_{1}(t),x_{2}(t),\dots,x_{n}(t))\in D$.
> נגדיר $F(t)=f(x_{1}(t),x_{2}(t),\dots,x_{n}(t))$ אזי $F$ גזירה ומתקיים:
> $$
> F'(t)\!=\!\parder{f}{x_{1}}(x_{1}(t),\dots,x_{n}(t))\!\cdot\! \frac{dx_{1}}{dt}\!+\!\parder{f}{x_{2}}(x_{1}(t),\dots,x_{n}(t))\!\cdot \!\frac{dx_{2}}{dt}\!+\!\dots\!+\!\parder{f}{x_{n}}(x_{1}(t),\dots,x_{n}(t))\!\cdot \!\frac{dx_{n}}{dt}
> $$

> [!example|*] ולאחריה ההוכחה
> $$
> y(t)=2t \qquad x(t)=t^2 \qquad f(x,y)=x^2y-y^2
> $$
> $$
> F(t)=2t^5-4t^2
> $$
> $$
> F'(t)=(2x(t)y(t))\cdot 2t+(x^2(t)-2y(t))\cdot 2=8t^4+2t^4-8t=10t^4-8t
> $$
> נשים לב כי קיבלנו את התוצאה המתאימה.

**הוכחה:**
נתון כי $F(t)=f(x_{1}I(t),x_{2}(t),\dots,x_{n}(t))$
$$
\frac{dF}{dt}=\lim_{ \Delta t \to 0 } \frac{F(t+\Delta t)-F(t)}{\Delta t}=\lim_{ \Delta t \to 0 } \frac{f(x_{1}(t+\Delta t),\dots,x_{n}(t+\Delta t))-f(x_{1}(t),\dots,x_{n}(t))}{\Delta t}
$$
נסמן: $\Delta x_{1}=x_{1}(t+\Delta t)-x_{1}(t),\;\Delta x_{2}=x_{2}(t+\Delta t)-x_{2}(t),\dots,\;\Delta x_{n}=x_{n}(t+\Delta t)-x_{n}(t)$ ואז:
$$
\frac{dF}{dt}=\lim_{ \Delta t \to 0 } \frac{f(x_{1}(t)+\Delta x_{1},\dots,x_{n}(t)+\Delta x_{n})-f(x_{1}(t),\dots,x_{n}(t))}{\Delta t}
$$
נסמן את המונה ב-$\Delta f$ ואז:
$$
\frac{dF}{dt}=\lim_{ \Delta t \to 0 } \frac{\Delta f}{\Delta t}
$$
$f$ גזירה ולכן:
$$
\Delta f\!=\!\parder{f}{x_{1}}(x_{1}(t),x_{2}(t),\dots,x_{n}(t)) \Delta x_{1}\!+\!\cdots\!+\!\parder{f}{x_{n}}(x_{1}(t),x_{2}(t),\dots,x_{n}(t))\Delta x_{n}\!+\!\alpha_{1}(\Delta x_{1},\dots,\Delta x_{n})\Delta x_{1}+\dots+\alpha_{n}(\Delta x_{1},\dots,\Delta x_{n})\alpha_{n}
$$
נחלק ב-$\Delta t$ ונקבל:
$$
\frac{\Delta f}{\Delta t}=\parder{f}{ {1}}(\dots) \frac{\Delta x_{1}}{\Delta t}+\dots+\parder{f}{x_{n}}(\dots) \frac{\Delta x_{n}}{\Delta t}+\alpha_{1}(\dots) \frac{\Delta x_{1}}{\Delta t}+\dots+\alpha_{n}(\dots) \frac{\Delta x_{n}}{\Delta t}
$$
נשאיף $\Delta t\to0$ ונקבל:
$$
F'(t)=\parder{f}{x_{1}}\cdot \frac{dx_{1}}{dt}+\parder{f}{x_{2}}\cdot \frac{dx_{2}}{dt}+\dots+\parder{f}{x_{n}}\cdot \frac{dx_{n}}{dt}
$$
`\end{proof}`

המשפט הבא ינוסח ברשלנות(ב-$\mathbb{R}^2$) עד שיהיה לי כח לסדר אותו:
> [!theorem|*] כלל השרשרת $\mathrm{II}$
> עבור $F(u,v)=f(x(u,v),y(u,v))$ כך ש-$f,x,y$ גזירות אזי:
> $$
> \parder{F}{u}=\parder{f}{x}\cdot \parder{x}{u}+\parder{f}{y} \cdot \parder{y}{u}
> $$
> $$
> \parder{F}{v}=\parder{f}{x}\cdot \parder{x}{v}+\parder{f}{y} \cdot \parder{y}{v}
> $$

> [!example|*] 
> $$
> f(x,y)=e^{x^2y} \qquad x(u,v)=\sqrt{ uv } \qquad y(u,v)=\frac{1}{v}
> $$
> נחשב את הנ"ח של $F$ לפי $u$.
> $$
> \parder{F}{u}=2xye^{x^2y}\cdot \sqrt{ v } \frac{1}{2\sqrt{ u }}+x^2e^{x^2y}\cdot 0=xye^{x^2y} \frac{\sqrt{ v }}{\sqrt{ u }}=\frac{\sqrt{ uv }}{v} e^{\frac{uv}{v}} \frac{\sqrt{ v }}{\sqrt{ u }}=e^u \cdot \frac{v\sqrt{ u }}{v\sqrt{ u }}=e^u
> $$
> בדיקה:
> $$
> F(u,v)=e^u \implies \parder{F}{u}=e^u
> $$

### נגזרת מכוונת
> [!definition] נגזרת מכוונת
> יהי $\hat{u}\in \mathbb{R}^n$ (הכובע מסמל שהוא וקטור יחידה. כלומר, $\left\lVert \hat{u} \right\rVert=1$) 
> נגדיר:
> $$
> \parder{f}{{u}}(\underline{x}^0\in \mathbb{R}^n)=\lim_{ h \to 0 } \frac{f(\underline{x}^0+h\underline{u})-f(\underline{x}^0)}{h}
> $$
> בתנאי שהגבול קיים. $\parder{f}{u}$ נקראת **הנגזרת המכוונת** בכיוון $\hat{u}$ ב-$\underline{x}^0$.

> [!remark|*] ב-$\mathbb{R}^2$ זה יראה:
> $$
> \parder{f}{u}(x_{0},y_{0})=\lim_{ h \to 0 } \frac{f(x_{0}+hu_{1},y_{0}+hu_{2})-f(x_{0},y_{0})}{h}
> $$


> [!remark|*] 
> עבור $\hat{u}=(1,0)$ נקבל את $\parder{f}{x}$
> עבור $\hat{u}=(0,1)$ נקבל את $\parder{f}{y}$

> [!theorem|*] 
> תהי $f(\underline{x})$ גזירה ב-$\underline{x}^0\in \mathbb{R}^n$.
> אזי, הנגזרת המכוונת $\displaystyle \parder{f}{u}(\underline{x}^0)$ נתונה ע"י:
> $$
> \parder{f}{u}(\underline{x}^0)=\sum_{i=1}^n\parder{f}{x_{i}}(\underline{x}^0)\cdot u_{i}
> $$

**הוכחה:** (ב-$\mathbb{R}^2$)
$$
f(x_{0}+hu_{1},y_{0}+hu_{2})-f(x_{0},y_{0})=\underbracket{\parder{f}{x}}_{A}\cdot hu_{1}+\underbracket{\parder{f}{y}}\cdot hu_{2}+\alpha(hu_{1},hu_{2})\sqrt{ (hu_{1})^2+(hu_{2})^2 }
$$
$$
\frac{f(x_{0}+hu_{1},y_{0}+hu_{2})-f(x_{0},y_{0})}{h}=\parder{f}{x}\cdot u_{1}+\parder{f}{y}\cdot u_{2}+\alpha(hu_{1},hu_{2}) \frac{|h|}{h}
$$
$$
\lim_{ h \to 0 } \frac{f(x_{0}+hu_{1},y_{0}+hu_{2})-f(x_{0},y_{0})}{h}=\lim_{ h \to 0 } \parder{f}{x}\cdot u_{1}+\parder{f}{y}\cdot u_{2}\!+\!\alpha(hu_{1},hu_{2}) \!\frac{|h|}{h}=\parder{f}{x}u_{1}+\parder{f}{y}u_{2}
$$
`\end{proof}`

> [!example|*] 
> $$
> f(x,y)=\sqrt[3]{ xy^2 }
> $$
> נתחיל בלחשב נגזרת מכוונת לפי הגזרה.
> $$
> \parder{f}{u}(0,0)=\lim_{ h \to 0 } \frac{f(hu_{1},hu_{2})-f(0,0)}{h}=\lim_{ h \to 0 } \frac{\sqrt[3]{ hu_{1}(hu_{2})^2 }}{h}=\lim_{ h \to 0 } \sqrt[3]{ u_{1}u_{2}^2 }=\sqrt[3]{ u_{1}u_{2} }
> $$
> נשים לב כי זה לא משנה מה $u_{1},u_{2}$ למעט העובדה ש-$\sqrt{ u_{1}^2+u_{2}^2 }=1$ אך זה התנאי היחיד שלנו.
> בפרט:
> $$
> \parder{f}{x}(0,0)=0 \qquad \qquad \parder{f}{y}(0,0)=0
> $$
> נבדוק גזירות בראשית על פי הגדרה:
> $$
> \sqrt[3]{ hk^2 }-0=0+0+\alpha(h,k)\sqrt{ h^2+k^2 }
> $$
> אנו פה בעצם מניחים שהיא גזירה ובודקים אם התנאי מתקיים: כלומר, אם $f$ גזירה ב-$(0,0)$ אז בהכרח $A=\parder{f}{x}$ ו-$B=\parder{f}{y}$.
> $$
> \alpha(h,k)=\frac{\sqrt[3]{ hk^2 }}{\sqrt{ h^2+k^2 }}
> $$
> נבדוק אם $\alpha(h,k)$ שואפת לאפס (אם כן, אז על פי הגדרת הגזירות, הפונקציה גזירה. אחרת, לא)
> $$
> \alpha(r\cos\theta,r\sin\theta)=\frac{\sqrt[3]{ r\cos\theta r^2\sin^2\theta }}{r}=\sqrt[3]{ \cos\theta \sin^2\theta }
> $$
> נשים לב כי $F(r)=1$ לא שואפת ל-$0$ כאשר $r\to 0$ ולכן, לא נוכל להשתמש במשפט, שכן הוא לא אמ"מ.
> מה עושים? נשים לב כי הפונקציה $\alpha$ תלויה אך ורק בזווית עם ציר ה-$x$. היא לא משתנה ב-$r$. כלומר, לאורך ישרים דרך הראשית יש גבולות שונים ולכן אין לה גבול לפי משפט אחר ⟸ $f$ לא גזירה ב-$(0,0)$.

### קצת על מישור משיק
![[6 - פונקציות רב מימדיות 2026-06-23 09.33.20.excalidraw|900]]

נסתכל על כמה הגדרות שקולות למישור משיק:
- מישור שמכיל את המשיקים בנקודה $(x_{0},y_{0},f(x_{0},y_{0}))$ לכל העקומים המוכלים במשטח (גרף הפונקציה)
- מישור שמקיים שהזוית בינו לבין מיתרים מנקודות על המשטח שואפת ל-$0$ כאשר הנקודות מתקרבות ל-$(x_{0},y_{0},f(x_{0},y_{0}))$.


### גרדיאנט
> [!definition] גרדיאנט
> יהי $\underline{x}^0\in \mathbb{R}^n$ נקודה ב-$\mathbb{R}^n$. אזי, **הגדיאנט** של $f$ בנקודה $\underline{x}^0$ הוא הוקטור $\displaystyle\left(\parder{f}{x_{1}}(\underline{x}^0),\parder{f}{x_{2}}(\underline{x}^0),\dots,\parder{f}{x_{n}}(\underline{x}^0)\right)$ ומסומן $grad(f)$ או $\nabla f$ 
> (סימן המשולש ההפוך נקרא $nabla$(נבל ביוונית) או דל(לב בפרסית))

> [!theorem|*] 
> אם $f$ גזירה אז $\displaystyle \parder{f}{u}=\vec{\nabla}f\cdot \hat{u}$.

**הוכחה:**
$$
\R{\text{ברור}}
$$
`\end{proof}`

> [!remark|*] 
> $\vec{\nabla}f$ הוא וקטור.
> $$
> \vec{\nabla}f:\mathbb{R}^n\to \mathbb{R}^n
> $$

נשים :LiHeart: כי:
1. $\displaystyle \parder{f}{u}$ מקבל ערך מקסימלי כאשר:
   $$
   \parder{f}{u}=\vec{\nabla}f\cdot \hat{u}=|\vec{\nabla}f||\hat{u}|\cos\alpha
   $$
   נשים לב כי עבור נקודה מסויימת $|\vec{\nabla}f|$ ו-$|\hat{u}|$ קבועים ולכן מה שמשפיע הוא הזווית בלבד.
   כלומר, נרצה ש-$\hat{u}$ יהיה באותו הכיוון $\vec{\nabla}f$.
   כלומר, מקבל ערך מקסימלי בכיוון הגרדיאנט.
2. $\displaystyle \parder{f}{u}$ מינימלי בכיוון המנוגד לגרדיאנט.
3. $\displaystyle \parder{f}{u}=0$ בכיוון ניצב לגרדיאנט.

# אינטגרלים
## אינטגרל פרמטרי
זהו לא אינטגרל כפול או שני נחשים, זה המקביל של נגזרת חלקית באינטגרלים.
אין פה תורה חדשה, אלא רק מעט חידושים על דברים שראינו.
> [!theorem|*]
> תהי $f(x,y)$ רציפה במלבן $[a,b]\times[c,d]$. נגדיר $\displaystyle F(y)=\int_{a}^b f(x,y)dx$.
> אזי, $F$ רציפה במ"ש ב-$[c,d]$.

^5caaf7

**הוכחה:**
$f$ רציפה ב[[5 - העולם הרב מימדי#^2c3b21|תחום קומפקטי]] ולכן, לפי קנטור-היינה, $f$ רציפה במ"ש.
יהי $\frac{\epsilon}{b-a}>0$. הפונקציה $f$ רציפה במ"ש ולכן קיימת $\delta>0$ כך שלכל $P,Q$ במלבן המקיימות $d(P,Q)<\delta$ מתקיים: $|f(P)-f(Q)|< \frac{\epsilon}{b-a}$.
נקח $y_{1},y_{2} \in[c,d]$ כך ש-$|y_{1}-y_{2}|<\delta$. אזי, לכל $x \in[a,b]$ מתקיים $d((x,y_{1}),(x,y_{2}))=\sqrt{ (x-x)^2+(y_{1}-y_{2})^2 }=|y_{1}-y_{2}|$ ולכן:
$$
|F(y_{1})-F(y_{2})|=\left| \int_{a}^b f(x,y_{1})dx-\int_{a}^b f(x,y_{2})dx \right| \underset{\begin{matrix}
\downarrow \\
\R{\text{מונוטוניות}}
\end{matrix}}{=}\left| \int_{a}^b (f(x,y_{1})-f(x,y_{2}))dx \right| 
$$
$$
\underset{\begin{matrix}
\downarrow \\
\R{\text{אי שוויון המשולש האינטגרלי}}
\end{matrix}}{\leq} \int_{a}^b \left| f(x,y_{1})-f(x,y_{2}) \right|dx< \int_{a}^b \frac{\epsilon}{b-a} dx \underset{\begin{matrix}
\downarrow \\
NL
\end{matrix}}{=}\epsilon
$$
לכן, לפי הגדרה, $F$ רציפה במ"ש ולכן רציפה.
`\end{proof}`

> [!theorem|*] כלל לייבניץ לגזירה תחת סימן האינטגרל
> תהי $f(x,y)$ מוגדרת במלבן $[a,b]\times[c,d]$ ונניח כי $\displaystyle \parder{f}{y}(x,y)$ רציפה במלבן ונניח כי $F(y)=\displaystyle \int_{a}^b f(x,y)dx$ מוגדרת לכל $y \in[c,d]$.
> אזי, $F$ גזירה ב-$[c,d]$ ומתקיים $F'(y)=\displaystyle \int_{a}^b \parder{f}{y}(x,y)dx$.

> [!remark|*] 
> אין צורך לדרוש רציפות.

ההוכחה הנכונה ברשימות של רון (ההוכחה בוידיאו **לא נכונה**)

> [!example|*] 
> $$
> F(x)=\int_{1}^2 \sin(xe^y)dy
> $$
> נחשב את $F'(x)$ באמצעות לייבניץ:
> $$
> f(x,y)=\sin(xe^y)
> $$
> היא מוגדרת בכל מלבן כי היא מוגדרת בכל $\mathbb{R}^2$.
> $$
> \parder{f}{x}=e^y\cos(xe^y)
> $$
> הנ"ח רציפה בכל $\mathbb{R}^2$ ולכן במלבן.
> $f$ רציפה לפי $y$ ולכן $F$ מוגדרת.
> עד כה **בדקנו את התנאים** וכעת אנו יכולים להשתמש במשפט:
> $$
> F'(x) \underset{\begin{matrix}
> \downarrow \\
> \R{\text{לייבניץ}}
> \end{matrix}}{=}\int_{1}^2 \parder{}{x}(\sin(xe^y))dy=\int_{1}^2 e^y\cos(xe^y)dy \overunderset{x\neq 0\;\R{\text{עבור:}}}{\begin{matrix}
> \downarrow \\
> t=xe^y \\
> dt=xe^ydy
> \end{matrix}}{=}\int_{xe}^{xe^2} \frac{1}{x}\cos t\,dt \underset{\begin{matrix}
> \downarrow \\
> NL
> \end{matrix}}{=}\left.\frac{1}{x}\cdot \sin t\right\vert_{t=xe}^{t=xe^2}
> $$
> $$
> F'(x)=\frac{1}{x}(\sin(xe^2)-\sin(xe))
> $$
> עבור $x=0$ נקבל:
> $$
> F'(x)=\int_{1}^2 e^ydy=e^2-e
> $$

> [!example|*] 
> נחשב את $\displaystyle \int_{0}^1 \frac{x}{(1+2x)^2}dx$.
> הכלי שנראה פה יעזור לנו בפתירת אינטגרלים מאוד מסובכים, למרות שזה לא אחד שכזה.
> נגדיר: $F(y)=\displaystyle\int_{0}^1 \frac{xdx}{(1+yx)^2}$ אנו רוצים לחשב את $F(2)$.
> נמצא פונקציה $f(x,y)$ כך ש-$\parder{f}{y}=\frac{x}{(1+yx)^2}$:
> $$
> \int \frac{x}{(1+yx)^2}dy=-\frac{1}{1+yx}+c
> $$
> נבחר $c=0$ ונגדיר $f(x,y)=-\frac{1}{1+yx}$ במלבן $[0,1]\times[1,3]$ שבו $f(x,y)$ וגם $\parder{f}{y}$ רציפות מהיותן אלמנטריות ומוגדרות.
> ⟸ תנאי לייבניץ מתקימיים.
> $$
> F(y)\!=\!\int_{0}^1 \parder{f}{y}(x,y)dx \underset{\begin{matrix}
> \downarrow \\
> \R{\text{לייבניץ}}
> \end{matrix}}{=} \frac{d}{dy}\int_{0}^1 -\frac{1}{1+yx}dx \underset{\begin{matrix}
> \downarrow \\
> NL
> \end{matrix}}{=} \frac{d}{dy}\left(\left.-\frac{1}{y}\ln(1+yx)\right\vert_{x=0}^{x=1} \right)=-\frac{d}{dy}\left( \frac{1}{y}\ln(1+y) \right)
> $$
> $$
> F(y)=-\frac{\frac{y}{1+y}-\ln(1+y)}{y^2}=\frac{\ln(1+y)-\frac{y}{y+1}}{y^2}
> $$
> $$
> F(2)=-\frac{1}{6}+\frac{\ln 3}{4}
> $$
> וזה הפתרון.

> [!remark|*] תזכורת - [[2 - האינטגרל המסויים#^474cbb|המשפט היסודי]]
> אם $f(x)$ רציפה ונגדיר $F(x)=\displaystyle\int_{a}^x f(t)dt$, אז $F$ גזירה ו-$F'(x)=f(x)$.
> _הכללה - כמה משפטים אחרי זה:_ עבור $F(x)=\displaystyle \int_{\alpha(x)}^{\beta(x)}f(t)dt$ אזי $F'(x)=f(\beta(x))\beta'(x)-f(\alpha(x))\alpha'(x)$.

> [!theorem|*] הכללה של משפט לייבניץ
> אם $f(x,y)$ גזירה ברציפות במלבן $[a,b]\times[c,d]$ והפונקציות $\alpha(y)$ ו-$\beta(y)$ גזירות בקטע $[c,d]$.
> נגדיר $F(y)=\displaystyle \int_{\alpha(y)}^{\beta(y)}f(x,y)dx$, אזי $F$ גזירה ומתקיים:
> $$
> F'(y)=\int_{\alpha(y)}^{\beta(y)} \parder{f}{y}(x,y)dx+f(\beta(y),y)\beta'(y)-f(\alpha(y),y)\alpha'(y)
> $$

_רעיון ההוכחה:_ נגדיר $\phi(s,t,y)=\displaystyle\int_{s}^t f(x,y)dx$ ⟸ מתקיים $F(y)=\phi(\alpha(y),\beta(y),y)$. לפי כלל השרשרת:
$$
\begin{align}
F'(y)&=\parder{\phi}{s}\cdot \frac{ds}{dy}+\parder{\phi}{t}\cdot \frac{dt}{dy}+\parder{\phi}{y}\cdot \frac{dy}{dy} \\
& =\parder{\phi}{s} \alpha'(y)+\parder{\phi}{t}\beta'(y)+\parder{\phi}{y}
\end{align}
$$
לפי לייבניץ:
$$
\parder{\phi}{y}=\int_{s}^t \parder{f}{y}(x,y)dx
$$
לפי המשפט היסודי:
$$
\parder{\phi}{t}=f(t,y) \qquad \qquad \parder{\phi}{t}=-f(s,y)
$$
לכן מתקיים:
$$
\begin{align}
F'(y)&=\int_{\alpha(y)}^{\beta(y)}\parder{f}{y}(x,y)dx+f(\beta(y),y)\beta'(y)-f(\alpha(y),y)\alpha'(y)
\end{align}
$$
> [!remark|*] למה זה רעיון ההוכחה ולא הוכחה?
> כי לא הצדקנו ש-$\phi$ היא פונקציה גזירה.
> ההצדקה שהיא גזירה יכולה לעבור דרך נגזרות חלקיות רציפות.

> [!example|*] "סופר מגניבה" - צנזור
> $$
> \int_{0}^1 \frac{\ln(1+x)}{1+x^2}dx
> $$
> "אם תרגיל כזה מופיע במבחן לא כתוב לו על המצח 'תגדיר פונקציה בשני משתנים'" - צנזור
> נגדיר $\displaystyle F(y)=\int_{0}^y \frac{\ln(1+xy)}{1+x^2}dx$ ונמצא את $F(1)$.
> [נעשה את זה אם נספיק]

## אינטגרלים נשנים
> [!definition] אינטגרל נשנה
> תהי $F(y)=\displaystyle \int_a^{b}f(x,y)dx$ מוגדרת בקטע $[c,d]$ ו[[2 - האינטגרל המסויים#^525de1|אינטגרבילית]] בו.
> האינטגרל $\displaystyle \int_{c}^d \left(\int_{a}^b f(x,y)dx\right)dy$ נקרא **אינטגרל נשנה** של $f$.

> [!theorem|*] פוביני
> תהי $f(x,y)$ רציפה במלבן $[a,b]\times[c,d]$, אזי:
> $$
> \int_{a}^b \left( \int_{c}^d f(x,y)dy \right)dx=\int_{c}^d \left( \int_{a}^b f(x,y)dx \right)dy
> $$

^dbf04d

**הוכחה:**
נגדיר $\varphi(t)= \displaystyle \int_{c}^t \left( \int_{a}^b f(x,y)dx \right)dy,\;\; \displaystyle \psi(t)=\int_{a}^b \left( \int_{c}^t f(x,y)dy \right)dx$  ונראה כי $\varphi(t)=\psi(t)$ לכל $t \in \mathbb{R}$ ובפרט $\varphi(d)=\psi(d)$.
הפונקציה $\displaystyle F(y)=\int_{a}^b f(x,y)dx$ רציפה לפי [[#^5caaf7|המשפט שלפני לייבניץ]] ולכן:
$$
\varphi'(t)=\frac{d}{dt}\int_{c}^t F(y)dy \underset{\begin{matrix}
\downarrow \\
\R{\text{המשפט היסודי}}
\end{matrix}}{=}\int_{a}^b f(x,t)dx
$$
הפונקציה  $G(x,t)=\displaystyle  \int_{c}^t f(x,y)dy$ גזירה לפי $t$ (משפט יסודי) ומתקיים:
$$
\parder{G}{t}(x,t)=f(x,t)
$$
לכן מתקיים:
$$
\psi'(t)=\frac{d}{dt} \int_{a}^b G(x,t) dx \underset{\begin{matrix}
\downarrow \\
\R{\text{לייבניץ}}
\end{matrix}}{=}\int_{a}^b \parder{G}{t}(x,t)dx=\int_{a}^b f(x,t)dx
$$
לכן מתקיים $\varphi'(t)=\psi'(t)$ ⟸ אנו יודעים כי $\varphi(t)=\psi(t)+const$ עבור $const \in \mathbb{R}$ מסויים.
נציב $t=c$ ונקבל כי:
$$
\varphi(t)=\int_{c}^c (\dots)dy=0=\int_{a}^b 0dx=\int_{a}^b \int_{c}^c (\dots)dydx=\psi(t)
$$
לכן בהכרח $const=0$ ולכן $\varphi(t)=\psi(t)$.
`\end{proof}`

> [!example|*] 
> יהיו $b>a>0$. נחשב את $\displaystyle\int_{0}^1 \frac{x^b-x^a}{\ln x}dx$. זה **לא** אינטגרל מוכלל.
> על מנת להצדיק את העובדה שהאינטגרנד חסום, נוכיח כי יש גבול מימין ומשמאל (**תרגיל**)
> נשים לב כי $\displaystyle\frac{x^b-x^a}{\ln x}=\int_{a}^b x^tdt$. נגדיר $f(x,t)=x^t$.
> $f$ רציפה במלבן $[0,1]\times[a,b]$ ולכן:
> $$
> \int_{0}^1 \frac{x^b-x^a}{\ln x}dx\!=\!\!\int_{0}^1 \left( \int_{a}^b x^tdt \right)dx \!\!\underset{\begin{matrix}
> \downarrow \\
> \R{\text{פוביני}}
> \end{matrix}}{=}\!\!\!\int_{a}^b \left( \int_{0}^1 x^tdx \right)dt \!\underset{\begin{matrix}
> \downarrow \\
> NL
> \end{matrix}}{=}\!\! \int_{a}^b \left.\frac{x^{t+1}}{t+1}\right\vert_{x=0}^{x=1}dt=\!\int_{a}^b \frac{1}{t+1} dt=\ln \frac{b+1}{a+1}
> $$

