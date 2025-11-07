import streamlit as st
import requests

API_KEY = ""
CITY = "Karlsruhe"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

weather = {
    "temperature": data["main"]["temp"],
    "description": data["weather"][0]["description"],
    "humidity": data["main"]["humidity"],
    "wind_speed": data["wind"]["speed"]
}

print(weather)

forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

next_hours = []
for entry in forecast_data["list"][:4]:  # Next 12 hours (3h * 4)
    next_hours.append({
        "time": entry["dt_txt"],
        "temp": entry["main"]["temp"],
        "desc": entry["weather"][0]["description"]
    })

print(next_hours)

st.title(f"🌤️ Real-Time Weather in {CITY}")
st.metric("Temperature", f"{weather['temperature']}°C")
st.text(f"Description: {weather['description'].capitalize()}")
st.text(f"Humidity: {weather['humidity']}%")
st.text(f"Wind Speed: {weather['wind_speed']} m/s")

st.subheader("Next 12 Hours")
for entry in next_hours:
    st.write(f"{entry['time']} - {entry['temp']}°C - {entry['desc'].capitalize()}")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
