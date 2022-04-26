import math
import random
import matplotlib.pyplot as plt

# array for generated data
tab = []

# generating data
for i in range(1000):
	o = 0
	for j in range(10):
		if random.random() < 0.5:
			o += 1
	tab.append(o)

# results analysis
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in tab:
	res[i] += 1

# preparing data for plot
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plot_text = ''

# wartość oczekiwana

expected_value = 0

sum_temp = 0
sum_temp_2 = 0
for i in range(len(res)):
	sum_temp += res[i] * i
	sum_temp_2 += res[i]

expected_value = sum_temp / sum_temp_2

plot_text += 'Wartość oczekiwana: ' + str(expected_value) + '\n'

# prawdopodobieństwo

probability = []

for i in res:
	probability.append(i / 1000)

# średnia arytmetyczna

average = 0

for i in range(len(res)):
	average += i * probability[i]

average /= 11

plot_text += 'Średnia arytmetyczna: ' + str(round(average, 3)) + '\n'

# Wariancja

variance = 0

for i in range(len(res)):
	variance += (i - average) ** 2 * probability[i]

plot_text += 'Wariancja: ' + str(round(variance, 3)) + '\n'


# Poisson Distribution


def pois(num):
	return ((expected_value ** num) * (math.e ** (-expected_value))) / (math.factorial(num))


pois_y = []
for i in x:
	pois_y.append(pois(i) * 1000)

# error bars
error_bars = []
for i in res:
	error_bars.append(i ** 0.5)

# generating plot
plt.bar(x, res, yerr=error_bars)
plt.grid(color='grey', linestyle='--', linewidth=1, alpha=0.6)
plt.title('Wykres')
plt.xlabel('Ilość orłów w jednej serii')
plt.ylabel('Ilość jednakowej wielkości serii')
plt.plot(x, pois_y, 'r--')
plt.axis(ymax=300)
plt.text(7, 290, plot_text)

plt.show()
