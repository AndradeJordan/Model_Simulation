from absParameter import AbsParameter
import numpy as np   # math operations
import numpy.random as npr # random
from scipy.stats import norm
import math
class BS_Model(AbsParameter) :
    def __init__(self, r, s0, sigma, T, K):
        self.interest_rate, self.spot, self.sigma, self.maturity, self.strike = r, s0, sigma, T, K
        self.Spaths = None

    def description(self):
        return f"Black sholes model with r={self.interest_rate}, S0 ={self.spot}, sigma={self.sigma}, T ={self.maturity}, K ={self.strike}"

    def simulation(self, n, N):
        r, s0, sigma, T, K = self.interest_rate, self.spot, self.sigma, self.maturity, self.strike

        delta = float(T / n)
        G = npr.normal(0, 1, size=(N, n))
        # Log returns
        LR = (r - 0.5 * sigma ** 2) * delta + np.sqrt(delta) * sigma * G
        # concatenate with log(S0)
        LR = np.concatenate((np.log(s0) * np.ones((N, 1)), LR), axis=1)
        # cumsum horizontally (axis=1)
        LR = np.cumsum(LR, axis=1)
        # take the expo Spath matrix
        spaths = np.exp(LR)
        self.Spaths = spaths

    def Price_simulation(self,tag,N):
        St, r, s0, sigma, T, K = self.Spaths, self.interest_rate, self.spot, self.sigma, self.maturity, self.strike

        if tag == 'call':
            price = np.exp(-r*T) * np.maximum(St-K,0)[:-1].mean()
            payoff = np.exp(-r*T) * np.maximum(St-K,0)[:-1]
            sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
            error = 1.96 * sigma / np.sqrt(N)
            parameter = [price, sigma, error]
            return parameter
        elif tag == 'put':
            price = np.exp(-r*T) * np.maximum(K-St,0)[:-1].mean()
            payoff = np.exp(-r * T) * np.maximum(K - St, 0)[:-1]
            sigma = np.std(payoff)  # standard deviation estimator  (ecart type de monte_carlo)
            error = 1.96 * sigma / np.sqrt(N)
            parameter = [price, sigma, error]
            return parameter
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")

    def Price_by_BS(self, tag):
        St, r, s0, sigma, T, K = self.Spaths, self.interest_rate, self.spot, self.sigma, self.maturity, self.strike
        d1 = (math.log(s0/K) + (r - 0.5 * sigma ** 2)*T) / (sigma*math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        N = norm.cdf
        if tag == 'call':
            return np.exp(-r*T) * (s0*N(d1) - K * np.exp(-r * T) * N(d2))
        elif tag == 'put':
            return np.exp(-r*T) * (-s0*N(-d1) + K*np.exp(-r * T) * N(-d2))
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")


