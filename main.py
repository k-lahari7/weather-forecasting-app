import random

def get_weather_forecast():
    """Get the weather forecast for a specific location."""
    # Generate random weather data for demonstration purposes
    temperature = random.randint(-10, 40)
    humidity = random.randint(0, 100)
    conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    weather = random.choice(conditions)

    forecast = {
        'temperature': temperature,
        'humidity': humidity,
        'weather': weather
    }

    return forecast

def main():
    print("Weather Forecast App")

    while True:
        location = input("Enter a location (or 'q' to quit): ")
        if location.lower() == 'q':
            break

        forecast = get_weather_forecast()
        print("\nWeather forecast for", location)
        print("Temperature:", forecast['temperature'], "°C")
        print("Humidity:", forecast['humidity'], "%")
        print("Conditions:", forecast['weather'])

if __name__ == '__main__':
    main()
