import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from constants import given_variables, universal_constants
from targets import targets

# --- This file is to calculate the performance of the turbine ---


# --- Reusable Functions ---    
def T0( Ta, c, cp):
    """Calculates the total temperature at a given inlet speed"""
    return Ta + (c)**2/2*cp

def P0( Pa, ca, Ta, gamma, cpa, eta_T):
    """Calculates total pressure at a given inlet speed"""
    return Pa*(1 + (eta_T)*(ca**2)/(2*cpa*Ta))**(gamma/(gamma-1))

# --- Angle Calculations ---



# - Beta -

unknowns_beta = ["beta2", "beta3"]

def residuals_beta(x, k):
    """
    This function calculates the residuals of the equations based on the unknowns and the targets. Its pupose is to be used with the fsolve function to find the beta unknown values that satisfy the targets.

    """
    v = dict(zip(unknowns_beta, x)) #Setting the unknowns to a dictionary for easier access
    tb2, tb3 = np.tan(v["beta2"]), np.tan(v["beta3"]) #Calculating the tangent of the unknown angles
    return [
        2*k["phi"] * (tb2 + tb3) - k["psi"],   #Equation 1: Stage loading coefficient
        0.5*k["phi"] * (tb3 - tb2) - k["R"] #Equation 2: Degree of Reaction
    ]

# - Alpha -

unknowns_alpha = ["alpha2", "alpha3"]

def residuals_alpha(x, k):
    """
    This function calculates the residuals of the equations based on the unknowns and the targets. Its pupose is to be used with the fsolve function to find the alpha unknown values that satisfy the targets.

    """
    v = dict(zip(unknowns_alpha, x)) #Setting the unknowns to a dictionary for easier access
    ta2, ta3 = np.tan(v["alpha2"]), np.tan(v["alpha3"]) #Calculating the tangent of the unknown angles
    return [
        2*k["phi"] * (ta2 + ta3) - k["psi"],   #Equation 1: Stage loading coefficient
        1 + 0.5*k["phi"] * (ta3 - ta2) - k["R"] #Equation 2: Degree of Reaction
    ]

# --- Design Calculations ---

if __name__ == "__main__":
   #This part calculates the beta angles 
   #Writing the initial guess for the unknowns and solving the system of equations using fsolve
   guess = [np.radians(30), np.radians(30)]
   #This function basically solves the system of equations defined in the residuals function and returns the unknowns that satisfy the targets.
   sol, info, ier, msg = sp.optimize.fsolve(residuals_beta, guess, args=(targets,), full_output=True)
   if ier != 1:
       print("Solution not found:", msg)
   for name, value in zip(unknowns_beta, sol):
        print(f"{name}: {np.degrees(value):.2f} degrees")

    #Same thing for the alpha angles
   guess = [np.radians(30), np.radians(30)]
   sol, info, ier, msg = sp.optimize.fsolve(residuals_alpha, guess, args=(targets,), full_output=True)
   if ier != 1:
         print("Solution not found:", msg)
   for name, value in zip(unknowns_alpha, sol):
        print(f"{name}: {np.degrees(value):.2f} degrees")


