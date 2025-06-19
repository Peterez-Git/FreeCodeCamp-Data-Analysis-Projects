import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from the file
    df = pd.read_csv('epa-sea-level.csv')

    # Plot a Scatter plot of CSRO Adjusted Sea Level accross all years
    plt.figure(figsize=(12, 6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], alpha=0.8)
    plt.xlabel('Year', fontsize=12, fontweight='bold')
    plt.ylabel('CSIRO Adjusted Sea Level', fontsize=12, fontweight='bold')
    plt.title('CSRO Adjusted Sea Level accross the years', fontsize=12, fontweight='bold', family='serif')

    # Compute the linear regression and make the forecast
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = np.arange(1880, 2051)
    y_pred1 = res1.intercept + res1.slope * x_pred1

    # Plot the regression line
    plt.figure(figsize=(10, 6))
    plt.plot(x_pred1, y_pred1, color='r')
    plt.xlabel('Year', fontweight='bold', fontsize=12, labelpad=5)
    plt.ylabel('Sea Level', fontweight='bold', fontsize=12, labelpad=5)
    plt.title('CSIRO Adjusted Sea Level prediction from 1880 - 2050', fontweight='bold', fontsize=14,
              family='Comic Sans MS')
    plt.tight_layout()

    # Filter the data for the next forecast
    df_recent = df[df['Year'] >= 2000]

    # Calculate the Linear Regression for the filtered data
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res2.intercept + res2.slope * x_pred2

    # Plot the Regression Line
    plt.figure(figsize=(10, 6))
    plt.plot(x_pred2, y_pred2, color='g')

    # Add labels and title
    plt.xlabel('Year', fontweight='bold', fontsize=12)
    plt.ylabel('Sea Level (inches)', fontweight='bold', fontsize=12)
    plt.title('Rise in Sea Level', fontweight='bold', fontsize=14, family='Comic Sans MS')
    plt.tight_layout()



    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()