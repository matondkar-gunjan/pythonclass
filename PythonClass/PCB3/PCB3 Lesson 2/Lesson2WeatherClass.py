class Weather:
      def __init__(self, temperature, condition, wind_speed):
            self.temperature = temperature
            self.condition = condition
            self.wind_speed = wind_speed
      def describe(self):
            print("Temperature:", self.temperature, "°C")
            print("Condition:", self.condition)
            print("Wind speed:", self.wind_speed, "km/h")
      def is_suitable_for_outdoor_activities(self):
            if self.temperature <= 30 and self.condition == "Clear" and self.wind_speed < 20:
                  print("The weather is suitable for outdoor activities")
            else:
                  print("The weather is not suitable for outdoor activities")
weather1 = Weather(25, "Clear", 10)
weather2 = Weather(10, "Rainy", 20)
weather3 = Weather(28, "Clear", 25)

weather1.describe()
weather1.is_suitable_for_outdoor_activities()
weather2.describe()
weather2.is_suitable_for_outdoor_activities()
weather3.describe()
weather3.is_suitable_for_outdoor_activities()
