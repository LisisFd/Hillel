class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s
        if self.hours not in range(0, 24):
            self.hours = 23
        if self.minutes not in range(0, 60):
            self.minutes = 59
        if self.seconds not in range(0, 60):
            self.seconds = 59

    @property
    def hours(self):
        return self.hours

    @hours.setter
    def hours(self, time_value):
        self.hours = Time(h=time_value)

    @property
    def minutes(self):
        return self.minutes

    @minutes.setter
    def minutes(self, time_value):
        self.minutes = Time(m=time_value)

    @property
    def seconds(self):
        return self.seconds

    @seconds.setter
    def seconds(self, time_value):
        self.seconds = Time(s=time_value)

    def __repr__(self):
        return f"Time: {[self.hours, self.minutes, self.seconds]}"

    def __str__(self):
        return f"Time: {self.hours, self.minutes, self.seconds}"
