import numpy as np

# Note: Bus prices were taken from the following source:
# Roland Berger. (2015). Fuel Cell Electric Buses – Potential for Sustainable Public Transport in Europe. 
# [Pdf]. Available at: https://www.fch.europa.eu/sites/default/files/150909_FINAL_Bus_Study_Report_OUT_0.PDF. 
# [Accessed October 31st 2020]

# Extrapolation date:
date = 2040
# Order of line of best fit:
order = 1

# Diesel buses:
time_diesel = np.array([2020,2025,2030])
price_diesel = np.array([233000,238000,244000])               # Prices in euros

# Hybrid buses:
time_hybrid = np.array([2020,2025,2030])
price_hybrid = np.array([299000,299000,300000])               # Prices in euros

# Extrapolating diesel and hybrid bus prices to 2040:
# Fitting lines of best fit (y = mx +c):
m_diesel, c_diesel = np.polyfit(time_diesel,price_diesel,order)
m_hybrid, c_hybrid = np.polyfit(time_hybrid,price_hybrid,order)
# Extrapolating to 2040:
price_2040_diesel = m_diesel*date + c_diesel
price_2040_hybrid = m_hybrid*date + c_hybrid

print('Diesel bus price in 2040 =', price_2040_diesel,'euros')
print('Hybrid bus price in 2040 =', price_2040_hybrid,'euros')

