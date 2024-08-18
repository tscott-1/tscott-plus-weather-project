import csv
from datetime import datetime
# import statistics

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

    ##format Temperature:
    # """Takes a temperature and returns it in string format with the degrees
    #     and Celcius symbols.
    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees Celcius."
    # """

def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"

    # convert_date
    # """Converts and ISO formatted date into a human-readable format.
    # Args:
    #     iso_string: An ISO date string.
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """

def convert_date(iso_string):
    datestr=datetime.fromisoformat(iso_string)
    return datestr.strftime("%A %d %B %Y")

    # convert_f_to_c
    # """Converts a temperature from Fahrenheit to Celcius.
    # Args:
    #     temp_in_fahrenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    # """

def convert_f_to_c(temp_in_fahrenheit):
    temp_in_c =(float(temp_in_fahrenheit) - 32) * 5/9
    return round(temp_in_c,1)

    # calculate_mean
    # """Calculates the mean value from a list of numbers.
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """

def calculate_mean(weather_data):
    return sum([float(temperature) for temperature in weather_data]) / len(weather_data)

    # load_data_from_csv
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """

def load_data_from_csv(csv_file):
    with open(csv_file) as file:
        dictreader = csv.DictReader(file)
        weather_floats = []
        for row in dictreader:
            weather_floats.append([row["date"],float(row["min"]),float(row["max"])])
    return weather_floats

    
    # find_last_value_in_list
    # """creating a function to find the index of the last occurence of a number in a list to be used in max and min functions - returns an integer of the index"""

def find_last_value_in_list(input_list,value):
    if not input_list:
        return None
    if not value:
        return None
    #reverse the order of the list
    reversed_list = list(reversed(input_list))
    #find the index of the first value occurence in the reversed list
    reverse_list_index = reversed_list.index(value)
    #calculate the index in the original list using length of the list - 1 - the index of the reversed list minimum
    return len(input_list) - 1 - reverse_list_index
    
    
    # find_min
    # """Calculates the minimum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    # """


def find_min(weather_data):
    if not weather_data:
        return ()
    else:
        #create a new list temperatures looping through each temperature in the list and converting to float
        temperatures = [float(temp) for temp in weather_data]
        min_temperature = float(min(temperatures))
        return (min_temperature,find_last_value_in_list(temperatures,min_temperature))


    # find_max
    # """Calculates the maximum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    # """

def find_max(weather_data):
    if not weather_data:
        return ()
    else:
        temperatures = [float(temp) for temp in weather_data]
        max_temperature = float(max(temperatures))
    return (max_temperature,find_last_value_in_list(temperatures,max_temperature))



    # generate_summary    
    # """Outputs a summary for the given weather data.
    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

def generate_summary(weather_data):
    number_of_days = len(weather_data)
    #create empty lists to store each group of data needed for this process
    days=[]
    min_temperatures = []
    max_temperatures = []

    #loop through each nested list
    #break each nested list into 3 separate lists for days minimum temps and maximum temps
    for line in weather_data:
        day = line[0]
        min = line[1]
        max = line[2]
        days.append(day)
        min_temperatures.append(min)
        max_temperatures.append(max)

    #use functions to pull out min and max temperatures with the index which can then be used to pull out the corresponding day
    minimums = find_min(min_temperatures)
    maximums = find_max(max_temperatures)

    return(     
        f"{number_of_days } Day Overview\n"
        f"  The lowest temperature will be {format_temperature(convert_f_to_c(minimums[0]))}, and will occur on {convert_date(days[minimums[1]])}.\n"
        f"  The highest temperature will be {format_temperature(convert_f_to_c(maximums[0]))}, and will occur on {convert_date(days[maximums[1]])}.\n"
        f"  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_temperatures)))}.\n"
        f"  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(max_temperatures)))}.\n"
    )


    # generate_daily_summary
    #     """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

def generate_daily_summary(weather_data):
    summary_string = ""
    for day in weather_data:
        summary_string += (
            f"---- {convert_date(day[0])} ----\n"
            f"  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}\n"
            f"  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}\n\n"
        )
    return(summary_string)
