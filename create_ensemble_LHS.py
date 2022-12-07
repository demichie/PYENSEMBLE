import pandas as pd
import numpy as np
import random
from linecache import getline
import itertools
from pyDOE import *
from scipy.stats import norm


def main():

    n_param = 4
    n_samples = 20

    design = lhs(n_param, samples=n_samples)    

    list_values = []
    list_names = []
    
    i = 0
    
    # range of volumes (log-uniform distribution)
    volume_min = 1000000  # m3
    volume_max = 10000000  # m3

    volume = volume_min * ( volume_max / volume_min )**design[:, i]
    
    list_values.append(volume)
    list_names.append('Volume')
    i +=1
    
    # range of mu (uniform distribution)
    mu_min = 0.1
    mu_max = 0.3
    
    mu = mu_min + ( mu_max - mu_min ) * design[:,i]

    list_values.append(mu)
    list_names.append('mu')
    i +=1

    # range of xi (log-uniform distribution)
    xi_min = 300.0 
    xi_max = 5000.0 

    xi = xi_min * ( xi_max / xi_min )**design[:, i]
    
    list_values.append(xi)
    list_names.append('xi')
    i +=1

    # range of gamma (normal distribution)
    gamma_mean = 10.0
    gamma_std = 2.0
    
    gamma = norm(loc=gamma_mean, scale=gamma_std).ppf(design[:, i])
    list_values.append(gamma)
    list_names.append('gamma')
    i +=1


    # when the samples are generated above the dataframe is
    # created as follows
    df = pd.DataFrame(list(map(list, zip(*list_values))), columns=list_names)
    df.to_csv('samples.csv')


if __name__ == '__main__':

    main()
