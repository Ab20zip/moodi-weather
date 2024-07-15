mood_to_weather = {
    'happy': 'sunny',
    'sad': 'rainy',
    'excited': 'stormy',
    'calm': 'clear',
    'anxious': 'cloudy',
    'romantic': 'partly cloudy',
    'energetic': 'windy',
    'peaceful': 'foggy',
    'nostalgic': 'misty',
    'playful': 'showers',
    'grateful': 'warm',
    'hopeful': 'cool',
    'confident': 'dry',
    'inspired': 'breezy',
    'reflective': 'chilly',
    'motivated': 'hot',
    'curious': 'cold',
    'relaxed': 'thunderstorms',
    'optimistic': 'overcast',
    'joyful': 'humid'
}


def get_weather_description(mood):
    return mood_to_weather.get(mood, 'neutral')
