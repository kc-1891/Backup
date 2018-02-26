from geopy.geocoders import Nominatim

loc = Nominatim()
add = loc.geocode("1 Sibley Park Road, Earley")
print(add)
print(add.latitude)
print(add.longitude, '\n')

from geopy.geocoders import GoogleV3

l = GoogleV3()
a = l.geocode("1 Sibley Park Road, Earley")
print(a)
print(a.latitude)
print(a.longitude)
