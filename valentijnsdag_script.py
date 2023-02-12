import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

xlim = [-3,2]
ylim = [-3,2]
N = 18000

df = pd.DataFrame({
    'x': np.random.uniform(xlim [0], xlim[1], N),
    'y': np.random.uniform(ylim [0], ylim[1], N)
    })
#df.plot.scatter(x='x', y='y')

def get_shape(x,y):
    return (x**2 + y**2 -1)**3 - x**2 * y**3

def get_points(row):
    dist = get_shape(row['x'], row['y'])
    if dist <=0 :
        return 1
    return 0

df['color'] = df.apply(get_points, axis=1)
df2 = df[df['color']==1]
df2.plot.scatter(x='x', y='y', color= 'red')

tekst_groot = "Fijne Valentijnsdag"
Naam1= "Cegeka"                                ##zet hier jouw naam
Symbool1=" ♥ "
Naam2= "haar klanten"                          ##zet hier de naam van je partner
Samen = Naam1+Symbool1+Naam2

plt.text(xlim[0]+2, ylim[1]-1.5, tekst_groot,   fontsize=28, color= 'black'   )
plt.text(xlim[0]+2.33, ylim[1]-3, Samen, fontsize=20, color= 'black')  ##staat je tekst niet precies in het midden , vervang dan de waarde 2.33 door een kleiner getal

plt.show()