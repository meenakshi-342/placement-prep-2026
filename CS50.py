#CS50 problem 1
'''def calculate_bill(meal_cost, tip_percentage, guests):
    tip_amount = meal_cost*(tip_percentage/100)
    total_bill = meal_cost + tip_amount
    cost_per_guest = total_bill / guests
    return round(cost_per_guest, 2)

def main():
    meal = float(input("Cost of the Meal: "))
    tip = float(input("Tip percentage (as of 15%=15): "))
    people = int(input("Total no. of people: "))
    per_person = calculate_bill(meal, tip, people)
    print(f"Cost per Person is: ${per_person}")

if __name__ == "__main__":
    main()

#CS50 problem 2
def convert_time(time_str):
    time_part, period = time_str.split()
    hour, minute = time_part.split(":")
    hour = int(hour)
 
    if period == "AM" and hour == 12:
        hour == 0
    if period == "PM" and hour != 12:
        hour += 12
    return(f"{hour:2d}:{minute}")

def main():
    user_time = input("enter your time: ")
    print(convert_time(user_time))

if __name__ == "__main__":
    main()

#CS50P problem 3
def calculate_energy(mass):
    c = 3000000000
    E = mass * (c**2)
    return E
def main():
    mass = int(input("Enter m: "))
    energy = calculate_energy(mass)
    print(f"E:{energy} Joules")
if __name__ == "__main__":
    main()

#CS50 problem 4
def is_answer(user_input):
    user_input = user_input.strip().lower()
    if user_input in ["forty-two" , "forty two" , "42"]:
        return True
    else:
        return False
def main():
    num = input("the Answer to the Ultimate Question of Life, the Universe, and Everything: ")
    if is_answer(num):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()'''

#CS50 PROBLEM 5
def check_eligibility(grades, attendance):
    if attendance < 75:
        return ("Ineligible due to low attendance")
    elif grades >= 90:
        return ("Grade: A")
    elif grades >= 80:
        return ("Grade: B")
    elif grades >= 70:
        return ("Grade: C")
    else:
        return ("Grade: F")
def main():
    marks = int(input("enter your marks: "))
    present = int(input("enter your attendance: "))
    value = check_eligibility(marks, present)
    print(f"Result:{value}")
if __name__ == "__main__":
    main()
