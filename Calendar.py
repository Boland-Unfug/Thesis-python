class Day:

    def __init__(self, day, day_name):
        self.day = day
        self.day_name = day_name
        self.note = None

    def get_day(self):
        return self.day # 1, 2, 3, etc.

    def get_day_name(self):
        return self.day_name # Monday, Tuesday, etc.

    def get_note():
        return self.note

    def set_note():
        self.note = note


class Week:
    def __init__(self):
        self.days = [None]*7

    def get_day(self, day):
        return self.days[day]

    def set_day(self, day, day_name):
        self.days[day] = Day(day, day_name)

    def add_day(self, day):
        self.days.append(day)

class Month:
    def __init__(self):
        self.weeks = [Week() for _ in range(4)]  # Assuming 4 weeks in a month

class Note:
    def __init__(self, note):
        self.note = note
    
    def get_note():
        return self.note

    def set_note():
        self.note = note

# Write some test code here to test your classes


monday = Day(1, "Monday")
print(Day.get_day())
print(Day.get_day_name())
tuesday = Day(2, "Tuesday")
wednesday = Day(3, "Wednesday")
thursday = Day(4, "Thursday")
friday = Day(5, "Friday")
saturday = Day(6, "Saturday")
sunday = Day(7, "Sunday")

week = Week()
week.set_day(monday)
week.set_day(tuesday)
week.set_day(wednesday)
week.set_day(thursday)
week.set_day(friday)
week.set_day(saturday)
week.set_day(sunday)


Month = Month()

