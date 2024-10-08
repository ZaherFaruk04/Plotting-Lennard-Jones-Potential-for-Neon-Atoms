import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data_and_potential(file_path, sigma, epsilon):
    
    data = pd.read_csv(file_path, sep=' ', header=None, names=['r', 'V']) #This Reads the Data
    
    plt.scatter(data['r'], data['V'], label='Van der Waals Data') #Makes scatter points (single dots)
    
    r_values = np.linspace(min(data['r']), max(data['r']), 500) #Spaces out X Axis Data
    
    lj_values = 4 * epsilon * ((sigma / r_values) ** 12 - (sigma / r_values) ** 6) # Calculate Y Axis Values
    
    plt.plot(r_values, lj_values, label='Lennard-Jones Potential', color='red') # Makes line graph
    
    plt.xlabel('Atomic Separation (Å)')
    
    plt.ylabel('Potential Energy (eV)')
    
    plt.title('Interatomic Potential for Neon')
    
    plt.legend()
    
    plt.show()
    
sigma = 2.687  
epsilon = 8.56e-3  
plot_data_and_potential('vdW_Ne.dat', sigma, epsilon) #Calls the function