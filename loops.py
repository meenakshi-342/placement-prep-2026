'''def vowel_killer(character):
    result=""
    for char in character:
        if char.lower() in "aeiou":
            pass
        else:
            result += char
    return result

def main():
    user_input = str(input("Enter your words: "))
    user_output = vowel_killer(user_input)
    print(f"The Expected word is: {user_output}")

if __name__ == "__main__":
    main()

def main():
    menu = {
    "Boba": 5,
    "Burger": 10,
    "Pizza": 12,
    "Fries": 4
}
    total = 0
    while True:
        item = input("items: ").title()
        if item.lower() == "exit":
            break
        if item in menu:
            total += menu[item]
            print(f"Total : ${total}")

if __name__ == "__main__":
    main()

def main():
    numbers = [12, 7, 19, 24, 3, 8, 10, 15]
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    print(f"The list with only even numbers are: {evens}")

if __name__ == "__main__":
    main()

def main():
    raw_courses = ["  python ", "DATA SCIENCE", "python", "  web dev  ", "Data Science ", "   PYTHON "]
    result = []
    for course in raw_courses:
        clean_course = course.strip().title()
        if clean_course  not in result:
            result.append(clean_course)
    print(f"The clean Course : {result}")

if __name__ == "__main__":
    main()

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input provided is not an integer")

def main():
    x = get_int("what is z? ")

if __name__ == "__main__":
    main()

def get_number():
    while True:
        try:
            user_input1 = float(input("Enter numerator? "))
            user_input2 = float(input("Enter denominator? "))
            division = user_input1 / user_input2
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return division
def main():
    x = get_number()
    print(f"The result is: {x}")

if __name__ == "__main__":
    main()'''

def fuel_guage():
    while True:
        user_input = (input("What's X and Y?" ))
        try:
           X, Y = user_input.split("/")
           X = int(X)
           Y = int(Y)
           if X > Y:
               continue
           else:
               percentage = round ((X/Y)*100)
               return percentage
        except( ValueError, ZeroDivisionError):
             pass
        

        
def main():
    percentage = fuel_guage() 
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print (f"{percentage}%")
    

if __name__ == "__main__":
    main()