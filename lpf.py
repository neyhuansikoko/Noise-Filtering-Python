import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('FILE_ADDRESS', names=['Index', 'X', 'Y', 'Z', 'Class'])
df = df[['Index', 'X']]

max_value = df['X'].max()

print(max_value)

sampling_rate = max_value * 2
input_signal = df['X'].to_numpy()

cutoff_frequency = sampling_rate / 200

allpass_output = np.zeros_like(input_signal)

dn_1 = 0

for n in range(input_signal.shape[0]):
  tan = np.tan(np.pi * cutoff_frequency / sampling_rate)

  a1 = (tan - 1) / (tan + 1)

  allpass_output[n] = a1 * input_signal[n] + dn_1

  dn_1 = input_signal[n] - a1 * allpass_output[n]

filter_output = input_signal + allpass_output
filter_output = filter_output *  0.5

plt.plot(input_signal, label='input_signal')
plt.plot(filter_output, label='filter_output')
plt.legend()
plt.show()