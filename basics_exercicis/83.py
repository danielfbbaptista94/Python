import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
jupiter_distance = jupiter.sun_distance
distance_sun = jupiter_distance * 149597870.691
print(distance_sun)
