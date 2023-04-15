from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from OSMPythonTools.nominatim import Nominatim
from streamlit_folium import st_folium
from IPython.display import display
import streamlit as st
from PIL import Image

import folium

st.title("Geo-spatial Web Application")

city = st.selectbox(
    'Which city would you like to focus on?',
    ('Washington DC', 'New York City', 'Seoul'))

amenity = st.selectbox(
    'What would you like to find?',
    ('Bars', 'Food Courts', 'Cafes', 'Libraries', 'Banks'))

st.write('Selected City:', city)
st.write('Selected Amenity:', amenity)

city_d = {
    'Washington DC':'Washington, District of Columbia, United States',
    'New York City':'New York, United States',
    'Seoul':'Seoul, South Korea '
}
amenity_d = {
    'Bars':'bar',
    'Food Courts':'food_court',
    'Cafes':'cafe',
    'Libraries':'library',
    'Banks':'bank'
}


city_d = {
    'Washington DC':'Washington, District of Columbia, United States',
    'New York City':'New York, United States',
    'Seoul':'Seoul, South Korea '
}
amenity_d = {
    'Bars':'bar',
    'Food Courts':'food_court',
    'Cafes':'cafe',
    'Libraries':'library',
    'Banks':'bank'
}

nominatim = Nominatim()
overpass = Overpass()

areaId = nominatim.query(city_d[city]).areaId()
query = overpassQueryBuilder(area=areaId, elementType='node', selector=f'"amenity"={amenity_d[amenity]}')
result = overpass.query(query)

elements = result.elements()
for element in elements:
    name = element.tag('name:en') or element.tag('name')
    lon = element.lon()
    lat = element.lat()
    phone = element.tag('phone')
    opening_hours = element.tag('opening_hours')
    addr_street = element.tag('addr:street')
    addr_housenumber = element.tag('addr:housenumber')

    print(f"Name: {name}")
    print(f"Longitude: {lon}")
    print(f"Latitude: {lat}")
    print(f"Phone: {phone}")
    print(f"Opening hours: {opening_hours}")
    print(f"Address: {addr_street} {addr_housenumber}")
    print("--------------------")
    
city_loc = nominatim.query(city_d[city]).toJSON()[0]
city_lat = city_loc['lat']
city_lon = city_loc['lon']

default_zoom = 11
max_width = 300

# create base map
base_map = folium.Map(location=[city_lat, city_lon], zoom_start=default_zoom)

for element in elements[:30]:
    name = element.tag('name:en') or element.tag('name')
    lon = element.lon()
    lat = element.lat()
    phone = element.tag('phone')
    opening_hours = element.tag('opening_hours')
    addr_street = element.tag('addr:street')
    addr_housenumber = element.tag('addr:housenumber')

    # create popups containing name, lon lat, phone, hours, address (if fields exist)
    popup_info = ""
    if name:
        popup_info += f"<b>Name:</b> {name}<br>"
    if lon and lat:
        popup_info += f"<b>Lon:</b> {lon}, <b>Lat:</b> {lat}<br>"
    if phone:
        popup_info += f"<b>Phone:</b> {phone}<br>"
    if opening_hours:
        popup_info += f"<b>Opening hours:</b> {opening_hours}<br>"
    if addr_street or addr_housenumber:
        popup_info += f"<b>Address:</b> {addr_street or ''} {addr_housenumber or ''}<br>"
        
    popup = folium.Popup(popup_info, max_width=max_width)

    # add markers to map with popup
    folium.Marker(location=[lat, lon], popup=popup).add_to(base_map)
    
st_data = st_folium(base_map)