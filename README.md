# MoodiWeather

MoodiWeather is an innovative weather application that provides personalized weather forecasts based on the user’s mood. By blending meteorological data with emotional insights, MoodiWeather delivers a unique and engaging weather experience tailored just for you.

## Features

- **Personalized Weather Descriptions:** Receive weather forecasts with descriptions that resonate with your current mood.
- **Mood Detection:** Input your mood manually or use sentiment analysis on your text to detect your mood.
- **Wide Range of Moods:** Supports a variety of moods, each mapped to specific weather descriptions.
- **User-Friendly Interface:** Simple and intuitive interface for easy mood input and weather forecast retrieval.

## Mood-to-Weather Mappings

MoodiWeather includes a diverse set of mood-to-weather mappings:

- **Happy:** Sunny
- **Sad:** Rainy
- **Excited:** Stormy
- **Calm:** Clear
- **Anxious:** Cloudy
- **Romantic:** Partly Cloudy
- **Energetic:** Windy
- **Peaceful:** Foggy
- **Nostalgic:** Misty
- **Playful:** Showers
- **Grateful:** Warm
- **Hopeful:** Cool
- **Confident:** Dry
- **Inspired:** Breezy
- **Reflective:** Chilly
- **Motivated:** Hot
- **Curious:** Cold
- **Relaxed:** Thunderstorms
- **Optimistic:** Overcast
- **Joyful:** Humid

## Getting Started

### Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

### Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/Ab20zip/moodi-weather.git
   cd moodi-weather
    ```

2. Install required dependencies:
    ```bash
   Copy code
   pip install -r requirements.txt
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) and set it in the config.py file:
    ```python
   # config.py
   API_KEY = 'your_api_key_here'
    ```
   
# Usage

1. Run the application:
    ```bash
   python moodiweather.py
    ```

2. Input your location and mood when prompted.

3. Receive your personalized weather forecast!

# License

This project, "MoodiWeather" is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

<!-- MADE WITH ❤️ BY Ab20zip -->
