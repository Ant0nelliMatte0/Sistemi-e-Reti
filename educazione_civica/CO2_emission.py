import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import csv

anno = []
Emissioni_tot = []
Carburante_gas = []
Carburante_liquido = []
Carburante_solido = []
Cemento = []
Gas_flaring = []
Per_Capita = []

data_file = open("./CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter = ',')
next(data_reader)
next(data_reader)

for row in data_reader:
    anno.append(float(row[0]))
    Emissioni_tot.append(float(row[1]))
    Carburante_gas.append(float(row[2]))
    Carburante_liquido.append(float(row[3]))
    Carburante_solido.append(float(row[4]))
    Cemento.append(float(row[5]))
    Gas_flaring.append(float(row[6]))
    if row[7] is None:
        Per_Capita.append(0.0)
    else:
        Per_Capita.append(row[7])

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1)
fig.suptitle('grafici surriscaldamento globale')

ax1.plot(anno, Emissioni_tot, 'g')
ax1.set_xlabel('anno')
ax1.set_ylabel('Emissioni_tot')

ax2.plot(anno, Carburante_gas, 'y')
ax2.set_xlabel('anno')
ax2.set_ylabel('Carburante_gas')

ax3.plot(anno, Carburante_liquido, 'r')
ax3.set_xlabel('anno')
ax3.set_ylabel('Carburante_liquido')

ax4.plot(anno, Carburante_solido, 'b')
ax4.set_xlabel('anno')
ax4.set_ylabel('Carburante_solido')

ax5.plot(anno, Cemento, 'g')
ax5.set_xlabel('anno')
ax5.set_ylabel('Cemento')

ax6.plot(anno, Gas_flaring, 'y')
ax1.set_xlabel('anno')
ax1.set_ylabel('Gas_flaring')

ax6.plot(anno, Per_Capita, 'r')
ax6.set_xlabel('anno')
ax6.set_ylabel('Per_Capita')

plt.show()