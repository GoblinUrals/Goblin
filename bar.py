import matplotlib.pyplot as plt

x_list = list(range(0,5))
y1_list = [22,17,81,41,25]
y2_list = [62,37,39,36,49]

plt.title('Salary Graph')
plt.xlabel('days')
plt.ylabel('salary, $')
plt.plot(x_list, y1_list, label="Mark", marker='0')
plt.plot(x_list, y2_list, label="Steven", marker='^')
plt.legend()
plt.show()




