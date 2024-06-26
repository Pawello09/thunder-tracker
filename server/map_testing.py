import graphics.generateMap as gM
import calculatePosition as calcP

lat = []
lon = []
t = []

for i in range(3):
    lat.append(float(input(f"Latitude {i+1}: ")))
    lon.append(float(input(f"Longitude {i+1}: ")))
    t.append(int(input(f"Time {i+1}: ")))

    print(" --- ")

position = calcP.calculatePosition(
    lat[0], lon[0], t[0],
    lat[1], lon[1], t[1],
    lat[2], lon[2], t[2]
)

gM.generateMap(
    [position[0], position[1]],
    [
        [lat[0], lon[0]],
        [lat[1], lon[1]],
        [lat[2], lon[2]]
    ],
    t
)