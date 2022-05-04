
import matplotlib.pyplot as plt
import numpy as np

epochs = [5*i for i in range(1,11)]
train = np.array([
    3.9976735432942707,
    3.2146670553419323,
    2.9078548749287925,
    2.7338196489546034,
    2.5889493730333117,
    2.4656562752193874,
    2.3443063682980005,
    2.2377181477016874,
    2.164258744981554,
    2.1049967024061416
])

val = np.array([
    3.8534605503082275,
    3.1765902638435364,
    2.923163195451101,
    2.796933114528656,
    2.696616609891256,
    2.6014734903971353,
    2.5007929603258767,
    2.446851074695587,
    2.3836488326390586,
    2.3825730085372925

])
a = [[j,i] for i,j in zip(epochs,train)]
b = [[j,i] for i,j in zip(epochs,val)]
print("a: ", len(a))
print("b: ", len(b))
plt.plot(epochs, train, label='Training Loss', color='orange')
plt.plot(epochs, val, label='Validation Loss', color='blue')
plt.legend()
plt.show()
