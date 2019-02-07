from tkinter import *
import datetime
import InOut
import Calculations

# check if today has already been registered
entry_today = FALSE
current_day = InOut.Day(50, datetime.date.today().strftime('%d-%m-%y'), "")
list_of_days = InOut.read_from_file("daysGUI.txt")
if list_of_days[len(list_of_days)-1].date == datetime.date.today().strftime('%d-%m-%y'):
    entry_today = TRUE
    current_day = list_of_days[len(list_of_days)-1]

# window params
window = Tk()
window.title("Mood GUI")
window.minsize(500, 465)
window.maxsize(500, 465)

# frames
f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)

# elements such as labels and entries
l1 = Label(f1, text="   Mood(1-100):\t")
l2 = Label(f2, text="   Comment:\t")
l3 = Label(f3, text="\t\tPress send to save today's entry")
e1 = Entry(f1)
t1 = Text(f2, width=50, wrap=WORD)
sb = Scrollbar(f2, orient=VERTICAL, command=t1.yview)
sb.pack(side=RIGHT, fill=Y)
t1['yscrollcommand'] = sb.set

if entry_today:
    e1.config(state='disabled')
    t1.insert("0.0", "You've already registered a mood today. If you wish to modify it press, EDIT.")
    t1.config(state='disabled')
    l3.config(text="\t\tPress edit to modify today's entry.")


# Gets info from entry and the text area and instantiates an saves a new day into a file
def send():
    global entry_today
    try:
        mood = int(e1.get())
    except ValueError:
        print("Mood needs to be a real number from 0-100.")
        e1.delete(0, END)

    if int(mood) > 100:
        mood = "100"
    if int(mood) < 0:
        mood = "0"
    today = InOut.Day(mood, datetime.date.today().strftime('%d-%m-%y').replace(",", ""),
                      t1.get("0.0", END).replace('\n', " "))  # remove \n in textArea for storage in file.

    if entry_today:
        list_of_days[len(list_of_days)-1] = today
        InOut.writeList("daysGUI.txt", list_of_days)
    else:
        InOut.add_today_to_file("daysGUI.txt", today)

    entry_today = TRUE
    e1.config(state="readonly")
    t1.config(state="disabled")
    b2.config(state="normal")
    l3.config(text="\t\tSaved today's entry correctly.\n \t\t   If you wish to edit it  press EDIT.")


b2 = Button(f3, text="EDIT")


def edit():
    if entry_today:
        e1.config(state='normal')
        e1.delete(0, END)
        e1.insert(0, current_day.mood)
        t1.config(state='normal')
        t1.delete("0.0", END)
        t1.insert("0.0", current_day.comment)
        b2.config(state='disabled')
        l3.config(text="")


def calc():
    global list_of_days
    list_of_days = InOut.read_from_file("daysGUI.txt")
    string = Calculations.calculate_max_and_average(list_of_days)
    t1.config(state="normal")
    t1.delete("0.0", END)
    t1.insert("0.0", string)
    t1.config(state="disabled")


b1 = Button(f3, text="SEND", command=send)
b3 = Button(window, text="STATS", command=calc)
b2.config(command=edit)
# pack elements
l1.pack(side=LEFT)
l2.pack(side=LEFT, anchor=N)
e1.pack(side=LEFT, fill=X)
b1.pack(side=RIGHT, anchor="se")
b2.pack(side=RIGHT, anchor="se")
l3.pack(anchor="ne", side=LEFT)
t1.pack(side=LEFT, fill=BOTH)
b3.pack(anchor="e", side=BOTTOM)

# pack frames
f1.pack(anchor=W, fill=BOTH)
f2.pack(anchor=W)
f3.pack(anchor=S, fill=BOTH)
# main loop
window.mainloop()
