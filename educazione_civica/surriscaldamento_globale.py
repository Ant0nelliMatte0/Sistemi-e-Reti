import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import csv

anno = []
valore = []

data_file = open("./Temperature_Anomaly.csv")
data_reader = csv.reader(data_file, delimiter = ',')
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)

for row in data_reader:
    anno.append(float(row[0]))
    valore.append(float(row[1]))

fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('grafici surriscaldamento globale')

ax1.plot(anno, valore, 'o-g')
ax1.set_xlabel('anno')
ax1.set_ylabel('valore(°C)')

plt.show()