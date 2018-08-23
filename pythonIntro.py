
import pandas as pd


df = pd.read_csv("rendimiento_distancia_litors.csv")

print df
print df.columns


print "select data : "
print "by label / position"

dfFila = df.ix[2]
print dfFila

dfRendimiento = df.ix[:,'rendimiento']
print dfRendimiento

print "fila, columna"
print df.ix[1,'rendimiento']


print df[(df['rendimiento']>2) | (df['rendimiento']<4)]

print "sort:"
print dfRendimiento.sort_values()

print "count: "

print dfRendimiento.count()

print "sum: "

print dfRendimiento.sum()

print "min: "
print dfRendimiento.min()

print "max: "
print dfRendimiento.max()

print "median: "
print dfRendimiento.median()

print "meam: "
print dfRendimiento.mean()

print "mode"
print dfRendimiento.mode()

print "quantile"
print dfRendimiento.quantile(0.25)

print "\n***** describe ****"
print dfRendimiento.describe()


print "--------------------------------"
print "Applyin functions: "

f = lambda x: x*2
print dfRendimiento.apply(f)

print "-------------------------------"
print "group by: SUM"
dfSum = df.groupby(by=['fecha']).sum()
print dfSum.ix[:,'rendimiento']
print "-------------------------------"
print "group by: count"
print df.groupby(by=['fecha']).count()


print "-------------------------------"
print "visualizing..."
import matplotlib.pyplot as plt

dfRendimiento.plot()
plt.show()
