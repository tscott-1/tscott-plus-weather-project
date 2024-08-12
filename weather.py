import csv
from datetime import datetime
# import statistics

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    datestr=datetime.fromisoformat(iso_string)
    return f"{datestr.strftime("%A")} {datestr.strftime("%d")} {datestr.strftime("%B")} {datestr.strftime("%Y")}"



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_c =(float(temp_in_fahrenheit) - 32) * 5/9
    return round(temp_in_c,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum_temperatures = 0
    list_length = len(weather_data)
    for temperature in weather_data:
        sum_temperatures = sum_temperatures + float(temperature)
    # print(sum_temperatures/list_length)
    list_length = len(weather_data)

    return sum_temperatures/list_length
    # temperatures = [float(temperature) for temperature in weather_data]
    # return(statistics.mean(temperatures))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data1 = filter(None,data[1:])
        print(data1)
        data2 = []
        for set in data1:
         data2.append([set[0],float(set[1]),float(set[2])])
    return data2


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    else:
        temperatures = [float(temp) for temp in weather_data]
        min_temperature = float(min(temperatures))
        reversed_temperatures = list(reversed(temperatures))
        reverse_temp_index = reversed_temperatures.index(min_temperature)
        temp_index = len(weather_data)-1-reverse_temp_index
        return (min_temperature,temp_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    else:
        temperatures = [float(temp) for temp in weather_data]
        min_temperature = float(max(temperatures))
        reversed_temperatures = list(reversed(temperatures))
        reverse_temp_index = reversed_temperatures.index(min_temperature)
        temp_index = len(weather_data)-1-reverse_temp_index
        return (min_temperature,temp_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    number_of_days = len(weather_data)

    days=[]
    min_temperatures = []
    max_temperatures = []

    #break the nested list into 3 separate lists for days minimum temps and maximum temps
    for day in weather_data:
        days.append(day[0])
        min_temperatures.append(day[1])
        max_temperatures.append(day[2])

    minimums = find_min(min_temperatures)
    maximums = find_max(max_temperatures)


    output = f"{number_of_days } Day Overview\n\
  The lowest temperature will be {format_temperature(convert_f_to_c(minimums[0]))}, and will occur on {convert_date(days[minimums[1]])}.\n\
  The highest temperature will be {format_temperature(convert_f_to_c(maximums[0]))}, and will occur on {convert_date(days[maximums[1]])}.\n\
  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_temperatures)))}.\n\
  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(max_temperatures)))}.\n"
    # print(output)
    return output


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary_string = ""
    for day in weather_data:
        summary_string = (summary_string + f"---- {convert_date(day[0])} ----\n\
  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}\n\
  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}\n\n")
    return(summary_string)
