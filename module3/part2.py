def get_hours(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            pass # repeat prompt

def main():
    # get current time in hours (24 hour time)
    current_hour = get_hours('Enter current hour of the day using 24 hour time: ')
    # get wait time
    wait_hours = get_hours('Enter wait time in hours: ')
    alarm_time = (current_hour + wait_hours) % 24
    if alarm_time < 0:
        alarm_time += 24
    print(f'The alarm will go off at {alarm_time}.')

if __name__ == '__main__':
    main()