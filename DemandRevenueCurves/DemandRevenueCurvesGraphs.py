import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Define the demand curve function
def demand_curve(q):
    return 24 - (3/10)*q # modify this with your function

# Create arrays for quantities and prices, modify this with your values
Vet_q = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
Vet_p = np.empty_like(Vet_q)

# Calculate prices for all quantities
Vet_p = np.vectorize(demand_curve)(Vet_q)

# Calculate revenue
Vet_r = Vet_p * Vet_q

# Create a DataFrame
df = pd.DataFrame({'Quantities (q)': Vet_q, 'Prices (p)': Vet_p, 'Revenues (R)': Vet_r})

# Create the demand curve graph
plt.plot(Vet_q, Vet_p, linestyle='--', color='red', marker='o')  # Stile o e linea tratteggiata
plt.xlabel('Quantity (q)')  # Etichetta asse x
plt.ylabel('Price (p)')  # Etichetta asse y
plt.title('Demand Curve')
plt.grid(True)

# Save the demand curve graph to a file
plt.savefig('demand_curve.png')

# Create the revenue graph
plt.figure()  # Create a new figure
plt.plot(Vet_q, Vet_r, linestyle='--', color='green', marker='o')  # Stile o e linea tratteggiata
plt.xlabel('Quantity (q)')  # Etichetta asse x
plt.ylabel('Revenue (R)')  # Etichetta asse y
plt.title('Revenue curve')
plt.grid(True)

# Save the revenue graph to a file
plt.savefig('revenue_curve.png')

# Create an Excel file
wb = Workbook()
ws = wb.active

# Add the DataFrame to the Excel file
ws.append(['Quantities (q)', 'Prices (p)', 'Revenues (R)'])  # header row
for row in df.values:
    ws.append(row.tolist())  # Convert NumPy array to list

# Add the demand curve graph to the Excel file
img = Image('demand_curve.png')
ws.add_image(img, 'A3')  # adjust the position as needed

# Add the revenue graph to the Excel file
img = Image('revenue_curve.png')
ws.add_image(img, 'A20')  # adjust the position as needed

# Save the Excel file
wb.save('demand_and_revenue_curves.xlsx')