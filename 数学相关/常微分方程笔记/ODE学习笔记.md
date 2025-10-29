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
其中$x \in \mathbf{R},\,A \in M^{n \times n}(\mathbf{R}),\vec{y}:I\to \mathbf{R^{n}},\vec{f}:I \to \mathbf{\mathrm{R^{n}}}$
现在我们来探索这个微分方程组的解
当$n=1时，方程组化为： \frac{dy}{dx}=ay,其解为y = Ce^{ ax },那么当n>1时，结果又如何呢?$
我们引入记号$e^{ \mathbf{A} }$,并希望$\mathbf{y'}=\mathbf{A}\mathbf{y}$的解恰好为$\mathbf{y}=Ce^{ x\mathbf{A} }$

所以，什么是$e^{ \mathbf{A} }$？
### 矩阵指数函数的定义和性质
参照$e^{ x }$的定义，我们想到可以使用级数$\sum ^{\infty}_{k=0} \frac{\mathbf{A}^{k}}{k!}来定义$
其中，$\mathbf{A}^{0}=\mathbf{I}$
我们先来检验一下该定义是否为良好的
这里使用$||\mathbf{A}||$来表示矩阵$\mathbf{A}$的无穷范数
首先根据矩阵范数的性质，我们会有$||\mathbf{A}\mathbf{B}||\leq||\mathbf{A}||\cdot||\mathbf{B}||$
即$||\mathbf{A}^{k}||\leq||\mathbf{A}||^{k}$
再根据三角不等式，我们有：
$||e^{ \mathbf{A} }||=||\sum ^{\infty}_{k=0} \frac{\mathbf{A}^{k}}{k!}||\leq\sum ^{\infty}_{k=0} \frac{||\mathbf{A}||^{k}}{k!}\leq e^{ \mathbf{||A||} }<\infty$
这表明该定义是良好的
由于要计算微分方程，我们还希望函数$\Phi(x)=e^{ x\mathbf{A} }具有良好的微分性质$
由于函数$\Phi(x)事实上是个幂级数矩阵，而每一项又绝对收敛，故它也是一致收敛的$
从而我们可以交换无穷求和和求导的顺序，得到：
$\Phi'(x)=\mathbf{A}\Phi(x)$
另一方面，参考$e^{ x }$的一些性质的证明，我们可以得到：
- $e^{ \mathbf{A}+\mathbf{B} }=e^{ \mathbf{A} }e^{ \mathbf{B} },若\mathbf{A}和\mathbf{B}可交换$
- $(e^{ \mathbf{A} })^{-1}=e^{ -\mathbf{A} }$
- $e^{ \mathbf{PAP^{-1}} }=\mathbf{P}e^{ \mathbf{A} }\mathbf{P}^{-1}$
最后一个与$e^{ x }$性质无关，而是使用了矩阵的快速幂算法（$即(\mathbf{PAP^{-1}})^{n}=\mathbf{PA^{n}P^{-1}}$)

### 计算矩阵指数函数
不难证明：
若$\mathbf{A}=diag\{a_{1},a_{2},\dots a_{n}\},那么e^{ \mathbf{A} }=diag\{e^{ a_{1} },e^{ a_{2} },\dots e^{ a_{n} }\}$
根据前面的性质：$若\mathbf{A}可对角化，则e^{ \mathbf{A} }也是容易计算的$

一个例子： 
$$
\begin{matrix}
已知\mathbf{A}=\begin{pmatrix}0 & \beta \\
-\beta & 0
\end{pmatrix},求解e^{ x\mathbf{A} }: \\
事实上x\mathbf{A}=\begin{pmatrix}
1 & 1 \\
i & -i
\end{pmatrix}\begin{pmatrix}
i\beta x & 0\\
0 & -i\beta x
\end{pmatrix}\begin{pmatrix}
\frac{1}{2} & - \frac{i}{2} \\
\frac{1}{2} &  \frac{i}{2}
\end{pmatrix} \\
从而e^{ x\mathbf{A} }=\begin{pmatrix}
1 & 1 \\
i & -i
\end{pmatrix}\begin{pmatrix}
e^{ i\beta x } & 0\\
0 & e^{ -i\beta x }
\end{pmatrix}\begin{pmatrix}
\frac{1}{2} & - \frac{i}{2} \\
\frac{1}{2} &  \frac{i}{2}
\end{pmatrix} =\begin{pmatrix}
\cos\beta x & \sin\beta x \\
-\sin\beta x & \cos\beta x
\end{pmatrix}\\考虑常系数微分方程组：\begin{pmatrix}
y_{1}'(x) \\
y_{2}'(x)
\end{pmatrix}=\mathbf{A}\begin{pmatrix}
y_{1}(x) \\
y_{2}(x)
\end{pmatrix} \\
其解恰好为\begin{pmatrix}
y_{1}(x) \\
y_{2}(x)
\end{pmatrix}=e^{ xA }\begin{pmatrix}
C_{1} \\
C_{2}
\end{pmatrix}(事实上这个方程等价于两个二阶常系数线性微分方程) 
\end{matrix}


$$

若$\mathbf{A}不能对角化，由高等代数知识，我们知道\mathbf{A}$在复数域内必定能化为若尔当标准型 

即$\mathbf{A}=diag\{J(\lambda_{1},k_{1}),J(\lambda_{2},k_{2}),\dots J(\lambda_{i},k_{i})\}$

其中 
$$J(\lambda,k)=\begin{pmatrix}\lambda & 1 &  &  \\
  & \lambda & \ddots & \, \\
  &   &  \ddots & 1 \\
  &  &  & \lambda

\end{pmatrix}=diag\{\lambda,\lambda,\dots\lambda\}+J(0,k)
$$
而根据若尔当矩阵的性质，我们有:$J(0,k)^{k-1}=\mathbf{0}$
这表明$diag\{J(0,k_{1}),J(0,k_{2}),\dots J(0,k_{i})\}是个幂零矩阵$
即$e^{ x\mathbf{A} }=e^{ x(\mathbf{P(D+Z)P^{-1}}) }=\mathbf{P}e^{ x\mathbf{D} }e^{ \mathbf{Z} }\mathbf{P}^{-1}$
其中$\mathbf{D}是对角阵，而\mathbf{Z}是幂零矩阵，它们的指数函数都较为容易计算$

特别的，假如$A$的代数重数等于几何重数，即$A$有着n个线性无关的特征向量$\xi_{1},\xi_{2},\dots \xi_{n}$
那我们便有:$$
e^{ x\mathbf{A} }\mathbf{P} = \begin{pmatrix}
\xi_{1},\xi_{2},\dots,\xi_{n}
\end{pmatrix}\begin{pmatrix}
e^{ \lambda_{1} } &  &  &  &  \\
 & e^{ \lambda_{2} } &  &  \\
 &  & \ddots &  \\
 &  &  & e^{ \lambda _{n}} 
\end{pmatrix}
$$
事实上这便是我们所要求得基解矩阵
假定有复特征值，根据虚根成对原理，它的共轭一定也是特征值，这样我们就能用欧拉公式将其改写为实基解矩阵事实上是取了复向量$\xi_{1}e^{ \lambda_{1} }$的实部和虚部
[^1]:关于若尔当标准型的存在和求解，可以使用$\lambda$矩阵的初等因子来证明和计算 
