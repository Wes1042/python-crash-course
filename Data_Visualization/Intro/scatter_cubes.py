import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#plt.axis([x_values,y_values])
plt.axis([0, 5100, 0, 5100**3])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')