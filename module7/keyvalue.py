room_numbers = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}
instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}
meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}
if __name__ == '__main__':
    course_number = input("Enter course number: ")
    try:
        room_number = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]
        print(f'Room number: {room_number}')
        print(f'Instructor: {instructor}')
        print(f'Meeting time: {meeting_time}')
    except KeyError:
        # print error if any course data was missing
        print(f'Invalid course number: {course_number}')
