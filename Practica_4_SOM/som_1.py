import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
from pylab import pcolor, colorbar, plot

vinhos = pd.read_csv('/content/sample_data/wine.csv')
vinhos.head()

x = vinhos.iloc[:,1:].values
y = vinhos.iloc[:,0].values

normalizador = MinMaxScaler(feature_range=(0,1))
x = normalizador.fit_transform(x)

som = MiniSom(x=8, y=8, input_len=13, sigma=1.0, learning_rate=0.5, random_seed=2)
som.random_weights_init(x)
som.train_random(data=x, num_iteration=100)

som._weights
som._activation_map
q = som.activation_response(x)

y[y==1] = 0
y[y==2] = 1
y[y==3] = 2

markers = ['o', 'D', 's']
color=['r', 'g', 'b']

pcolor(som.distance_map().T)
colorbar()

for i, X in enumerate(x):
  w=som.winner(X)
  plot(w[0]+0.5, w[1]+0.5, markers[y[i]], markerfacecolor='None', markersize=10, markeredgecolor=color[y[i]], markeredgewidth=2)