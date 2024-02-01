# import matplotlib.pyplot as plt
import math
LAND_AREA = 148940000000000
dogs = [0] * 20
dogs[5] = 2000000000
all_dogs = [2000000000]
z = []
for year in range(2000):
	for age in range(19, 0, -1):
		dogs[age] = dogs[age-1]
	dogs[0] = sum(dogs[5:15])*5
	print("years:",year+1, "\ndogs",sum(dogs), "\ndogs per capita:", sum(dogs)/8000000000, "\ndogs per square meter:", sum(dogs)/LAND_AREA, "\navg distance between dogs: ", math.sqrt((LAND_AREA/sum(dogs))), "meters\ndog increase factor:", sum(dogs)/all_dogs[-1], "\ndog log:", len(str(sum(dogs))), "\n")
	all_dogs += [sum(dogs)]
	add_dogs = [age*(20/max(dogs)) for age in dogs]
	# z.append(add_dogs)


# z = np.array(z)
# x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
#
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.contour(x, y, z)
# plt.title('z as 2d contour map')
# plt.show()
#
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1, projection='3d')
# ax.plot_surface(x, y, z)
# plt.title('z as 3d height map')
# plt.show()
#
# plt.figure()
# plt.title('z as 2d heat map')
# p = plt.imshow(z)
# plt.colorbar(p)
# plt.show()

