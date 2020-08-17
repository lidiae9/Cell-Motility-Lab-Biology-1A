import pandas as pd
from matplotlib import pyplot 

#The Effect of Toxin A on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time
#Defining the variable for time in seconds.
time_x = [180,360,540,720,900,1080,1260,1440,1620,1800]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) in the control group.
con_y = [71.86,104.24,92.34,93.60,97.43,79.72,91.85,90.58,86.32,72.22]
statcellcon_y = [0,0,0,0,0,0,0,0,0,0]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) after being exposed to Toxin A.
txna_y = [79.75,76.04,70.77,70.08,56.48,42.67,40.1,8.61,3.31,0.00]
statcella_y = [5,6,7,11,11,16,21,28,30,32]


fig, ax1 = pyplot.subplots()

ax1.plot(time_x, con_y, label="Velocity of Control Group")
ax1.plot(time_x, statcellcon_y, label="Stationary Cells of Control Group")
ax1.plot(time_x, txna_y, label="Velocity of Group with Toxin A")
ax1.plot(time_x, statcella_y, label="Stationary Cells of Toxin Group A")

pyplot.title("The Effect of Toxin A on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time")
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Average Velocity (µms-1)")

#allows for the addition of a secondary axis and a label.
ax2 = ax1.twinx()
ax2.set_ylabel("Number of Secondary Cells")

ax1.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol= 2)
pyplot.show()

#The Effect of Toxin B on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time
time_x = [180,360,540,720,900,1080,1260,1440,1620,1800]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) in the control group.
con_y = [71.86,104.24,92.34,93.60,97.43,79.72,91.85,90.58,86.32,72.22]
statcellcon_y = [0,0,0,0,0,0,0,0,0,0]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) after being exposed to Toxin B.
txnb_y = [86.90,88.30,92.65,72.97,63.50,47.46,18.01,1.23,0.00,0.00]
statcellb_y = [5,6,7,16,18,19,20,25,25,26]

fig, ax1 = pyplot.subplots()

ax1.plot(time_x, con_y, label="Velocity of Control Group")
ax1.plot(time_x, statcellcon_y, label="Stationary Cells of Control Group")
ax1.plot(time_x, txnb_y, label="Velocity of Group with Toxin B")
ax1.plot(time_x, statcellb_y, label="Stationary Cells of Toxin Group B")

pyplot.title("The Effect of Toxin B on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time")
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Average Velocity (µms-1)")

#allows for the addition of a secondary axis and a label.    
ax2 = ax1.twinx()
ax2.set_ylabel("Number of Secondary Cells")

ax1.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol= 2)
pyplot.show()


#The Effect of Toxin C on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time
time_x = [180,360,540,720,900,1080,1260,1440,1620,1800]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) in the control group.
con_y = [71.86,104.24,92.34,93.60,97.43,79.72,91.85,90.58,86.32,72.22]
statcellcon_y = [0,0,0,0,0,0,0,0,0,0]

#Defining the velocity of cells (con_y) and the number of static cells (statcellcon_y) after being exposed to Toxin C.
txnc_y = [81.10,74.92,65.02,56.80,36.54,46.72,65.64,91.22,97.20,98.96]
statcellc_y = [3,8,8,16,16,13,6,4,2,1]

fig, ax1 = pyplot.subplots()

ax1.plot(time_x, con_y, label="Velocity of Control Group")
ax1.plot(time_x, statcellcon_y, label="Stationary Cells of Control Group")
ax1.plot(time_x, txnc_y, label="Velocity of Group with Toxin C")
ax1.plot(time_x, statcellc_y, label="Stationary Cells of Toxin Group C")

pyplot.title("The Effect of Toxin C on Average Velocity and Number of Stationary Cells of Paramecium Compared to a Control Group Over Time")
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Average Velocity (µms-1)")

#allows for the addition of a secondary axis and a label.  
ax2 = ax1.twinx()
ax2.set_ylabel("Number of Secondary Cells")

ax1.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol= 2)
pyplot.show()
