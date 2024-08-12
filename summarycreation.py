from weather import convert_date, convert_f_to_c, format_temperature, calculate_mean, load_data_from_csv, find_min, find_max


# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

example_one = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

# number_of_days = len(example_one)

# days=[]
# min_temperatures = []
# max_temperatures = []

# for day in example_one:
#     days.append(day[0])
#     min_temperatures.append(day[1])
#     max_temperatures.append(day[2])

# minimums = find_min(min_temperatures)
# maximums = find_max(max_temperatures)
# print(f"The lowest temperature will be {format_temperature(convert_f_to_c(minimums[0]))}, and it will occur on {convert_date(days[minimums[1]])}.")

# print(f"{number_of_days } Day Overview\n\
# \tThe lowest temperature will be {format_temperature(convert_f_to_c(minimums[0]))}, and will occur on {convert_date(days[minimums[1]])}.\n\
# \tThe highest temperature will be {format_temperature(convert_f_to_c(maximums[0]))}, and will occur on {convert_date(days[maximums[1]])}.\n\
# \tThe average low this week will be {format_temperature(convert_f_to_c(calculate_mean(min_temperatures)))}.\n\
# \tThe average high this week will be {format_temperature(convert_f_to_c(calculate_mean(max_temperatures)))}.")

from weather import generate_summary

frog = generate_summary(example_one)
print(frog)