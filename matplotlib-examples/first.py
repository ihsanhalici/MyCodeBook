import matplotlib.pyplot as plt
plt.figure()

x_series   = [ x for x in xrange(0,10) if x%2==0 ]
y_series_1 = [x**2 for x in x_series]
y_series_2 = [x**3 for x in x_series]

plt.xlabel("Small X Interval")
plt.ylabel("Calculated Data")
plt.title("Our Fantastic Graph")

plt.xlim(0, 6)
plt.ylim(-5, 80)


plt.plot(x_series, y_series_1, label="x^2")
plt.plot(x_series, y_series_2, label="x^3")

plt.legend(loc="upper left")

plt.savefig("1.png")