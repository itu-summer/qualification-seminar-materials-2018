import math
import matplotlib.pyplot as plt
# %matplotlib notebook


upper_bound = 200
input_values = range(1, upper_bound)
constant = [1 for i in input_values]
linear = [i for i in input_values]
quadratic = [i ** 2 for i in input_values]
cubic = [i ** 3 for i in input_values]
exponential = [2 ** i for i in input_values]
logaritmic = [math.log2(i) for i in input_values]
linear_logaritmic = [i * math.log2(i) for i in input_values]

plt.plot(input_values, constant, label='$O(1)$')
plt.plot(input_values, logaritmic, label='$O(log_2(n))$')
plt.plot(input_values, linear, label='$O(n)$')
plt.plot(input_values, linear_logaritmic, label='$O(nlog_2(n))$')
plt.plot(input_values, quadratic, label='$O(n^2)$')
plt.plot(input_values, cubic, label='$O(n^3)$')
plt.plot(input_values, exponential, label='$O(n^3)$')


plt.axis([0, 80, 0, 100])
plt.legend(loc='upper right')
# Set chart title and label axes.
plt.title("Worst-case run time classes", fontsize=20)
plt.xlabel("n", fontsize=14)
plt.ylabel("Runtime", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.savefig('images/runtime_classes.png')
