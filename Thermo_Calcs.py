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

unknowns = ["beta2", "beta3"]

#This function calculates the residuals of the equations based on the unknowns and the targets.
#Its pupose is to be used with the fsolve function to find the beta unknown values that satisfy the targets.
def residuals(x, k):
    v = dict(zip(unknowns, x)) #Setting the unknowns to a dictionary for easier access
    tb2, tb3 = np.tan(v["beta2"]), np.tan(v["beta3"]) #Calculating the tangent of the unknown angles
    return [
        2*k["phi"] * (tb2 + tb3) - k["psi"],   #Equation 1: Stage loading coefficient
        0.5*k["phi"] * (tb2 - tb3) - k["R"] #Equation 2: Degree of Reaction
    ]



# --- Design Calculations ---

if __name__ == "__main__":
   guess = [np.radians(30), np.radians(30)]
   sol, info, ier, msg = sp.optimize.fsolve(residuals, guess, args=(targets,), full_output=True)
   if ier != 1:
       print("Solution not found:", msg)
   for name, value in zip(unknowns, sol):
        print(f"{name}: {np.degrees(value):.2f} degrees")

   
