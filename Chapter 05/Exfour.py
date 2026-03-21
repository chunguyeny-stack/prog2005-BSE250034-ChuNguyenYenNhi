import matplotlib.pyplot as plt
cities = ['A', 'B', 'C', 'D', 'E']
area = [500, 300, 700, 200, 600]
cities, area = zip(*sorted(zip(cities, area), key=lambda x: x[1], reverse=True))
plt.barh(cities, area)
plt.title("Xếp hạng diện tích thành phố")
plt.xlabel("Diện tích (km2)")
plt.show()
