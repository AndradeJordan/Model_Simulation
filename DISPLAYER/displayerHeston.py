
import matplotlib.pyplot as plt
from scipy.stats import describe
import numpy as np

class Displayer :


    def scenario_heston(St, Vt, cp_scenario):
        plt.figure(figsize=(8, 3))

        plt.subplot(1, 2, 1)
        plt.plot(St[:, :cp_scenario])
        plt.grid(True)
        plt.xlabel("Times Steps")
        plt.ylabel("Stock Price (S)")

        plt.subplot(1, 2, 2)
        plt.plot(Vt[:, :cp_scenario])
        plt.grid(True)
        plt.xlabel("Times Steps")
        plt.ylabel("Variance (V)")

        plt.suptitle('PLot of simulated stock price and volatility paths')
        plt.tight_layout()
        plt.show()

    def display_price(price,tag):
        if tag == 'call' or tag == 'put' :
            print(f"Price of the {tag} by Simulation is {price[0]}")
            print("On the confidence interval [ ",price[0]-price[2]," ",price[0]+price[2]," ]")
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")


    def print_statistics_Heston(a1, a2):
        '''
        Print selected statistics.
        parameters
        =======
        a1, a2 : ndarray objects generated from simulation
        '''
        sta1 = describe(a1)
        sta2 = describe(a2)
        print('%14s %14s %14s' % ('statistic Heston at Maturity', 'Maturity Scenario St', 'Maturity Scenario Vt'))
        print(45 * "-")
        print('%14s % 14.3f %14.3f' % ('size', sta1[0], sta2[0]))
        print('%14s % 14.3f %14.3f' % ('min', sta1[1][0], sta2[1][0]))
        print('%14s % 14.3f %14.3f' % ('max', sta1[1][1], sta2[1][1]))
        print('%14s % 14.3f %14.3f' % ('median', sta1[2], sta2[2]))
        print('%14s % 14.3f %14.3f' % ('std', np.sqrt(sta1[3]), np.sqrt(sta2[3])))
        print('%14s % 14.3f %14.3f' % ('skew', sta1[4], sta2[4]))
        print('%14s % 14.3f %14.3f' % ('kurtosis', sta1[5], sta2[5]))