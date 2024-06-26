import folium
import json
import webbrowser
import os

def generateMap(strike_pos, mic_pos, mic_time_offset):
    zoom_start = 0
    mic_icon_color = ""
    lightning_icon_color = ""
    mic_icon = ""
    lightning_icon = ""

    with open(f"{os.path.dirname(__file__)}/styles.json", "r") as f:
        data = json.load(f)

        zoom_start = data.get("zoom_start", zoom_start)
        mic_icon_color = data.get("mic_icon_color", mic_icon_color)
        lightning_icon_color = data.get("lightning_icon_color", lightning_icon_color)
        mic_icon = data.get("mic_icon", mic_icon)
        lightning_icon = data.get("lightning_icon", lightning_icon)

    m = folium.Map(location=strike_pos, zoom_start=zoom_start)

    marker = folium.Marker(location=strike_pos, tooltip="Lightning strike!")
    marker.add_to(m)
    marker_data = {
        "prefix": "fa",
        "color": lightning_icon_color,
        "icon": lightning_icon,
        "angle": 0
    }
    icon = folium.Icon(**marker_data)
    marker.add_child(icon)

    marker_data = {
        "prefix": "fa",
        "color": mic_icon_color,
        "icon": mic_icon,
        "angle": 0
    }
    for i in range(3):
        marker = folium.Marker(location=mic_pos[i], tooltip=f"{mic_time_offset[i]}ms")
        marker.add_to(m)
        icon = folium.Icon(**marker_data)
        marker.add_child(icon)
        line = folium.PolyLine(
            locations=[mic_pos[i], strike_pos],
            color="red",
            weight=3
        )
        line.add_to(m)

    m.save("map.html")
    webbrowser.open("map.html") # it's a bit primitive, but works, right?

    input("Press Enter to close . . .")