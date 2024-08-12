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

# import statistics

#temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# temperatures = [49, 57, 56, 55, 53]
# temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"]
temperatures = [-51, -58, -59, -52, -52, -48, -47, -53]

# sum_temperatures = 0
# list_length = len(temperatures)
# for temperature in temperatures:
#     sum_temperatures = sum_temperatures + float(temperature)
# print(sum_temperatures/list_length)

# float_temperatures = [float(temp) for temp in temperatures]
# print(statistics.mean(float_temperatures))

# def load_data_from_csv(csv_file):
#     """Reads a csv file and stores the data in a list.

#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """
#     pass
#  self.example_one = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]
#         self.example_two = [
#             ["2020-06-19T07:00:00+08:00", 47, 46],
#             ["2020-06-20T07:00:00+08:00", 51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", 52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", 48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]
#         self.example_three = [
#             ["2020-06-19T07:00:00+08:00", -47, -46],
#             ["2020-06-20T07:00:00+08:00", -51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", -52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", -48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]
from weather import load_data_from_csv
import csv

# csv_file = "./tests/data/example_one.csv"
# csv_file = "./tests/data/example_two.csv"

# # with open(csv_file, newline='') as f:
# #     reader = csv.reader(f)
# #     data = list(reader)
# #     data1 = data[1:]
# #     data2 = []
# #     for set in data1:
# #         data2.append([set[0],float(set[1]),float(set[2])])
# # print(data2)

# data = load_data_from_csv(csv_file)

# print(data)

temperatures = [49, 57, 56, 55, 53]
expected_result = (49.0, 0)

# temperatures = [-10, -8, 2, -16, 4]
# expected_result = (-16.0, 3)

# temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
# expected_result = (8.9, 3)

# temperatures = ["49", "57", "56", "55", "53", "49"]
# expected_result = (49.0, 5)

# temperatures = [49, 57, 56, 55, 53, 49]
# expected_result = (49.0, 5)
temperatures = []

from weather import find_min

print(find_min(temperatures))

# min_temperature = min(temperatures)
# list_length = len(temperatures)
# reversed_temperatures = list(reversed(temperatures))
# reverse_temp_index = reversed_temperatures.index(min_temperature)
# temp_index = len(temperatures)-1-reverse_temp_index

# print((float(min_temperature),temp_index))
                

# for temperature in list(reversed(temperatures)):
#     if temperature == min_temperature:
#         temp_index = index()
#         print(temperature, temp_index)

# for temperature, ind in enumerate(temperatures):
#     if temperature == min_temperature:
#         print(temperature)
#         print(ind)