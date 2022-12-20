from classes.Schedule import Schedule

def test_schedule_valid_day():
    schedule = Schedule( day = 'MO', begin = '10:00', end = '12:00')
    assert schedule.day == 'MO'
    assert schedule.begin == '10:00'
    assert schedule.end == '12:00'

def test_schedule_wrong_day():
    schedule = Schedule( day = 'XX', begin = '40:00', end = '50:00')
    assert schedule.day == None
    # Todo: Validate format of hours
    assert schedule.begin == '40:00'
    assert schedule.end == '50:00'