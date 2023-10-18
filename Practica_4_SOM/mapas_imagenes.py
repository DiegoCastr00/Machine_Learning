from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt



img = plt.imread('/content/sample_data/pinos.jpg')


pixels = np.reshape(img, (img.shape[0]*img.shape[1], 3)) / 255.


print('training...')
som = MiniSom(2, 3, 3, sigma=1.,
              learning_rate=0.2, neighborhood_function='bubble')  
som.random_weights_init(pixels)
starting_weights = som.get_weights().copy()  
som.train(pixels, 10000, random_order=True, verbose=True)

print('quantization...')
qnt = som.quantization(pixels) 
print('building new image...')
clustered = np.zeros(img.shape)
for i, q in enumerate(qnt):  
    clustered[np.unravel_index(i, shape=(img.shape[0], img.shape[1]))] = q
print('done.')


plt.figure(figsize=(7, 7))
plt.figure(1)
plt.subplot(221)
plt.title('original')
plt.imshow(img)
plt.subplot(222)
plt.title('result')
plt.imshow(clustered)

plt.subplot(223)
plt.title('initial colors')
plt.imshow(starting_weights, interpolation='none')
plt.subplot(224)
plt.title('learned colors')
plt.imshow(som.get_weights(), interpolation='none')

plt.tight_layout()
plt.show()