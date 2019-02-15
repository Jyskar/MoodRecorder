from Day import Day


# Writes the hole file again// NOT EFFICIENT AT ALL
def write_list(name, l):
    file = open(name, "w+")
    for day in l:
        file.write(str(day.mood)+","+str(day.date)+","+day.comment)
    file.close()


# Adds a day to the file
def add_today_to_file(filename, today_day):
    file = open(filename, "a")
    file.write("\n"+str(today_day.mood)+","+str(today_day.date)+","+today_day.comment)
    file.close()


# Reads from file the past days and puts them on a list
def read_from_file(filename):
    file = open(filename, "r+")
    list1 = []
    for line in file:
        parts = line.split(",", 2)
        list1.append(Day(int(parts[0]), parts[1], parts[2]))
    file.close()
    return list1
