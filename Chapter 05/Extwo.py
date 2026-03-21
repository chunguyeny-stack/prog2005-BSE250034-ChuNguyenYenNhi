import matplotlib.pyplot as plt
x = list(range(0, 11))
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Đồ thị y = x^2 và y = x^3")
plt.show()
