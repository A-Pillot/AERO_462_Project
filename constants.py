import numpy as np

#This file contains the contants used in the Thermo_Calcs.py file

#Constants given from the problem statement
given_variables = {
    "m": 20,  # kg/s
    "eta_T": 0.9,  # turbine efficiency
    "TiT": 1100,  # K
    "TiP": 600,  # kPa
    "ToT": None,  # K (to be calculated)
    "r": 250,  # rev/s
    "r_rad" : 250 * 2 * np.pi,  # rad/s
    "u": 340  # m/s
}


#Universal constants
universal_constants = {
    "R": 0.287,  # kJ/kgK
    "cp": 1148,  # J/kgK
    "gamma": 1.33,  # ratio of specific heats
}
