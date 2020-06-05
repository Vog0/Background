from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

data = YahooWeather(APP_ID="lMa5T450",
                     api_key="dj0yJmk9SE03emFqS3haUlREJmQ9WVdrOWJFMWhOVlEwTlRBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTEw",
                     api_secret="f53bd8f7a002286ccf8b8a986426f6ecbf24bcb0")

data.get_yahoo_weather_by_city("vienna", Unit.celsius)
print(data.condition.text)
print(data.condition.temperature)

data.get_yahoo_weather_by_location(35.67194, 51.424438)
print(data.condition.text)
print(data.condition.temperature)

data.get_forecasts()[1]
print(data.get_forecasts()[1].as_dict())