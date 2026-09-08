class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        if cm >= 100:
            cm = cm - 100
            m = m + 1

        if m >= 1000:
            m = m - 1000
            km = km + 1

        return Distance(km, m, cm)

    def __sub__(self, other):
        cm = self.cm - other.cm
        m = self.m - other.m
        km = self.km - other.km

        if cm < 0:
            cm = cm + 100
            m = m - 1

        if m < 0:
            m = m + 1000
            km = km - 1

        return Distance(km, m, cm)

    def display(self):
        print("Distance =", self.km, "km", self.m, "m", self.cm, "cm")

    def __del__(self):
        print("Destructor called")


d1 = Distance(5, 700, 80)
d2 = Distance(2, 500, 50)

d3 = d1 + d2
d3.display()

d4 = d1 - d2
d4.display()