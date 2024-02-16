# Description
The *Black Scholes and Heston stock prices* are being examined in this project. 
The **Black Scholes model** is based on the assumption that *volatility is constant*, 
but the **Heston model** allows *stochastic volatility*, 
which is more customizable and has better performance with empirical data. 
Analyzing and simulating both models is done.

# Black Scholes model

The *Geometric Brownian Motion Model*, given by the Stochastic Differential Equation (SDE) of the stock price :
$$dS_t = r S_t dt +S_t \sigma dW_t$$ 
where $r$ is the drift term of the Stock price and $\sigma$ the variance of the stochastic process.

# Heston Model
*Heston model* is a popular extension of the Black-Scholes model where the main assumption is not consider a constant volatility, it uses a stochastic volatility characterized by mean reversion process: 
$$dS(t) = rS(t) dt + \sqrt{V(t)} S(t) dW_1(t)$$ 
$$dV(t) = \kappa (\overline{\nu} - V(t))\,dt + \gamma\sqrt{V(t)} dW_2(t)$$
$$dW_1(t) dW_2(t) = \rho\, dt$$ for 0<t<T
with correlation $\rho$ between the Brownian Motions $W_1$ and $W_2$.

# Pricing
I value call's pricing and put's pricing using a Monte Carlo (MC) approach on both models :
Under $\mathbb{Q}$, the pay-off $P$ is as follows:

$\mathbb{E}^{\mathbb{Q}} [e^{-rT} P]$ where $P$ is :
- for a call $(S_T-K)_{+}$
- for a put $(K-S_T)_{+}$.



