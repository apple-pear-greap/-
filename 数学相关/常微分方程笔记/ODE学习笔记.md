# 初等积分法
## 恰当方程
考虑对称形式的一阶微分方程
		 $P(x,y)dx+Q(x,y)dy=0$
若存在一个可微函数$\Phi(x,y)$，使得其全微分恰为：
$d\Phi(x,y)=P(x,y)dx+Q(x,y)dy$

## 一阶线性ODE
形如以下形式的ODE称之为一阶线性ODE:
$a(x)y'(x)+b(x)y(x)=c(x)$
事实上$a(x)$不恒为0
从而可以将上述方程化为：
$y'(x)+p(x)y(x)=q(x)$

### 求解方法：
#### 积分因子法（注意力法）
我们注意到$\frac{d}{dx}\left( e^{ \int p(x)  \, dx }y(x) \right)=p(x)e^{ \int p(x) \,dx } y(x)+e^{ \int p(x)\,dx }y'(x)=e^{ \int p(x)dx }q(x)$
从而我们有$e^{ \int p(x)\,dx }y(x)=\int e^{ \int p(x)dx }q(x)dx$
这便求得了$y(x)$

例子：
1. $xy'-y=x^3$
$$
\begin{gather}
我们将上式化为y'-\frac{1}{x}y=x^2 \\
计算e^{ \int -\frac{1}{x}dx }=e^{ -\ln |x| +C}=\frac{A}{x} \\
套用上述公式，我们便得到 \\
\frac{A}{x}y(x)=\int \frac{A}{x}x^2dx=\frac{A}{2}x^2+C \\
从而得到y(x)=\frac{x^3}{2}+Cx
\end{gather}
$$
2. $y'-\sin \frac{x}{1+\cos x}y= \frac{2x}{1+\cos x}$
$$
事实上我们注意到[(1+\cos x)y]'=(1+\cos x)y'-\sin x \,y=2x
故y = \frac{x^2+C}{1+\cos x}
$$

#### 常数变易法（可用于求解高阶线性ODE)
我们先来求解对应的齐次方程$y'+py=0$
事实上由分离变量易得$\frac{dy}{y}=-p(x)dx$
由此得到$y(x)=Ae^{ -\int p(x)dx }$
现在我们假设$A并非常数，而是一个与x相关的函数A(x)$
代入方程得到：$A'(x)e^{ -\int p(x)dx }=q(x)$
$分离变量直接积分便可求得A(x)$

#### 综合例题
$y'+y=x^2$
$$
\begin{gather}
注意到原式可化为 \frac{d}{dx}(e^{ x }y)=e^{ x }x^2 \\
从而我们有y(x)=e^{ -x }\int e^{ x }x^2dx=e^{ -x }(e^{ x }x^2-2xe^{ x }+2e^{ x }+C)=x^2 -2x +2 + Ce^{ -x } \\
若考虑常数变易法，我们容易求得对应齐次方程的解为y(x)=Ce^{ -x } \\
令C变易为C(x),代入得到C'(x)e^{ -x }=x^2 \\
同样解得C(x)=e^{ x }x^2-2xe^{ x }+2e^{ x }+C \\
即y(x) = x^2 -2x +2 + Ce^{ -x }
\end{gather}
$$
$$
\begin{gather}
考虑非齐次方程 \,y'+py=q \dots(1) \\
与齐次方程\,y'+py=0\dots(2)
\end{gather}
$$
性质1：方程(2)的解要么恒为0,要么恒不为0
性质2：（1）和（2）的解都是整体存在的（即在方程的定义域内都存在）注：方程的定义域由p,q决定
性质3：方程（2）的解关于加法和数乘可以构成一个线性空间
		若$y_{1}为(1)的解，y_{2}为(2)的解，则y_{1}+cy_{2}为(1)的解$
		$y_{1},y_{2}为(1)的解，则它们的差为(2)的解$
性质4：(1)的特解+(2)的通解=(1)的通解
性质5：$y'+py=q 与y(x_{0})=y_{0}形成的方程组的解存在且唯一$

## 积分因子法
我们都知道若方程：$P(x,y)dx+Q(x,y)dy=0$是恰当方程时的解法
而对于可分类变量的方程以及一阶线性方程时的解法（实际上是转化成了恰当方程）
现在思考，对于一般的方程$P(x,y)dx+Q(x,y)dy=0$，是否存在一个$\mu(x,y)$
使得$\mu(x,y)P(x,y)dx+\mu(x,y)Q(x,y)dy=0$是一个恰当方程
考虑恰当方程的充要条件，我们有：
	$\frac{ \partial (\mu P) }{ \partial y }=\frac{ \partial (\mu Q) }{ \partial x }$
	即$P \frac{ \partial \mu }{ \partial y }-Q\frac{ \partial \mu }{ \partial x }=\left( \frac{ \partial Q }{ \partial x }-\frac{ \partial P }{ \partial y } \right)\mu$
然而这个偏微分方程不是很好解（事实上这个偏微分方程的求解要用到上面的常微分方程）
	我们不妨考虑简单的情况，假设$\mu(x,y)=\phi(x)$(即$\mu$只与$x$相关)
	这样我们便有：
	$Q \frac{d\phi}{dx}=\left( \frac{ \partial P }{ \partial y } -\frac{ \partial Q }{ \partial x } \right)\phi$
	即$\frac{1}{\phi} \frac{d\phi}{dx}= \frac{1}{Q}\left( \frac{ \partial P }{ \partial y } -\frac{ \partial Q }{ \partial x }\right)$
	由于左端只与x有关，故右端也只与$x$有关,记为$G(x)$
	解出$\phi(x)=e^{ \int G(x)dx },此为所求积分因子$


# 常系数线性微分方程组
形式：$\vec{y}'(x)=A \vec{y}(x)+\vec{f}(x)$
其中$x \in \mathbf{R},\,A \in M^{n*n}(\mathbf{R}),\vec{y}:I\to \mathbf{R^{n}},\vec{f}:I \to \mathbf{\mathrm{R^{n}}}$
现在我们来探索这个微分方程组的解
当$n=1时，方程组化为： \frac{dy}{dx}=ay,其解为y = Ce^{ ax },那么当n>1时，结果又如何呢?$
