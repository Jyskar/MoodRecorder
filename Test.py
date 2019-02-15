import Calculations
import InOut

rel = Calculations.relevant_days(InOut.read_from_file("daysGUI.txt"))
for obj in rel:
    print(obj.to_string())
