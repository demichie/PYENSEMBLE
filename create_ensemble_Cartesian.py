import pandas as pd
from scipy.stats import norm
import numpy as np
import random
from linecache import getline
import itertools

##########################################

def main():

     
    ### Cartesian Product
    list_names = []
    
    list_vel = [0.0, 30.0, 60.0, 90.0]
    list_names.append('Velocity')
    
    list_volume = [1.0e5 , 5.0e5 , 1.0e6]
    list_names.append('Volume')

    list_mu = [0.1 , 0.2 , 0.3]
    list_names.append('mu')

    
    list_prod = list(itertools.product(list_vel, list_volume,list_mu))
    list_prod = [list(elem) for elem in list_prod]
    
    # when the samples are generated with the Cartesian Product
    # the dataframe is generated as follows
    df = pd.DataFrame(list_prod, columns=list_names)
    
    ###

    df.to_csv('samples.csv')


if __name__ == '__main__':

    main()
