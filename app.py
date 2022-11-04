# This program will help you memorise the whole periodic table
# and understand many aspects of it. In the end you will be able
# to get to know all of the elements and the ups and downs of all the groups
# You will also be able to understand the history behind the elements.
# Things like their appearance, state, reactivity, ores and minerals will be
# obvious to you then. Not only that, but after making use of this program,
# you will be able to really easily solve questions pertaining to the periodic table

# ~~~ Imports
import random
import csv


# temporary data to test the program
# elements = {"hydrogen": [1, 1, "gas"], "oxygen": [8, 2, "gas"]}

# Initialise the data
def loadData():
    with open("PeriodicTableofElements.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        # for i in csv_reader:
        #     print(i)
        elements = list(csv_reader)
        # print(elements)
        # print(elements, "elements")
    groups = [[] for i in range(18)]
    periods = [[] for i in range(7)]
    types = {}
    # print(elements == [])
    # print(elements)
    for element in elements:
        # print("came inside loop")
        try:
            groups[int(element["Group"])-1].append(element)
            periods[int(element["Period"])-1].append(element)
            types[element["Type"]].append(element)
        except KeyError:
            types[element["Type"]] = [element]
        except ValueError:
            pass
        except Exception as e:
            raise(e)
    return elements, groups, periods, types


elements, groups, periods, types = loadData()

# Select training program here

# Select the groups here
# groups = [groups[i-1] for i in [1, 2, 15, 16, 17]]
# Select the Element Types
# training_vals = ["Alkali Metal", "Alkaline Earth Metal", "Nonmetal", "Halogen"]
# elements = []
# for cat in training_vals:
#     elements += types[cat]

# Functions that ask questions
def askQues():
    """Asks a question"""
    element = random.choice(elements)
    case_sensitive = False
    field_name = random.choice(["Symbol", "AtomicNumber", "Period", "Group", "Type"]*2 + ["Phase"])
    if field_name == "Symbol":
        case_sensitive = True
    ans = element[field_name]
    q = f"What is the {field_name} of {element['Element']}?"
    ans_script = f"The {field_name} of {element['Element']} is {ans}."
    return ans, q, ans_script, case_sensitive

def askElementName():
    """gives some information and asks for the name of the element"""
    element = random.choice(elements)
    field_name = random.choice(["Symbol", "AtomicNumber"])
    ans = element["Element"]
    q = f"What is the name of the element whose {field_name} is {element[field_name]}?"
    ans_script = f"The element whose {field_name} is {element[field_name]} is {ans}."
    return ans, q, ans_script, False

def GroupPeriodWise():
    """Asks about elements from a group"""
    x = random.randint(0, 1)
    elems = random.choice([groups, periods][x])
    names = [i["Element"].lower() for i in elems]
    def check_ans(ans):
        ans = set(ans.split())
        if len(ans) < 3 and len(ans) < len(names):
            return False
        for i in ans:
            if i.lower() not in names:
                return False
        return True
    a = check_ans
    gp = ["Group", "Period"][x]
    q = f"List 3 or more elements from the {gp} {elems[0][gp]}"
    ans_script = f"The elements of {gp} {elems[0][gp]} are {' '.join(names)}"
    return a, q, ans_script, False


# The main function
def main():
    print("Hello and Welcome to this program. This program will "\
        "quiz you about the periodic table")
    # questions = [GroupPeriodWise]
    questions = [askQues, askElementName, GroupPeriodWise]
    while True:
        question = random.choice(questions)()
        print("-"*25)
        ans = input(question[1]+"\n--> ")
        corr_ans = question[0]
        if not question[3] and not callable(question[0]):
            ans = ans.lower()
            corr_ans = question[0].lower()
        if ans == "quit":
            break
        if callable(corr_ans):
            if corr_ans(ans):
                print(random.choice(["Awesome! Next Question!", "Nice you got this!", "Correct! Keep it going!"]))
            else:
                print(f"No no! Think think!\n{question[2]}")
        elif ans == corr_ans:
            print(random.choice(["Awesome! Next Question!", "Nice you got this!", "Correct! Keep it going!"]))
        else:
            print(f"No no! Think think!\n{question[2]}")
    print("\nThank you for using this program. Hope it was of help.")


if __name__ == "__main__":
    main()
