---
cssclasses:
  - center-h1
  - center-images
---
בניגוד לרוב הדברים שעשינו בשני משתנים, שקורסים להיות זהים למשתנה יחיד כשמורידים משתנה, באינטגרל מוכלל יהיה רעיון עקרוני שונה אשר נביט בו כעת.
_למה זה קרה ככה?_ בגלל היסטוריה. יכלו להגדיר אינטגרל מוכלל יחיד כמו שמגדירים בכמה משתנים, אך לא עשו זאת.
## פונקציות אי שליליות
> [!definition] אינטגרל כפול מוכלל עבור פונקציה אי שלילית
> תהי $f:\mathbb{R}^n\to \mathbb{R}$ אי שלילית בתחום פתוח $D \subseteq \mathbb{R}^n$.
> נניח כי $f$ אינטגרבילית בכל תת קבוצה [[5 - העולם הרב מימדי#^2c3b21|קומפקטית]] ו[[7 - אינטגרל כפול#^c0a6c2|בעלת שטח]] $K \subset D$.
> נגדיר:
> $$
> \int_{D} f(\underline{x})d\underline{x}=\underset{K \subset D}{\sup}\int_{K}f(\underline{x})d\underline{x}
> $$
> בתנאי שאגף ימין סופי.

- אם אגף ימין סופי נגיד שהאינטגרל המוכלל **מתכנס**.
- אם אגף ימין לא סופי נגיד שהאינטגרל המוכלל **לא מתכנס**.

איך נדמיין פונקציה שעבורה האינטגרל המוכלל מתכנס?(_אינטואיציה_) נניח פונקציה עם מקסימום בראשית אשר בכל כיוון היא כמו $e^{-x}$ שכזו.
**נשים :LiHeart:** כי ההגדרה שראינו מטפלת בכל המקרים של אינטגרל מוכלל - לא דרשנו רציפות בכל התחום או שהתחום יהיה קומפקטי.

> [!theorem|*] 
> תהי $D \subseteq \mathbb{R}^n$ פתוחה ותהי $f:D\to \mathbb{R}$ אי שלילית ואינטגרבילית בכל תת קבוצה קומפקטית ובעלת שטח $K \subset D$.
> תהי $K_{n}$ סדרה של קבוצות קומפקטיות ובעלות שטח המוכלות ב-$D$ ומקיימות:
> 1. $K_{n}$ סדרה עולה. כלומר, $K_{n}\subset int(K_{n+1})$ (כאשר $int$ מסמל $interior$ - הפנים של הקבוצה)
> 2. $K_{n}$ היא כיסוי של $D$. כלומר, $\displaystyle D= \bigcup_{n=1}^\infty K_{n}$
> 
> אזי, $\displaystyle \int _D f(\underline{x})d\underline{x}$ מתכנס $\displaystyle \lim_{ n \to \infty } \int_{K_{n}}f(\underline{x})d\underline{x}\iff$ קיים וסופי. במקרה זה:
> $$
> \int_{D}f(\underline{x})d\underline{x}=\lim_{ n \to \infty } \int_{K_{n}}f(\underline{x})d\underline{x}
> $$

> [!remark|*] 
> ההגדרה הינה די עקבית בכל מקום שתסתכלו.
> המשפט הזה שונה בין מקום למקום, אפילו בין הוידאיו לעכשיו. החישובים יוצאים כמעט זהים אך הנימוקים הינם שונים.

> [!remark|*] 
> הסמסטר הזה לא נוכיח את המשפט הזה, ההוכחה של המשפט הזה ספציפית אצל רון רוזנטל.
> "את ההוכחה לא נעשה הסמסטר, נגמר לי הזמן - אבל מי שאחראי לזה מת. קוראים לו חמינאי האב" - צנזור

> [!example|*] "כולם מבינים למה אני מלטף פה כבשה מפוטמת?" - אביב צנזור
> $$
> \iint_{\mathbb{R}^2} e^{-x^2-y^2}dxdy
> $$
> נשים לב כי הפונקציה הזו אינטגרבילית בכל קבוצה קומפקטית ולכן התנאי ההכרחי מתקיים.
> אנו נקח סדרה $K_{n}$ של מעגלים ברדיוס $n$ לכל $n \in \mathbb{N}$ סביב הראשית.
> $$
> \iint_{K_{n}} e^{-x^2-y^2}dxdy \underset{\begin{matrix}
> \downarrow \\
> \R{\text{חישוב שכבר}} \\
> \R{\text{עשינו}}
> \end{matrix}}{=}\pi(1-e^{-n^2}) \rarrowlim{n\to \infty} \pi
> $$
> לכן, לפי משפט האינטגרל הנ"ל מתכנס ומתקיים $\displaystyle \iint_{\mathbb{R}^2}e^{-x^2-y^2}dxdy$.

> [!example|*] פונקציה לא חסומה על $\partial D$
> מה שאתם אמורים לדמיין זה אגרטל אינסופי שכזה.
> $$
> \iint_{x^2+y^2<1} \frac{1}{\sqrt{ 1-x^2-y^2 }}dxdy
> $$
> נשים לב כי מקובל לרשום מתחת לנחשים מהו $D$ ולא רק $D$ ואז להגדירו. (מקובל גם לצייר את $D$ למען בהירות - פחות מקובל כי זה פחות מדוייק)
> **חובה כמובן לעבור על כל תנאי המשפט לפני שמשתמשים בו!**
> - הפונקציה אי שלילית - כן, בזכות השורש.
> - בכל קבוצה קומפקטית בעלת שטח $K \subset D$ הפונקציה אינטגרבילית - כן!
>
> נבחר את $K_{n}$ כמעגלים בעלי רדיוס השואף להיות $1$ משמאל. (נשים לב כי הסדרה שבחרנו מקיימת את כל התנאים)
> $$
> \iint_{K_{n}=\left\{ \begin{array}{c|c}
> (x,y) & x^2+y^2\leq 1-\frac{1}{n}
> \end{array} \right\}} \frac{1}{\sqrt{ 1-x^2-y^2 }} \underset{\begin{matrix}
> \downarrow \\
> \R{\text{פולריות}} \\
> \R{\text{+ פוביני}}
> \end{matrix}}{=} \int_{0}^{2\pi}\left( \int_{0}^{1-\frac{1}{n}} \frac{r}{\sqrt{ 1-r^2 }}dr \right)d\theta=
> $$
> נשים לב כי באינטגרל הפנימי אין $\theta$ ולכן ניתן להוציא את כולו החוצה ולקבל:
> $$
> =2\pi \int_{0}^{1-\frac{1}{n}} \frac{r}{\sqrt{ 1-r^2 }}dr \underset{\begin{matrix}
> \downarrow \\
> \R{\text{מיידי}}
> \end{matrix}}{=}\left.2\pi \left( -1 \right)\sqrt{ 1-r^2 }\right\vert_{r=0}^{r=1-\frac{1}{n}}=-2\pi\left( \sqrt{ 1-\left( 1-\frac{1}{n} \right)^2 }-1 \right) \rarrowlim{n\to \infty} 2\pi
> $$
> > [!corollary|*] 
> > $$
> > \iint_{x^2+y^2<1} \frac{1}{\sqrt{ 1-x^2-y^2 }}dxdy=2\pi
> > $$

> [!example|*] 
> $$
> \iint_{0<x^2+y^2<1} \frac{1}{(x^2+y^2)^\alpha} dxdy
> $$
> מה הבעיה עכשיו? איך נראית הפונקציה הזו? איפה יש לה בעיה? בראשית! אם $\alpha>0$ אז כש-$x^2+y^2 \rarrowlim{}0$ אז המכנה שואף ל-$0$ ו-$\frac{1}{}$ שואף ל-$\infty$.
> כעת האי-חסימות היא בנקודה בודדת שהיא בכלל נקודה פנימית של התחום.
> 
> נבחר את $K_{n}$ כסדרה של טבעות עם רדיוס פנימי של $\frac{1}{n}$ ורדיוס חיצוני של $1$. לכל $2\leq n \in \mathbb{N}$. בכל איטרציה החור יותר קטן ולכן $K_{n}$ עולה במצב זה שכן כל טבעת מוכלת בהבאה.
> **יש בעיה:** הטבעות הללו מכילות יותר מאשר את $D$ שכן ב-$D$ אין את השפה ולכן נדרש שהרדיוס החיצוני יהיה $1-\frac{1}{n}$.
> עכשיו הכל אחלה! - ויייייייייי
> $$
> K_{n}=\left\{ \begin{array}{c|c}
> (x,y) & \displaystyle\frac{1}{n^2}\leq x^2+y^2\leq \left( 1-\frac{1}{n} \right)^2
> \end{array} \right\}
> $$
> כעת נוכל לבצע את האינטגרל:
> $$
> \begin{align}
> \iint_{K_{n}} \frac{1}{(x^2+y^2)^\alpha}dxdy &\!\!\!\!\!\!\!\!\!\underset{\begin{matrix}
> \downarrow \\
> \R{\text{פולאריות + פוביני}}
> \end{matrix}}{=}\!\!\!\!\!\!\!\!\!\!\!\!\int_{0}^{2\pi}\left( \int_{\frac{1}{n}}^{1-\frac{1}n} \frac{r}{r^{2\alpha}}dr \right)d\theta=2\pi \int_{\frac{1}{n}}^{1-\frac{1}{n}} \frac{1}{r^{2\alpha-1}}dr \\
> &\!\!\!\!\!\!\!\!\!\!\!=\begin{cases}
> \alpha=1, & \displaystyle 2\pi \int_{\frac{1}{n}}^{1-\frac{1}{n}} \frac{1}{r}dr=2\pi \left( \ln\left( {1-\frac{1}{n}}\right)-\ln\left({\frac{1}{n}} \right) \right) \rarrowlim{n\to \infty} -\infty \R{\text{לא קיים - }} \\
> \alpha\neq 1, & \displaystyle \left.2\pi  \frac{1}{2-2\alpha} \frac{1}{r^{2\alpha-2}} \right\vert_{r=\frac{1}{n}}^{r=1-\frac{1}{n}}=\frac{\pi}{1-\alpha}\left( \frac{1}{\left( 1-\frac{1}{n} \right)^{2\alpha-1}}-n^{2\alpha-1} \right) \\
> & \quad \quad \quad \qquad \qquad \displaystyle  \lim_{ n \to \infty } [\cdots]= \begin{cases}
> \alpha>1, & \R{\text{לא קיים גבול}} \\
> \alpha<1, & \frac{\pi}{1-\alpha}
> \end{cases}
> \end{cases}
> \end{align}
> $$
	
> [!remark|*] 
> [[3 - אינטגרל מוכלל#^106572|מהלא"ש]] תקף :) (_נסחו והוכיחו_)

> [!definition] אינטגרל כפול מוכלל עבור פונקציה אי שלילית ותחום אחר
> תהי $D$ פתוחה ותהי $0\leq f$ ומקיימת כי $f$ אינטגרבילית בכל תת קבוצה קומפקטית ובעלת שטח $K \subset D$.
> תהי $E$ קבוצה שנבדלת מ-$D$ בקבוצה בעלת שטח $0$.
> נגדיר: 
> $$
> \displaystyle \iint_{E}f=\iint_{D}f
> $$
> בנתאי ש-$\displaystyle \iint_{D}f$ קיים.

> [!example|*] 
> נסתכל על תחום שהוא הרצועה האינסופית כך ש-$x \in(-\infty,\infty)$ ו-$y \in(0,1)$. אזי $D=\left\{ \begin{array}{c|c}(x,y)& \begin{matrix}-\infty<x<\infty \\  0\leq y\leq 1\end{matrix}\end{array} \right\}$.
> נגדיר $K_{n}=[-n,n]\times [0,1]$.
> _הערה:_ אם רוצים לעשות את זה פתוח אז צריך לקחת מ-$\frac{1}{n}$ עד $1-\frac{1}{n}$.
> $$
> \iint_{K_{n}} \sin x\,dxdy=\int_{0}^1 \left( \int_{-n}^n \sin x\,dx \right)dy=-\int_{0}^1 \left.\cos x\right\vert_{x=-n}^{x=n}dy=-\cos n+\cos(-n)=0 \rarrowlim{n\to \infty}0
> $$
> **יש פה באג ← הפונקציה $\sin x$ לא אי שלילית!!!** לראיה, בואו נקח $\tilde{K}_{n}=\left[ -2n\pi,2n\pi+\frac{\pi}{2} \right]\times[0,1]$ ואז:
> $$
> \cdots=-\cos\left( 2n\pi+\frac{\pi}{2} \right)+\cos(-2n\pi)=1 \rarrowlim{n\to \infty}1
> $$
> **שימוש שגוי מופרך והזוי!**

## פונקציות כלליות
> [!definition] אינטגרל כפול מוכלל כללי
> תהי $f:\mathbb{R}^n\to \mathbb{R}$ מוגדרת בתחום $D \subseteq \mathbb{R}^n$ פתוח.
> נסמן $f^+(\underline{x})=\max\left\{ f(\underline{x}),0 \right\}$ ו-$f^-(\underline{x})=\max\left\{ -f(\underline{x}),0 \right\}$ ונגדיר:
> $$
> \int_{D}f(\underline{x})d\underline{x}=\int_{D}f^+(\underline{x})d\underline{x}-\int_{D}f^-(\underline{x})d\underline{x}
> $$
> בתנאי ששני האינטגרלים באף ימין מתכנסים.

> [!remark|*] 
> $$
> f(\underline{x})=f^+(\underline{x})-f^-(\underline{x})
> $$
> $$
> \left| f(\underline{x}) \right|=f^++f^-
> $$

> [!corollary|*] 
> אם $\displaystyle\int_{D}f(\underline{x})d\underline{x}$ מתכנס אזי $\displaystyle \int_{D}\left|f(\underline{x})\right|d\underline{x}$ מתכנס ומתקיים:
> $$
> \int_{D}|f(\underline{x})|d\underline{x}=\int_{D}f^+(\underline{x})d\underline{x}+\int_{D}f^-(\underline{x})d\underline{x}
> $$
> כלומר, אין דבר כזה התכנסות בתנאי.

