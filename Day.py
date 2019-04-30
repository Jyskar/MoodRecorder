class Day:
    def __init__(self, mood, d, comment):
        self.date = d
        self.mood = mood
        self.comment = comment
        self.colorGrade = int(self.mood/20)
        self.switcher = {0: (0, 0, 255), 1: (0, 75, 175), 2: (0, 135, 135), 3: (0, 175, 75), 4: (0, 255, 0),
                         5: (255, 255, 0)}
        self.color = self.switcher[self.colorGrade]


    def to_string(self):
        return "Date: " + str(self.date) + "\tMood: " + str(self.mood) + "\nComment: "+self.comment
