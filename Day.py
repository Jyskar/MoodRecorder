class Day:
    def __init__(self, mood, d, comment):
        self.date = d
        self.mood = mood
        self.comment = comment

    def to_string(self):
        return "Date: " + str(self.date) + "\tMood: " + str(self.mood) + "\nComment: "+self.comment
