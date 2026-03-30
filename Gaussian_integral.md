---
title: "Gaussian integral - Wikipedia"
source: "https://en.wikipedia.org/wiki/Gaussian_integral"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2004-04-01
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gaussian_Integral.svg/250px-Gaussian_Integral.svg.png)

A graph of the function {\\displaystyle f(x)=e^{-x^{2}}} and the area between it and the {\\displaystyle x} -axis, (i.e. the entire real line) which is equal to {\\displaystyle {\\sqrt {\\pi }}}.

The **Gaussian integral**, also known as the **Euler–Poisson integral**, is the [integral](https://en.wikipedia.org/wiki/Integral "Integral") of the [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function "Gaussian function") ${\displaystyle f(x)=e^{-x^{2}}}$ over the entire real line. Named after the German mathematician [Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss "Carl Friedrich Gauss"), the integral is 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}.}
$$

[Abraham de Moivre](https://en.wikipedia.org/wiki/Abraham_de_Moivre "Abraham de Moivre") originally discovered this type of integral in 1733, while Gauss published the precise integral in 1809,[^1] attributing its discovery to [Laplace](https://en.wikipedia.org/wiki/Laplace "Laplace"). The integral has a wide range of applications. For example, with a slight change of variables it is used to compute the [normalizing constant](https://en.wikipedia.org/wiki/Normalizing_constant "Normalizing constant") of the [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution "Normal distribution"). The same integral with finite limits is closely related to both the [error function](https://en.wikipedia.org/wiki/Error_function "Error function") and the [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function "Cumulative distribution function") of the [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution "Normal distribution"). In physics this type of integral appears frequently, for example, in [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics "Quantum mechanics"), to find the probability density of the ground state of the harmonic oscillator. This integral is also used in the path integral formulation, to find the propagator of the harmonic oscillator, and in [statistical mechanics](https://en.wikipedia.org/wiki/Statistical_mechanics "Statistical mechanics"), to find its [partition function](https://en.wikipedia.org/wiki/Partition_function_\(statistical_mechanics\) "Partition function (statistical mechanics)").

Although no [elementary function](https://en.wikipedia.org/wiki/Elementary_function "Elementary function") exists for the error function, as can be proven by the [Risch algorithm](https://en.wikipedia.org/wiki/Risch_algorithm "Risch algorithm"),[^2] the Gaussian integral can be solved [analytically](https://en.wikipedia.org/wiki/Closed-form_expression#Analytic_expression "Closed-form expression") through the methods of [multivariable calculus](https://en.wikipedia.org/wiki/Multivariable_calculus "Multivariable calculus"). That is, there is no elementary *[indefinite integral](https://en.wikipedia.org/wiki/Indefinite_integral "Indefinite integral")* for 
$$
{\displaystyle \int e^{-x^{2}}\,dx,}
$$
 but the [definite integral](https://en.wikipedia.org/wiki/Definite_integral "Definite integral") 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx}
$$
 can be evaluated. The definite integral of an arbitrary [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function "Gaussian function") is 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-a(x+b)^{2}}\,dx={\sqrt {\frac {\pi }{a}}}.}
$$

## Computation

### By polar coordinates

A standard way to compute the Gaussian integral, the idea of which goes back to Poisson,[^3] is to make use of the property that:

$$
{\displaystyle \left(\int _{-\infty }^{\infty }e^{-x^{2}}\,dx\right)^{2}=\int _{-\infty }^{\infty }e^{-x^{2}}\,dx\int _{-\infty }^{\infty }e^{-y^{2}}\,dy=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }e^{-\left(x^{2}+y^{2}\right)}\,dx\,dy.}
$$

Consider the function ${\displaystyle e^{-\left(x^{2}+y^{2}\right)}=e^{-r^{2}}}$ on the plane ${\displaystyle \mathbb {R} ^{2}}$, and compute its integral two ways:

1. on the one hand, by [double integration](https://en.wikipedia.org/wiki/Double_integration "Double integration") in the [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system "Cartesian coordinate system"), its integral is a square: 
	$$
	{\displaystyle \left(\int e^{-x^{2}}\,dx\right)^{2};}
	$$
2. on the other hand, by [shell integration](https://en.wikipedia.org/wiki/Shell_integration "Shell integration") (a case of double integration in [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinates "Polar coordinates")), its integral is computed to be ${\displaystyle \pi }$

Comparing these two computations yields the integral, though one should take care about the [improper integrals](https://en.wikipedia.org/wiki/Improper_integral "Improper integral") involved.

$$
{\displaystyle {\begin{aligned}\iint _{\mathbb {R} ^{2}}e^{-\left(x^{2}+y^{2}\right)}dx\,dy&=\int _{0}^{2\pi }\int _{0}^{\infty }e^{-r^{2}}r\,dr\,d\theta \\[6pt]&=2\pi \int _{0}^{\infty }re^{-r^{2}}\,dr\\[6pt]&=2\pi \int _{-\infty }^{0}{\tfrac {1}{2}}e^{s}\,ds&&s=-r^{2}\\[6pt]&=\pi \int _{-\infty }^{0}e^{s}\,ds\\[6pt]&=\pi \,\left[e^{s}\right]_{-\infty }^{0}\\[6pt]&=\pi \,\left(e^{0}-e^{-\infty }\right)\\[6pt]&=\pi \,\left(1-0\right)\\[6pt]&=\pi ,\end{aligned}}}
$$
 where the factor of r is the [Jacobian determinant](https://en.wikipedia.org/wiki/Jacobian_determinant "Jacobian determinant") which appears because of the [transform to polar coordinates](https://en.wikipedia.org/wiki/List_of_canonical_coordinate_transformations "List of canonical coordinate transformations") (*r* *dr* *dθ* is the standard measure on the plane, expressed in polar coordinates [Wikibooks:Calculus/Polar Integration#Generalization](https://en.wikibooks.org/wiki/Calculus/Polar_Integration#Generalization "wikibooks:Calculus/Polar Integration")), and the substitution involves taking *s* = − *r* <sup>2</sup>, so *ds* = −2 *r* *dr*.

Combining these yields 
$$
{\displaystyle \left(\int _{-\infty }^{\infty }e^{-x^{2}}\,dx\right)^{2}=\pi ,}
$$
 so 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}.}
$$

#### Complete proof

To justify the improper double integrals and equating the two expressions, we begin with an approximating function: 
$$
{\displaystyle I(a)=\int _{-a}^{a}e^{-x^{2}}dx.}
$$

If the integral 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx}
$$
 were [absolutely convergent](https://en.wikipedia.org/wiki/Absolutely_convergent "Absolutely convergent") we would have that its [Cauchy principal value](https://en.wikipedia.org/wiki/Cauchy_principal_value "Cauchy principal value"), that is, the limit 
$$
{\displaystyle \lim _{a\to \infty }I(a)}
$$
 would coincide with 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx.}
$$
 To see that this is the case, consider that

$$
{\displaystyle \int _{-\infty }^{\infty }\left|e^{-x^{2}}\right|dx<\int _{-\infty }^{-1}-xe^{-x^{2}}\,dx+\int _{-1}^{1}e^{-x^{2}}\,dx+\int _{1}^{\infty }xe^{-x^{2}}\,dx<\infty .}
$$

So we can compute 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx}
$$
 by just taking the limit 
$$
{\displaystyle \lim _{a\to \infty }I(a).}
$$

Taking the square of ${\displaystyle I(a)}$ yields

$$
{\displaystyle {\begin{aligned}I(a)^{2}&=\left(\int _{-a}^{a}e^{-x^{2}}\,dx\right)\left(\int _{-a}^{a}e^{-y^{2}}\,dy\right)\\[6pt]&=\int _{-a}^{a}\left(\int _{-a}^{a}e^{-y^{2}}\,dy\right)\,e^{-x^{2}}\,dx\\[6pt]&=\int _{-a}^{a}\int _{-a}^{a}e^{-\left(x^{2}+y^{2}\right)}\,dy\,dx.\end{aligned}}}
$$

Using [Fubini's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem "Fubini's theorem"), the above double integral can be seen as an area integral 
$$
{\displaystyle \iint _{[-a,a]\times [-a,a]}e^{-\left(x^{2}+y^{2}\right)}\,d(x,y),}
$$
 taken over a square with vertices {(− *a*, *a*), (*a*, *a*), (*a*, − *a*), (− *a*, − *a*)} on the *xy* - [plane](https://en.wikipedia.org/wiki/Cartesian_plane "Cartesian plane").

Since the exponential function is greater than 0 for all real numbers, it then follows that the integral taken over the square's [incircle](https://en.wikipedia.org/wiki/Incircle "Incircle") must be less than ${\displaystyle I(a)^{2}}$, and similarly the integral taken over the square's [circumcircle](https://en.wikipedia.org/wiki/Circumcircle "Circumcircle") must be greater than ${\displaystyle I(a)^{2}}$. The integrals over the two disks can easily be computed by switching from Cartesian coordinates to [polar coordinates](https://en.wikipedia.org/wiki/List_of_canonical_coordinate_transformations "List of canonical coordinate transformations"):

$$
{\displaystyle {\begin{aligned}x&=r\cos \theta ,&y&=r\sin \theta \end{aligned}}}
$$
 
$$
{\displaystyle \mathbf {J} (r,\theta )={\begin{bmatrix}{\dfrac {\partial x}{\partial r}}&{\dfrac {\partial x}{\partial \theta }}\\[1em]{\dfrac {\partial y}{\partial r}}&{\dfrac {\partial y}{\partial \theta }}\end{bmatrix}}={\begin{bmatrix}\cos \theta &-r\sin \theta \\\sin \theta &{\hphantom {-}}r\cos \theta \end{bmatrix}}}
$$
 
$$
{\displaystyle d(x,y)=\left|J(r,\theta )\right|d(r,\theta )=r\,d(r,\theta ).}
$$
 
$$
{\displaystyle \int _{0}^{2\pi }\int _{0}^{a}re^{-r^{2}}\,dr\,d\theta <I^{2}(a)<\int _{0}^{2\pi }\int _{0}^{a{\sqrt {2}}}re^{-r^{2}}\,dr\,d\theta .}
$$

(See [to polar coordinates from Cartesian coordinates](https://en.wikipedia.org/wiki/List_of_canonical_coordinate_transformations "List of canonical coordinate transformations") for help with polar transformation.)

Integrating, 
$$
{\displaystyle \pi \left(1-e^{-a^{2}}\right)<I^{2}(a)<\pi \left(1-e^{-2a^{2}}\right).}
$$

By the [squeeze theorem](https://en.wikipedia.org/wiki/Squeeze_theorem "Squeeze theorem"), this gives the Gaussian integral 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}.}
$$

### By Cartesian coordinates

A different technique, which goes back to Laplace (1812),[^3] is the following. Let 
$$
{\displaystyle {\begin{aligned}y&=xs\\dy&=x\,ds.\end{aligned}}}
$$

Since the limits on s as *y* → ±∞ depend on the sign of x, it simplifies the calculation to use the fact that *e* <sup>− <i>x</i> <sup>2</sup></sup> is an [even function](https://en.wikipedia.org/wiki/Even_function "Even function"), and, therefore, the integral over all real numbers is just twice the integral from zero to infinity. That is,

$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}\,dx=2\int _{0}^{\infty }e^{-x^{2}}\,dx.}
$$

Thus, over the range of integration, *x* ≥ 0, and the variables y and s have the same limits. This yields: 
$$
{\displaystyle {\begin{aligned}I^{2}&=4\int _{0}^{\infty }\int _{0}^{\infty }e^{-\left(x^{2}+y^{2}\right)}dy\,dx\\[6pt]&=4\int _{0}^{\infty }\left(\int _{0}^{\infty }e^{-\left(x^{2}+y^{2}\right)}\,dy\right)\,dx\\[6pt]&=4\int _{0}^{\infty }\left(\int _{0}^{\infty }e^{-x^{2}\left(1+s^{2}\right)}x\,ds\right)\,dx\\[6pt]\end{aligned}}}
$$
 Then, using [Fubini's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem "Fubini's theorem") to switch the [order of integration](https://en.wikipedia.org/wiki/Order_of_integration_\(calculus\) "Order of integration (calculus)"): 
$$
{\displaystyle {\begin{aligned}I^{2}&=4\int _{0}^{\infty }\left(\int _{0}^{\infty }e^{-x^{2}\left(1+s^{2}\right)}x\,dx\right)\,ds\\[6pt]&=4\int _{0}^{\infty }\left[{\frac {e^{-x^{2}\left(1+s^{2}\right)}}{-2\left(1+s^{2}\right)}}\right]_{x=0}^{x=\infty }\,ds\\[6pt]&=4\left({\frac {1}{2}}\int _{0}^{\infty }{\frac {ds}{1+s^{2}}}\right)\\[6pt]&=2\arctan(s){\Big |}_{0}^{\infty }\\[6pt]&=\pi .\end{aligned}}}
$$

Therefore, ${\displaystyle I={\sqrt {\pi }}}$, as expected.

### By Laplace's method

In the [Laplace approximation](https://en.wikipedia.org/wiki/Laplace%27s_method "Laplace's method"), we deal only with up to second-order terms in [Taylor expansion](https://en.wikipedia.org/wiki/Taylor_series "Taylor series"), so we consider ${\displaystyle e^{-x^{2}}\approx 1-x^{2}\approx (1+x^{2})^{-1}}$.

In fact, since ${\displaystyle (1+t)e^{-t}\leq 1}$ for all ${\displaystyle t}$, we have the exact bounds:
$$
{\displaystyle 1-x^{2}\leq e^{-x^{2}}\leq (1+x^{2})^{-1}}
$$
 Then we can do the bound at Laplace approximation limit:
$$
{\displaystyle \int _{[-1,1]}(1-x^{2})^{n}dx\leq \int _{[-1,1]}e^{-nx^{2}}dx\leq \int _{[-1,1]}(1+x^{2})^{-n}dx}
$$

That is, 
$$
{\displaystyle 2{\sqrt {n}}\int _{[0,1]}(1-x^{2})^{n}dx\leq \int _{[-{\sqrt {n}},{\sqrt {n}}]}e^{-x^{2}}dx\leq 2{\sqrt {n}}\int _{[0,1]}(1+x^{2})^{-n}dx}
$$

By trigonometric substitution, we exactly compute those two bounds: ${\displaystyle 2{\sqrt {n}}(2n)!!/(2n+1)!!}$ and ${\displaystyle 2{\sqrt {n}}(\pi /2)(2n-3)!!/(2n-2)!!}$

By taking the square root of the [Wallis formula](https://en.wikipedia.org/wiki/Wallis_formula "Wallis formula"), 
$$
{\displaystyle {\frac {\pi }{2}}=\prod _{n=1}{\frac {(2n)^{2}}{(2n-1)(2n+1)}}}
$$
 we have ${\displaystyle {\sqrt {\pi }}=2\lim _{n\to \infty }{\sqrt {n}}{\frac {(2n)!!}{(2n+1)!!}}}$, the desired lower bound limit. Similarly we can get the desired upper bound limit. Conversely, if we first compute the integral with one of the other methods above, we would obtain a proof of the Wallis formula.

### Proof by complex integral

Several proofs have been discovered using [Cauchy's integral formula](https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula "Cauchy's integral formula"), despite the integral being initially thought to be ill-suited to the [residue calculus](https://en.wikipedia.org/wiki/Residue_calculus "Residue calculus").[^3] [^4]

## Relation to the gamma function

The integrand is an [even function](https://en.wikipedia.org/wiki/Even_function "Even function"),

$$
{\displaystyle \int _{-\infty }^{\infty }e^{-x^{2}}dx=2\int _{0}^{\infty }e^{-x^{2}}dx}
$$

Thus, after the change of variable ${\textstyle x={\sqrt {t}}}$, this turns into the Euler integral

$$
{\displaystyle 2\int _{0}^{\infty }e^{-x^{2}}dx=2\int _{0}^{\infty }{\frac {1}{2}}\ e^{-t}\ t^{-{\frac {1}{2}}}dt=\Gamma {\left({\frac {1}{2}}\right)}={\sqrt {\pi }}}
$$

where ${\textstyle \Gamma (z)=\int _{0}^{\infty }t^{z-1}e^{-t}dt}$ is the [gamma function](https://en.wikipedia.org/wiki/Gamma_function "Gamma function"). More generally, 
$$
{\displaystyle \int _{0}^{\infty }x^{n}e^{-ax^{b}}dx={\frac {\Gamma {\left((n+1)/b\right)}}{ba^{(n+1)/b}}},}
$$
 which can be obtained by substituting ${\displaystyle t=ax^{b}}$ in the integrand of the gamma function to get ${\textstyle \Gamma (z)=a^{z}b\int _{0}^{\infty }x^{bz-1}e^{-ax^{b}}dx}$.

## Generalizations

### The integral of a Gaussian function

The integral of an arbitrary [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function "Gaussian function") is 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-a(x+b)^{2}}\,dx={\sqrt {\frac {\pi }{a}}}.}
$$

An alternative form is 
$$
{\displaystyle \int _{-\infty }^{\infty }e^{-(ax^{2}-bx+c)}\,dx={\sqrt {\frac {\pi }{a}}}\,e^{{\frac {b^{2}}{4a}}-c}.}
$$

This form is useful for calculating expectations of some continuous probability distributions related to the normal distribution, such as the [log-normal distribution](https://en.wikipedia.org/wiki/Log-normal_distribution "Log-normal distribution"), for example.

### Complex form

$$
{\displaystyle \int _{-\infty }^{\infty }e^{{\frac {1}{2}}it^{2}}dt=e^{i\pi /4}{\sqrt {2\pi }}}
$$
 and more generally,
$$
{\displaystyle \int _{\mathbb {R} ^{N}}e^{{\frac {1}{2}}i\mathbf {x} ^{T}A\mathbf {x} }dx=\det(A)^{-{\frac {1}{2}}}{\left(e^{i\pi /4}{\sqrt {2\pi }}\right)}^{N}}
$$
 for any positive-definite symmetric matrix ${\displaystyle A}$.

### n-dimensional and functional generalization

Suppose *A* is a symmetric positive-definite (hence invertible) *n* × *n* [precision matrix](https://en.wikipedia.org/wiki/Precision_matrix "Precision matrix"), which is the matrix inverse of the [covariance matrix](https://en.wikipedia.org/wiki/Covariance_matrix "Covariance matrix"). Then,

$$
{\displaystyle {\begin{aligned}\int _{\mathbb {R} ^{n}}\exp {\left(-{\frac {1}{2}}\mathbf {x} ^{\mathsf {T}}A\mathbf {x} \right)}\,d^{n}\mathbf {x} &=\int _{\mathbb {R} ^{n}}\exp {\left(-{\frac {1}{2}}\sum \limits _{i,j=1}^{n}A_{ij}x_{i}x_{j}\right)}\,d^{n}\mathbf {x} \\[1ex]&={\sqrt {\frac {{\left(2\pi \right)}^{n}}{\det A}}}={\sqrt {\frac {1}{\det \left(A/2\pi \right)}}}\\[1ex]&={\sqrt {\det \left(2\pi A^{-1}\right)}}\end{aligned}}}
$$

By completing the square, this generalizes to 
$$
{\displaystyle \int _{\mathbb {R} ^{n}}\exp {\left(-{\tfrac {1}{2}}\mathbf {x} ^{\mathsf {T}}A\mathbf {x} +\mathbf {b} ^{\mathsf {T}}\mathbf {x} +c\right)}\,d^{n}\mathbf {x} ={\sqrt {\det \left(2\pi A^{-1}\right)}}\exp \left({\tfrac {1}{2}}\mathbf {b} ^{\mathsf {T}}A^{-1}\mathbf {b} +c\right)}
$$

This fact is applied in the study of the [multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution "Multivariate normal distribution").

Also, 
$$
{\displaystyle \int x_{k_{1}}\cdots x_{k_{2N}}\,\exp {\left(-{\frac {1}{2}}\sum \limits _{i,j=1}^{n}A_{ij}x_{i}x_{j}\right)}\,d^{n}x={\sqrt {\frac {(2\pi )^{n}}{\det A}}}\,{\frac {1}{2^{N}N!}}\,\sum _{\sigma \in S_{2N}}(A^{-1})_{k_{\sigma (1)}k_{\sigma (2)}}\cdots (A^{-1})_{k_{\sigma (2N-1)}k_{\sigma (2N)}}}
$$
 where *σ* is a [permutation](https://en.wikipedia.org/wiki/Permutation "Permutation") of {1, …, 2 *N* } and the extra factor on the right-hand side is the sum over all combinatorial pairings of {1, …, 2 *N* } of *N* copies of *A* <sup>−1</sup>.

Alternatively,[^5]

$$
{\displaystyle \int f(\mathbf {x} )\exp {\left(-{\frac {1}{2}}\sum _{i,j=1}^{n}A_{ij}x_{i}x_{j}\right)}d^{n}\mathbf {x} ={\sqrt {\frac {{\left(2\pi \right)}^{n}}{\det A}}}\,\left.\exp \left({\frac {1}{2}}\sum _{i,j=1}^{n}\left(A^{-1}\right)_{ij}{\partial  \over \partial x_{i}}{\partial  \over \partial x_{j}}\right)f(\mathbf {x} )\right|_{\mathbf {x} =0}}
$$

for some [analytic function](https://en.wikipedia.org/wiki/Analytic_function "Analytic function") *f*, provided it satisfies some appropriate bounds on its growth and some other technical criteria. (It works for some functions and fails for others. Polynomials are fine.) The exponential over a differential operator is understood as a [power series](https://en.wikipedia.org/wiki/Power_series "Power series").

While [functional integrals](https://en.wikipedia.org/wiki/Functional_integral "Functional integral") have no rigorous definition (or even a nonrigorous computational one in most cases), we can *define* a Gaussian functional integral in analogy to the finite-dimensional case. There is still the problem, though, that ${\displaystyle (2\pi )^{\infty }}$ is infinite and also, the [functional determinant](https://en.wikipedia.org/wiki/Functional_determinant "Functional determinant") would also be infinite in general. This can be taken care of if we only consider ratios:

$$
{\displaystyle {\begin{aligned}&{\frac {\displaystyle \int f(x_{1})\cdots f(x_{2N})\exp \left[{-\iint {\frac {1}{2}}A(x_{2N+1},x_{2N+2})f(x_{2N+1})f(x_{2N+2})\,d^{d}x_{2N+1}\,d^{d}x_{2N+2}}\right]{\mathcal {D}}f}{\displaystyle \int \exp \left[{-\iint {\frac {1}{2}}A(x_{2N+1},x_{2N+2})f(x_{2N+1})f(x_{2N+2})\,d^{d}x_{2N+1}\,d^{d}x_{2N+2}}\right]{\mathcal {D}}f}}\\[6pt]={}&{\frac {1}{2^{N}N!}}\sum _{\sigma \in S_{2N}}A^{-1}(x_{\sigma (1)},x_{\sigma (2)})\cdots A^{-1}(x_{\sigma (2N-1)},x_{\sigma (2N)}).\end{aligned}}}
$$

In the [DeWitt notation](https://en.wikipedia.org/wiki/DeWitt_notation "DeWitt notation"), the equation looks identical to the finite-dimensional case.

### n-dimensional with linear term

If *A* is again a symmetric positive-definite matrix, then (assuming all are column vectors) 
$$
{\displaystyle {\begin{aligned}\int \exp \left(-{\frac {1}{2}}\sum _{i,j=1}^{n}A_{ij}x_{i}x_{j}+\sum _{i=1}^{n}b_{i}x_{i}\right)d^{n}\mathbf {x} &=\int \exp \left(-{\tfrac {1}{2}}\mathbf {x} ^{\mathsf {T}}A\mathbf {x} +\mathbf {b} ^{\mathsf {T}}\mathbf {x} \right)d^{n}\mathbf {x} \\&={\sqrt {\frac {(2\pi )^{n}}{\det A}}}\exp \left({\tfrac {1}{2}}\mathbf {b} ^{\mathsf {T}}A^{-1}\mathbf {b} \right).\end{aligned}}}
$$

$$
{\displaystyle \int _{0}^{\infty }x^{2n}e^{-{x^{2}}/{a^{2}}}\,dx={\sqrt {\pi }}{\frac {a^{2n+1}(2n-1)!!}{2^{n+1}}}}
$$
 
$$
{\displaystyle \int _{0}^{\infty }x^{2n+1}e^{-{x^{2}}/{a^{2}}}\,dx={\frac {n!}{2}}a^{2n+2}}
$$
 
$$
{\displaystyle \int _{0}^{\infty }x^{2n}e^{-bx^{2}}\,dx={\frac {(2n-1)!!}{b^{n}2^{n+1}}}{\sqrt {\frac {\pi }{b}}}}
$$
 
$$
{\displaystyle \int _{0}^{\infty }x^{2n+1}e^{-bx^{2}}\,dx={\frac {n!}{2b^{n+1}}}}
$$
 
$$
{\displaystyle \int _{0}^{\infty }x^{n}e^{-bx^{2}}\,dx={\frac {\Gamma ({\frac {n+1}{2}})}{2b^{\frac {n+1}{2}}}}}
$$
 where ${\displaystyle n}$ is a positive integer

An easy way to derive these is by [differentiating under the integral sign](https://en.wikipedia.org/wiki/Leibniz_integral_rule#Evaluating_definite_integrals "Leibniz integral rule").

$$
{\displaystyle {\begin{aligned}\int _{-\infty }^{\infty }x^{2n}e^{-\alpha x^{2}}\,dx&=\left(-1\right)^{n}\int _{-\infty }^{\infty }{\frac {\partial ^{n}}{\partial \alpha ^{n}}}e^{-\alpha x^{2}}\,dx\\[1ex]&=\left(-1\right)^{n}{\frac {\partial ^{n}}{\partial \alpha ^{n}}}\int _{-\infty }^{\infty }e^{-\alpha x^{2}}\,dx\\[1ex]&={\sqrt {\pi }}\left(-1\right)^{n}{\frac {\partial ^{n}}{\partial \alpha ^{n}}}\alpha ^{-{\frac {1}{2}}}\\[1ex]&={\sqrt {\frac {\pi }{\alpha }}}{\frac {(2n-1)!!}{\left(2\alpha \right)^{n}}}\end{aligned}}}
$$

One could also integrate by parts and find a [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation "Recurrence relation") to solve this.

### Higher-order polynomials

Applying a linear change of basis shows that the integral of the exponential of a homogeneous polynomial in *n* variables may depend only on [SL(*n*)](https://en.wikipedia.org/wiki/SL\(n\) "SL(n)") -invariants of the polynomial. One such invariant is the [discriminant](https://en.wikipedia.org/wiki/Discriminant "Discriminant"), zeros of which mark the singularities of the integral. However, the integral may also depend on other invariants.[^6]

Exponentials of other even polynomials can numerically be solved using series. These may be interpreted as [formal calculations](https://en.wikipedia.org/wiki/Formal_calculation "Formal calculation") when there is no convergence. For example, the solution to the integral of the exponential of a quartic polynomial is

$$
{\displaystyle \int _{-\infty }^{\infty }e^{ax^{4}+bx^{3}+cx^{2}+dx+f}\,dx={\frac {1}{2}}e^{f}\sum _{\begin{smallmatrix}n,m,p=0\\n+p=0{\bmod {2}}\end{smallmatrix}}^{\infty }{\frac {b^{n}}{n!}}{\frac {c^{m}}{m!}}{\frac {d^{p}}{p!}}{\frac {\Gamma {\left({\frac {3n+2m+p+1}{4}}\right)}}{{\left(-a\right)}^{\frac {3n+2m+p+1}{4}}}}.}
$$

The *n* + *p* = 0 mod 2 requirement is because the integral from −∞ to 0 contributes a factor of (−1) <sup><i>n</i> + <i>p</i></sup> /2 to each term, while the integral from 0 to +∞ contributes a factor of 1/2 to each term. These integrals turn up in subjects such as [quantum field theory](https://en.wikipedia.org/wiki/Quantum_field_theory "Quantum field theory").

## See also

- [List of integrals of Gaussian functions](https://en.wikipedia.org/wiki/List_of_integrals_of_Gaussian_functions "List of integrals of Gaussian functions")
- [Common integrals in quantum field theory](https://en.wikipedia.org/wiki/Common_integrals_in_quantum_field_theory "Common integrals in quantum field theory")
- [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution "Normal distribution")
- [List of integrals of exponential functions](https://en.wikipedia.org/wiki/List_of_integrals_of_exponential_functions "List of integrals of exponential functions")
- [Error function](https://en.wikipedia.org/wiki/Error_function "Error function")
- [Berezin integral](https://en.wikipedia.org/wiki/Berezin_integral "Berezin integral")

## References

### Citations

### Sources

- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein") ["Gaussian Integral"](https://mathworld.wolfram.com/GaussianIntegral.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld "MathWorld")*.
- Griffiths, David. *Introduction to Quantum Mechanics* (2nd ed.).
- Abramowitz, M.; Stegun, I. A. *Handbook of Mathematical Functions*. New York: Dover Publications.

[^1]: Stahl, Saul (April 2006). ["The Evolution of the Normal Distribution"](https://web.archive.org/web/20160125095729/https://www.maa.org/sites/default/files/pdf/upload_library/22/Allendoerfer/stahl96.pdf) (PDF). *MAA.org*. Archived from [the original](https://www.maa.org/sites/default/files/pdf/upload_library/22/Allendoerfer/stahl96.pdf) (PDF) on January 25, 2016. Retrieved May 25, 2018.

[^2]: Cherry, G. W. (1985). ["Integration in Finite Terms with Special Functions: the Error Function"](https://doi.org/10.1016%2FS0747-7171%2885%2980037-7). *Journal of Symbolic Computation*. **1** (3): 283–302. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S0747-7171(85)80037-7](https://doi.org/10.1016%2FS0747-7171%2885%2980037-7).

[^3]: Lee, Peter M. ["The Probability Integral"](https://www.york.ac.uk/depts/maths/histstat/normal_history.pdf) (PDF).

[^4]: Remmert, Reinhold (1998). *Theory of Complex Functions* (2nd English ed.). New York: Springer-Verlag. p. 414. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-97195-5](https://en.wikipedia.org/wiki/Special:BookSources/0-387-97195-5 "Special:BookSources/0-387-97195-5").

[^5]: ["Reference for Multidimensional Gaussian Integral"](https://math.stackexchange.com/q/126227). *[Stack Exchange](https://en.wikipedia.org/wiki/Stack_Exchange "Stack Exchange")*. March 30, 2012.

[^6]: Morozov, A.; Shakirove, Sh. (2009). "Introduction to integral discriminants". *Journal of High Energy Physics*. **2009** (12): 002. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[0903.2595](https://arxiv.org/abs/0903.2595). [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2009JHEP...12..002M](https://ui.adsabs.harvard.edu/abs/2009JHEP...12..002M). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1088/1126-6708/2009/12/002](https://doi.org/10.1088%2F1126-6708%2F2009%2F12%2F002).