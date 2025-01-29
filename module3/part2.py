def main():
    # get current time in hours (24 hour time)
    current_hour = int(input('Enter current hour of the day using 24 hour time: '))
    # get wait time
    wait_hours = int(input('Enter wait time in hours: '))
    # add times together and take the modulus of 24
    alarm_time = (current_hour + wait_hours) % 24
    if alarm_time < 0:
        # adjust for negative numbers
        alarm_time += 24
    print(f'The alarm will go off at {alarm_time}.')

if __name__ == '__main__':
    main()