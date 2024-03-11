# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk # DeckGL for 3D interactive maps
import plotly.express as px





# Set the title
st.title('Motor Vehicle Collisions in New York City')

# Title image
st.image('Crash.jpeg', caption=' ')

st.markdown('Dashboard to Analyze Motor Vehicle Collisions in NYC')

# Specify data url
DATA_URL = (
'Motor_Vehicle_Collisions_-_Crashes.csv'
)

# Load Motor Vehicle Collision Data
@st.cache(persist = True) # Only rerun the computation when some input in dataset changes
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows, parse_dates = [['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset = ['LATITUDE', 'LONGITUDE'], inplace = True)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis = 'columns', inplace = True)
    data.rename(columns = {'crash_date_crash_time': 'date/time'}, inplace = True)

    return data

# Load some data
data = load_data(100000)
raw_data = data

# Visualize Data on Map
st.header('Where do most people suffer from injury in NYC?')
injured_people = st.slider('Number of injury in vehicle collisions', 0, 19) # slider range
st.map(data.query('injured_persons >= @injured_people')[['latitude', 'longitude']].dropna(how ='any'))


# FIltering Data and Interactive Tables
st.header('How many Collisions occur during a given time of day?')
# hour = st.selectbox('Hours in 24 HOUR MILITARY FORMAT (00.00 - 23.59)', range(0,24), 1)
# hour = st.sidebar.slider('Hours in 24 HOUR MILITARY FORMAT (00.00 - 23.59)',0,23)
hour = st.slider('Hours in 24 HOUR MILITARY FORMAT (00.00 - 23.59)',0,23)
data = data[data['date/time'].dt.hour == hour]

# Plot Filtered Data on 3D Interactive Map
st.markdown('Vehicle collisions between %i:00 and %i:00' % (hour, (hour + 1) %24))
midpoint = (np.average(data['latitude']), np.average(data['longitude']))

st.write(pdk.Deck(
    map_style = 'mapbox://styles/mapbox/light-v9',  #check documentation of pydeck to customize
    initial_view_state = {
        "latitude" : midpoint[0],
        "longitude" : midpoint[1],
        "zoom" : 11,
        "pitch" : 50,
    },

    # Add a layer on top of the empty map to plot dataset
    layers = [
        pdk.Layer(
            "HexagonLayer",
            data = data[['date/time', 'latitude', 'longitude']],
            get_position = [ 'longitude','latitude'],
            radius = 100, # Radius of each data points in meters
            extruded = True, # False if the map is 2D
            pickable = True,
            elevation_scale = 4,

            ),
    ]


))

# Add charts and histograms using Plotly
st.subheader("Breakdown the collisions by minute between %i:00 and %i:00" %(hour,(hour +1) %24))
filtered = data[
    (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour + 1))
]

hist = np.histogram(filtered['date/time'].dt.minute, bins = 60, range = (0,60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'crashes' : hist})
fig = px.bar(chart_data, x = 'minute', y = 'crashes', hover_data = ['minute', 'crashes'], height = 400)
st.write(fig)


# Select Data using Dropdowns
st.header('Top 5 dangerous streets ')
select = st.selectbox('Affected type of people', ['Pedestrians', 'Cyclists', 'Motorists'])

# '''
# Sketch :
# if select == Pedestrians :
# then query(data)
# WHERE injured Pedestrians
# AND sort(list( injured Pedestrians)) BY Descending order
#
# '''

if select == 'Pedestrians' :
    st.write(raw_data.query("injured_pedestrians >= 1")[['on_street_name','injured_pedestrians']].sort_values(by = ['injured_pedestrians'], ascending = False).dropna(how = 'any')[:5])
elif select == 'Cyclists' :
    st.write(raw_data.query("injured_cyclists >= 1")[['on_street_name','injured_cyclists']].sort_values(by = ['injured_cyclists'], ascending = False).dropna(how = 'any')[:5])
else :
    st.write(raw_data.query("injured_motorists >= 1")[['on_street_name','injured_motorists']].sort_values(by = ['injured_motorists'], ascending = False).dropna(how = 'any')[:5])



# Display the data
if st.checkbox('Show Raw Data', False):
    st.subheader('Raw Data')
    st.write(data)


# footer
footer = """<style> .footer {
position: fixed; left: 0; bottom: 0; width: 100%; background-color: black; color: white; text-align: center;
}
</style>
<div class="footer">
Dashboard by Navid Tehseen 2024
</div>
"""
st.markdown(footer, unsafe_allow_html=True)