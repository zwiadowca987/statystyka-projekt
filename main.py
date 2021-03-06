# It imports libraries that are needed for the program to work.
import math
import random
import matplotlib.pyplot as plt

# List containing the number of eagles in 1000 randomly generated series of 10 throws.
tab = []

# Generating 1000 series of 10 throws and counting how many times the coin landed on the eagle side.
for i in range(1000):
	o = 0
	for j in range(10):
		if random.random() < 0.5:
			o += 1
	tab.append(o)

# Counting how many times each number of eagles appeared in the generated data.
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in tab:
	res[i] += 1

# Preparing data for plot.
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plot_text = ''

# EXPECTED VALUE
# It calculates the expected value of the number of eagles in a series of 10 throws.
expected_value = 0

sum_temp = 0
sum_temp_2 = 0
for i in range(len(res)):
	sum_temp += res[i] * i
	sum_temp_2 += res[i]

expected_value = sum_temp / sum_temp_2

plot_text += 'Wartość oczekiwana: ' + str(expected_value) + '\n'

# PROBABILITY
# Calculating the probability of each number of eagles in a series of 10 throws.
probability = []

for i in res:
	probability.append(i / 1000)

# AVERAGE
# It calculates the average value of the number of eagles in a series of 10 throws.
average = 0

for i in range(len(res)):
	average += i * probability[i]

# Variance
# It calculates the variance of the number of eagles in a series of 10 throws.
variance = 0

for i in range(len(res)):
	variance += (i - average) ** 2 * probability[i]

plot_text += 'Wariancja: ' + str(round(variance, 3)) + '\n'

# Poisson Distribution


def pois(num):
	"""
	It takes the expected value of the Poisson distribution, raises it to the power of the number of successes, multiplies
	it by e to the power of the negative of the expected value, and divides it by the factorial of the number of successes

	:param num: the number of events
	:return: The probability of a certain number of events occurring in a given time period.
	"""
	return ((expected_value ** num) * (math.e ** (-expected_value))) / (math.factorial(num))


pois_y = []
for i in x:
	pois_y.append(pois(i) * 1000)

# CHI-SQUARED DISTRIBUTION
# It calculates the chi-squared distribution.
chi_distrib = 0

for i in range(len(res)):
	chi_distrib += (res[i] - pois_y[i]) ** 2 / pois_y[i]

plot_text += 'Rozkład Chi^2: ' + str(round(chi_distrib, 3)) + '\n'

# Calculating the error bars for the plot.
error_bars = []
for i in res:
	error_bars.append(i ** 0.5)

# Generating a plot.
plt.bar(x, res, yerr=error_bars)
plt.grid(color='grey', linestyle='--', linewidth=1, alpha=0.6)
plt.title('Wykres')
plt.xlabel('Ilość orłów w jednej serii')
plt.ylabel('Ilość jednakowej wielkości serii')
plt.plot(x, pois_y, 'r--')
plt.axis(ymax=300)
plt.text(7, 290, plot_text)

# It shows the plot.
plt.show()
