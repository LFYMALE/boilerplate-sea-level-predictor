import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all the data)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create second line of best fit (using data from 2000 onwards)
    data_from_2000 = data[data['Year'] >= 2000]  # Correct range for data from 2000 onwards
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_from_2000['Year'],
                                                                                      data_from_2000[
                                                                                          'CSIRO Adjusted Sea Level'])

    # Create the lines of best fit for both datasets
    years_extended = range(1880, 2051)  # This will cover the full range for the first line
    sea_levels_fit = [slope * year + intercept for year in years_extended]  # First line of fit

    # For the second line of best fit, limit the years to 2000 - 2050
    years_from_2000 = range(2000, 2051)  # Only years from 2000 to 2050 for the second line
    sea_levels_fit_2000 = [slope_2000 * year + intercept_2000 for year in years_from_2000]  # Second line of fit

    # Plot the lines of best fit
    plt.plot(years_extended, sea_levels_fit, label='Best fit line (1880 - 2000)', color='red')
    plt.plot(years_from_2000, sea_levels_fit_2000, label='Best fit line (2000 - 2050)', color='blue')

    # Add labels and title
    plt.xlabel('Year')  # x label should be "Year"
    plt.ylabel('Sea Level (inches)')  # y label should be "Sea Level (inches)"
    plt.title('Rise in Sea Level')  # title should be "Rise in Sea Level"

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

