import matplotlib.pyplot as plt
import numpy as np

epochs = [5*i for i in range(1,11)]
train = np.array([
    3.964075411690606,
    2.9546794732411703,
    2.4575167496999106,
    1.972292462984721,
    1.5081013176176283,
    1.16615756087833,
    0.9519165582127042,
    0.8399800260861715,
    0.7721771160761516,
    0.6971113257937961
])

val = np.array([
    3.7828709284464517,
    2.9033023715019226,
    2.4819130897521973,
    2.0554769535859427,
    1.6335046390692394,
    1.3131142755349476,
    1.1423973441123962,
    1.0297658344109852,
    0.9768550197283427,
    0.8916531701882681
])
a = [[j,i] for i,j in zip(epochs,train)]
b = [[j,i] for i,j in zip(epochs,val)]
print("a: ", len(a))
print("b: ", len(b))
plt.plot(epochs, train, label='Training Loss', color='orange')
plt.plot(epochs, val, label='Validation Loss', color='blue')
plt.legend()
plt.show()
