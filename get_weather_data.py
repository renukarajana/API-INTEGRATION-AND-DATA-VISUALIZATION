import requests
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Replace with your OpenWeatherMap API key
API_KEY = "38280eaf4afd2cd501147112a68734d6"  # <--- Replace with your actual API key

# City for which you want to fetch weather data
CITY = "bangalore"  # You can change this to any city you like

# API endpoint for fetching current weather data
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    # Fetch data from the API
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()

    # Extract relevant data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    city_name = data["name"]

    # Print basic weather data
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

    # Create visualizations
    plt.figure(figsize=(12, 8))  # Adjust figure size for better layout

    # 1. Bar chart for Temperature, Humidity, and Wind Speed
    plt.subplot(2, 2, 1)  # 2 rows, 2 columns, first subplot
    metrics = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"]
    values = [temperature, humidity, wind_speed]
    sns.barplot(x=metrics, y=values, palette="viridis")
    plt.title(f"Weather Metrics in {city_name}", fontsize=14)
    plt.xlabel("Metric", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 2. Pie chart for Weather Description
    plt.subplot(2, 2, 2)  # 2 rows, 2 columns, second subplot
    # Get counts of each unique description.
    descriptions = [description] # Make sure description is a list.
    description_counts = {desc: descriptions.count(desc) for desc in set(descriptions)}
    plt.pie(description_counts.values(), labels=description_counts.keys(), autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    plt.title(f"Weather Description in {city_name}", fontsize=14)
    plt.tight_layout()

    # 3.  Display City Name
    plt.subplot(2, 2, 3)
    plt.text(0.5, 0.5, f"City: {city_name}", ha='center', va='center', fontsize=16, bbox=dict(facecolor='lightblue', alpha=0.5))
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Error: Key not found in API response. Check the API response format and ensure your API key is correct. Key Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}. Check the API response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
