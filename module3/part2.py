"""
1. Asks the user for the current time of day as an integer using 24-hour time, as follows:
  - An input of 0 is equivalent to 12 AM (midnight)
  - An input between 1 and 11, inclusive, represents an AM time, e.g. 1 is 1 AM
  - An input of 12 is equivalent 12 PM (noon).
  - An input between 13 and 23, inclusive, represents a PM time, offset by 12, e.g. 13 is 1 PM
  - Inputs greater than 23 are equivalent to a 24-hour time of the input modulo 24.
    For example, an input of 24 is equivalent to 24 % 24 = 0 (midnight),
    and an input of 30 is equivalent to 30 % 24 = 6 (6 am).
  - Negative inputs are equivalent to the 24-hour time with the same modulo 24,
    plus 24. For example, -1 is equivalent to 23 (-1 % 24 + 24 = -1 + 24 = 23)
  - These adjustments are not performed until the final step.
2. Ask the user for the number of hours to wait. This can be any integer value,
   including negative values.
3. The alarm time is calculated as the sum of the current time and the wait time, modulo 24.
   If the final result is negative, it is converted into a positive number by adding 24.
   This results in a number between 0 and 23, inclusive, representing standard 24-hour time:
  - An value of 0 is midnight
  - An value between 1 and 12, inclusive, represents an AM time, e.g. 1 is 1 AM
  - An value between 13 and 23, inclusive, represents a PM time, offset by 12, e.g. 13 is 1 PM
4. The alarm time is printed
"""
def main():
    # get current time in hours (24 hour time)
    current_hour = int(input('Enter current hour of the day using 24 hour time: '))
    # get wait time
    wait_hours = int(input('Enter wait time in hours: '))
    # add times together, modulo 24
    alarm_time = (current_hour + wait_hours) % 24
    if alarm_time < 0:
        # adjust for negative numbers by adding
        alarm_time += 24
    print(f'The alarm will go off at {alarm_time}.')

if __name__ == '__main__':
    main()