import matplotlib.pyplot as plt

fabrics_circulation = [4420,4640,4625]
clothes_circulation = [6720,7400,6630]
footwear_circulation = [5854,6250,6500]
jersey_circulation = [3682,3850,4500]
haberdashery_circulation = [2694,3000,3590]
year = [2013,2014,2015]

plt.plot(fabrics_circulation,year,label = "Тканини")
plt.plot(clothes_circulation,year,label = "Одяг")
plt.plot(footwear_circulation,year,label = "Взуття")
plt.plot(jersey_circulation,year,label = "Трикотаж")
plt.plot(haberdashery_circulation,year,label = "Галантерея")
plt.xlabel("Товарообіг")
plt.ylabel("Рік")
plt.legend()
plt.grid(True)

plt.show()