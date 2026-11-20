import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#This file is to calculate the thermodynanic requirements of the engine



def T0( Ta, ca, cpa):
    """Calculates the temperature at a given speed of aircraft"""
    return Ta + (ca)^2/2*cpa

def P0( Pa, ca, Ta, gamma, cpa, eta_N):
    """Calculates the pressure at a given speed of aircraft"""
    return Pa*(1 + (eta_N)*(ca**2)/(2*cpa*Ta))**(gamma/(gamma-1))

if __name__ == "__main__":
   
