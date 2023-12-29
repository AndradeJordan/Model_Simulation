from BS_MODEL import BSmodel
from DISPLAYER import displayerBS, displayerHeston
from HESTON_MODEL import HESTONmodel

def main():
    r, S0, sig, T, K,  N, n= 0.05,100,0.2,1,95,1000,252
    model_bs = BSmodel.BS_Model(r, S0, sig, T, K)
    model_bs.simulation(n,N)
    displayerBS.Displayer.scenario(model_bs.Spaths,100)
    tag = "call"
    p = model_bs.Price_simulation(tag,N)
    displayerBS.Displayer.display_price(p,tag)
    p = model_bs.Price_by_BS(tag)
    displayerBS.Displayer.display_BS_price(p, tag)

    print("Heston Model")
    #Heston
    #S0, V0 = 100, 0.25 ** 2  # spot and variance
    V0 = sig
    #T, r = 1, 0.05
    kappa, theta, eta, rho = 3, 0.30 ** 2, 0.2, 0.5

    #N, M = 252, 1000
    model_heston = HESTONmodel.Heston_Model(S0, V0, T, r, kappa, theta, rho, eta)
    model_heston.simulation(n, N)
    displayerHeston.Displayer.scenario_heston(model_heston.Spaths,model_heston.Vol_Spaths, 100)
    tag = "call"
    p = model_heston.Price_simulation(tag,K, N)
    displayerHeston.Displayer.display_price(p, tag)


    #display statistic Heston and BSM
    displayerBS.Displayer.print_statistics_BS(model_bs.Spaths[-1])
    displayerHeston.Displayer.print_statistics_Heston(model_heston.Spaths[-1], model_heston.Vol_Spaths[-1])



if __name__ == '__main__':
    main()

