# from datetime import datetime

# date = "2021-07-05T07:00:00+08:00"
#         # expected_result = "Monday 05 July 2021"
#         # result = weather.convert_date(date)

# datestr=datetime.fromisoformat(date)
# print(f"{datestr.strftime("%A")} {datestr.strftime("%d")} {datestr.strftime("%B")} {datestr.strftime("%Y")}")
 
# 
# 
#     
# def convert_f_to_c(temp_in_fahrenheit):
#     """Converts a temperature from Fahrenheit to Celcius.

#     Args:
#         temp_in_fahrenheit: float representing a temperature.
#     Returns:
#         A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
#     """
# temp_in_f = 90
#         expected_result = 32.2
#         result = weather.convert_f_to_c(temp_in_f)
#         self.assertEqual(result, expected_result)

#     def test_convert_f_to_c_negative(self):
#         temp_in_f = -10
#         expected_result = -23.3

# temp_in_farenheit = -10

# temp_in_c =(float(temp_in_farenheit) - 32) * 5/9
# print(round(temp_in_c,1))


# def calculate_mean(weather_data):
#     """Calculates the mean value from a list of numbers.

#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     """
#     pass

import statistics

#temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# temperatures = [49, 57, 56, 55, 53]
# temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"]
temperatures = [-51, -58, -59, -52, -52, -48, -47, -53]

float_temperatures = [float(temp) for temp in temperatures]
print(statistics.mean(float_temperatures))