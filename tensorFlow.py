import tensorFlow as mesin_ai
# prinsip import LIBRARY as ALIAS
# nama dataset = taksonomi_hewan

hewan = mesin_ai.keras.dataset.taksonomi_hewan # memasukkan dataset ke variabel "hewan"

# training data x, y
# testing data x, y
(x_train, y_train), (x_test, y_test) = hewan.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 # normalisasi nilai input
model_ai = mesin_ai.keras.models.Sequential([ # membuat model AI dari dataset

        mesin_ai.keras.layers.Flatten(input_shape=(28, 28)),
        # melakukan flatten untuk mengubah dataset matriks 28 x 28 pixel menjadi array 784 elemen
        
        mesin_ai.keras.layers.Dense(512, activation=mesin_ai.nn.relu), # hidden layer
        # jika angka 512, maka jumlah unit/neuron adalah 512 

        mesin_ai.keras.layers.Dense(10, activation=mesin_ai.nn.softmax) # output
])





