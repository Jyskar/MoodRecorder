import datetime


class Day:
    def __init__(self, mood, d, comment):
        self.date = d
        self.mood = mood
        self.comment = comment


# Adds a day to the file
def add_today_to_file(filename, today_day):
    file = open(filename, "a")
    file.write("\n"+today_day.mood+","+today_day.date+","+today_day.comment)
    file.close()


print("===========================================================================")
print("== Rank your mood from 1-100 and please explain why in the comment.      ==")
print("===========================================================================")
# Instantiate today, replace commas in first to fields to avoid incorrect splits
current_mood = input("Today's mood:").replace(",", "")
if int(current_mood) > 100:
    current_mood = "100"
if int(current_mood) < 0:
    current_mood = "0"
today = Day(current_mood,
            datetime.date.today().strftime('%d-%m-%y').replace(",", ""),
            input("Care to comment on your mood:"))

add_today_to_file("days.txt", today)
