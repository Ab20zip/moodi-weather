from weather import get_weather_data
from mood import get_weather_description
import config


def main():
    city = input("Enter your city: ")
    user_mood = input("Enter your mood: ").lower()

    weather_data = get_weather_data(city, config.API_KEY)
    if not weather_data:
        print("Error fetching weather data.")
        return

    current_weather = weather_data['weather'][0]['description']
    mood_based_weather = get_weather_description(user_mood)

    print(f"\nFor {city}, the current weather is: {current_weather}.")
    print(f"Based on your mood ({user_mood}), today's weather is described as: {mood_based_weather}.")


if __name__ == "__main__":
    main()
