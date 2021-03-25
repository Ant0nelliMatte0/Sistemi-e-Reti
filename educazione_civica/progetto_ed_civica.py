import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temperatura = []
giorni_scuola = []
giorni_giacca = []
giorni_videogioco = []

data_file = open("./progetto_ed_civica.csv")
data_reader = csv.reader(data_file, delimiter = ',')
next(data_reader)

for row in data_reader:
    mesi_n.append(int(row[0]))
    temperatura.append(int(row[1]))
    giorni_scuola.append(int(row[2]))
    giorni_giacca.append(int(row[3]))
    giorni_videogioco.append(int(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('grafici esercitazione educazione fisica')

ax1.plot(mesi_n, temperatura, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperatura')

ax2.plot(mesi_n, giorni_scuola, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('scuola')

ax3.plot(mesi_n, giorni_giacca, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('giacca')

ax4.plot(mesi_n, giorni_videogioco, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('videogiochi')

plt.show()  