class Day:
    def __init__(self, mood, d, comment):
        self.date = d
        self.mood = mood
        self.comment = comment


# Calculates and prints some info on the days so far
def calculate_max_and_average(list_days):
    max_mood = Day(0, "01-01-10", "Shat ma self")
    worst_mood = Day(500000, "01-01-10", "Shat ma self")
    counter = 0
    sum_of_moods = 0
    for d in list_days:
        if d.mood > max_mood.mood:
            max_mood = d

        if d.mood < worst_mood.mood:
            worst_mood = d

        sum_of_moods += d.mood
        counter += 1
    average_mood = sum_of_moods/counter
    return "===================STATS==================="+"\nBEST MOOD\nDay: " + max_mood.date + "\tMood: " \
           + str(max_mood.mood) + "\nComment of that day: " + max_mood.comment+"\nWORST MOOD\nDay: "\
           + worst_mood.date + "\tMood: " + str(worst_mood.mood) + "\nComment of that day: "\
           + worst_mood.comment + "\nAVERAGE MOOD: "+str(average_mood)

