from Day import Day


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
    return "==================STATS=================="+"\nBEST MOOD\nDay: " + max_mood.date + "\tMood: " \
           + str(max_mood.mood) + "\nComment of that day: " + max_mood.comment+"\nWORST MOOD\nDay: "\
           + worst_mood.date + "\tMood: " + str(worst_mood.mood) + "\nComment of that day: "\
           + worst_mood.comment + "\nAVERAGE MOOD: "+str(average_mood)


# ======================================================================================================================
# ===                                                                                                                ===
# ===                                 FUNCTIONS TREATING COMMENTS                                                    ===
# ===                                                                                                                ===
# ======================================================================================================================

# Splits de comment from each line ignoring the date and mood
def tokenize(line):
    if line is not None:
        words = line[12:].replace("'", " ").lower().split()
        return words
    else:
        return None


# Maps the appearance of words through the comments of a file
# Needs a file name to read from
# returns a hash map of the words in the comments sorted from most to least appearances
def words_map(filename):
    f = open(filename, "r+")
    file = f.read()
    lis = file.split("\n")
    h_map = {}

    for line in lis:
        words = tokenize(line)
        if words is not None:
            for ele in words:
                word = ele.replace(",", "")
                word = word.replace(".", "")
                if word == "t":
                    word = "not"
                if word in h_map:
                    h_map[word] = h_map[word]+1
                else:
                    h_map[word] = 1
    f.close()
    return h_map


# Sorts hash_map depending of value assigned to key form bigger to smaller
# returns a list of tuples with key and value
def sort_map(hash_map):
    sorted_by_value = sorted(hash_map.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_by_value


# Returns the total number of words in the comments
def reduce_words(hash_map):
    count = 0
    for x in hash_map:
        count += hash_map[x]

    return count


def relevant_days(list_of_days):
    relevant = []
    for day in list_of_days:
        if day.mood > 85 or day.mood < 30 and len(day.comment) > 50:
            relevant.append(day)
    cadena = ""
    for obj in relevant:
        cadena += obj.to_string()

    return cadena
