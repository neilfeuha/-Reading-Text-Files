from unicodedata import name


class Student:
    track = []
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score

    def Introduce_self(self):
        print('hi', self.name, "you are", self.age,'years old. You are in the', self.track, 'and your score was', self.score)

    def change_name(self, name):
        self.name = name
        print("Hi. I am", self.name)

    def change_age(self, age):
        self.age = age
        print("I am", self.age)

    def add_track(self, track):
        self.track = track
        print("I am now in", self.track)

    def get_score(self):
        #self.score = score
        print("I obtained", self.score, "marks")


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

Bob.Introduce_self()

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

