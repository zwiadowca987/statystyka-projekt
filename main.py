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


# Poisson Distribution


def pois(num):
	return ((5 ** num) * (math.e ** (-5))) / (math.factorial(num))


pois_y = []
for i in x:
	pois_y.append(pois(i) * 1000)

# generating plot
plt.bar(x, res)
plt.grid(color='grey', linestyle='--', linewidth=1, alpha=0.6)
plt.title('Wykres')
plt.xlabel('Ilość orłów w jednej serii')
plt.ylabel('Ilość jednakowej wielkości serii')
plt.plot(x, pois_y, 'r--')

plt.show()
