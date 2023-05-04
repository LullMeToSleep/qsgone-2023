import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Phenol_Red_data = pd.read_csv("Phenol_Red_Assay.csv")

Time_s = np.array(Phenol_Red_data.iloc[:,0])
Column = np.array(Phenol_Red_data.iloc[:,1])
ABS_410 = np.array(Phenol_Red_data.iloc[:,2])

Times = Time_s[::36]

# reshape the 2D array into a 3D array with 3 rows and 12 columns for each slice
ABS_410_3D = ABS_410.reshape((-1, 3, 12))

# calculate the mean and standard deviation for each column for every 3 rows
means = np.mean(ABS_410_3D, axis=1)
stds = np.std(ABS_410_3D, axis=1)

labels = ('pH 8.13', 'pH 7.92', 'pH 7.80', 'pH 7.55', 'pH 7.33', 'pH 6.92', 'pH 6.51',
          'blank', 'negative control', 'positive control', 'PON2 w/ oxododecanoyl', 'PON2 w/ oxooctanoyl')

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'black']

fig = plt.figure(num = 1, clear = True) #create figure
ax = fig.add_subplot(1,1,1) #create subplot
ax.grid(True)
for i, col in enumerate(means.T):
    plt.errorbar(Times, col, yerr=stds[:,i], label=labels[i], color=colors[i])
plt.xlabel('time (s)') #x label
plt.ylabel('absorption at 410nm (-)') #y label
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
fig.tight_layout() #tight layout
fig.savefig("Phenol_Red.png", bbox_inches='tight', dpi=1000)
