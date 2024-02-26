from absParameter import AbsParameter
import numpy as np   # math operations
import numpy.random as npr # random
from scipy.stats import norm
import math

class Heston_Model(AbsParameter) :
    def __init__(self, S0, V0, T, r, kappa, theta, rho, eta):
        self.spot, self.spot_vol, self.maturity, self.interest_rate, self.kappa, self.theta, self.rho, self.eta = S0, V0, T, r, kappa, theta, rho, eta
        self.Spaths = None
        self.Vol_Spaths = None

    def description(self):
        return f"Heston model with  S0 ={self.spot}, V0 ={self.spot_vol}, T ={self.maturity}, r={self.interest_rate}, kappa={self.kappa}, theta={self.theta}, rho={self.rho}, eta={self.eta}"

    def simulation(self, N, M):
        S0, V0, T, r, kappa, theta, rho, eta = self.spot, self.spot_vol, self.maturity, self.interest_rate, self.kappa, self.theta, self.rho, self.eta

        # set the random seed for reproducibility
        # Same seed leads to the same set of random values
        np.random.seed(42)
        # Parameters
        # S0 : spot
        # T : Maturity
        # t : risk-free rate
        # N : time steps number
        # M MC simulation

        # calibrated parameters
        # kappa : rate of mean reversion in variance process
        # rho : correlation between asset returns and variance
        # theta : long-term mean of variance process
        # eta : volatility of variance process

        # define dt (delta t) the lenght of time interval
        dt = T / N
        # Simulating M asset price paths with N times steps
        V = np.zeros((N + 1, M))
        V[0] = V0  # or V[0,:] = V0

        S = np.zeros((N + 1, M))
        S[0] = S0
        for i in range(1, N + 1):
            Z1 = np.random.standard_normal(M)
            Z2 = np.random.standard_normal(M)
            ZV = Z1
            ZS = rho * Z1 + math.sqrt(1 - rho ** 2) * Z2
            V[i] = V[i - 1] + kappa * (theta - V[i - 1]) * dt + eta * np.sqrt(V[i - 1] * dt) * ZV
            S[i] = S[i - 1] * np.exp((r - 0.5 * V[i - 1]) * dt + np.sqrt(V[i - 1] * dt) * ZS)

        self.Spaths = S
        self.Vol_Spaths = V

    def Price_simulation(self,tag,K,N):
        r, T = self.interest_rate, self.maturity

        if tag == 'call':
            price = np.exp(- r * T) * np.mean( np.maximum(self.Spaths[-1] - K, 0))
            payoff = np.exp(- r * T) * np.maximum(self.Spaths[-1] - K, 0)
            sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
            error = 1.96 * sigma / np.sqrt(N)
            parameter = [price, sigma, error]
            return parameter
        elif tag == 'put':
            price = np.exp(- r * T) * np.mean(np.maximum(K - self.Spaths[-1], 0))
            payoff = np.exp(- r * T) * np.maximum(K - self.Spaths[-1], 0)
            sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
            error = 1.96 * sigma / np.sqrt(N)
            parameter = [price, sigma, error]
            return parameter
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")




