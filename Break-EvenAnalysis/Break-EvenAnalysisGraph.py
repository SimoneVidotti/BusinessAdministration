import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# modify the values with your values
Vet_q = np.array([0, 1, 2, 3, 4, 5, 6])
Vet_R = np.array([0, 15, 30, 45, 60, 75, 90])
Vet_C = np.array([30, 30, 32, 35, 43, 58, 128])

Vet_Rm = np.diff(Vet_R)
Vet_Cm = np.diff(Vet_C)
Vet_Diff_RmCm = Vet_Rm - Vet_Cm
Vet_P = Vet_R - Vet_C
Vet_Produzione = np.where(Vet_Diff_RmCm > 0, 'Increase', np.where(Vet_Diff_RmCm == 0, 'Keep', 'Decrease'))

# Initialize multiple vectors
Vet_Rm = np.insert(Vet_Rm, 0, 0)
Vet_Cm = np.insert(Vet_Cm, 0, 0)
Vet_Diff_RmCm = np.insert(Vet_Diff_RmCm, 0, 0)
Vet_Produzione = np.insert(Vet_Produzione, 0, 'Keep')

# Create a dictionary with the results
results = {
    'Q': Vet_q,
    'R': Vet_R,
    'C': Vet_C,
    'Rm': Vet_Rm,
    'Cm': Vet_Cm,
    'Rm - Cm': Vet_Diff_RmCm,
    'P': Vet_P,
    'Production': Vet_Produzione
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(results)

# Output the results to an Excel file
df.to_excel('results.xlsx', index=False)

# Plot the results
fig, ax = plt.subplots()
ax.plot(Vet_q, Vet_R, label='R', marker='o', color='green')
ax.plot(Vet_q, Vet_C, label='C', marker='o', color='red')
ax.set_xlabel('Q')
ax.set_ylabel(' Revenues, Costs')
ax.set_title('Break-Even Analysis Graph')
ax.legend()
ax.grid(True)  # grid
ax.set_facecolor('white')  # set background color
ax.set_yticks(np.arange(0, 150, 10))  
plt.show()