class society:
    Live = "America"
    def __init__(self, name, age, live):
        self.name = name
        self.age = age
        self.live = live
    def get_name(self):
        # return self.name
        pass
    def get_info(self):
        info = f"His name is {self.name}\nhe's age is {self.age}\nHe is live in {self.live}"
        print(info)


A1 = society("Jack", 80, "Newyork")
print(A1.Live)
print(A1.get_name())
print(A1.get_info())

