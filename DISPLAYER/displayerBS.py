
import matplotlib.pyplot as plt
from scipy.stats import describe
import numpy as np

class Displayer :
    def scenario(St, cp_scenario):
        plt.plot(St[: cp_scenario,:].T)
        plt.grid(True)
        plt.xlabel('Time step (t)')
        plt.ylabel('Underlying (S)')
        plt.legend("Scenario (St) On BSM")
        plt.tight_layout()
        plt.show()

    def display_price(price,tag):
        if tag == 'call' or tag == 'put' :
            print(f"Price of the {tag} by Simulation is {price[0]}")
            print("On the confidence interval [ ",price[0]-price[2]," ",price[0]+price[2]," ]")
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")

    def display_BS_price(price,tag):
        if tag == 'call' or tag == 'put' :
            print(f"Price by BS of the {tag} by Simulation is {price}")
        else:
            raise ValueError(f"You need to take an option called 'call' or 'put' ")

    def print_statistics_BS(a1):
        sta1 = describe(a1)

        print('%14s %14s ' % ('statistic BS', 'Maturity Scenario St'))
        print(45 * "-")
        print('%14s % 14.3f ' % ('size', sta1[0]))
        print('%14s % 14.3f ' % ('min', sta1[1][0]))
        print('%14s % 14.3f ' % ('max', sta1[1][1]))
        print('%14s % 14.3f ' % ('median', sta1[2]))
        print('%14s % 14.3f ' % ('std', np.sqrt(sta1[3])))
        print('%14s % 14.3f ' % ('skew', sta1[4]))
        print('%14s % 14.3f ' % ('kurtosis', sta1[5]))

