class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, name):
        self.name = str(name)
        return self.name
    
    def change_age(self, age):
        self.age = int(age)
        return self.age
    
    def add_track(self, track):
        self.tracks.append(str(track))
        return self.tracks
    
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods

print(Bob.name)
print(Bob.change_name("Peter"))
print(Bob.age)
print(Bob.change_age(34.5))
print(Bob.tracks)
print(Bob.add_track("UI/UX"))
print(Bob.score)
print(Bob.get_score())
