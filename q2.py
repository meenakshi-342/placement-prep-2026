'''def camel_to_snake(text):
    result = ""
    for char in text:
        if char.isupper() :
            result = result + "_" + char.lower( )
        else:
            result += char
    return result

def main():
    user_input = str(input("Enter camel_case: "))
    user_output = camel_to_snake(user_input)
    print(f"snake_case: {user_output}")

if __name__ == "__main__":
    main()

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    while True:
        try:
            item = input("Enter your order: ").title()
            if item in menu:
                total += menu[item]
                print(f"total: ${total:.2f}")
        except EOFError:
            pass
            break

if __name__ == "__main__":
    main()

def main():
    grocery_list ={}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print()
            for item in sorted(grocery_list):
                count = grocery_list[item]
                print(f"{count}{item}")
            break
if __name__ == "__main__":
    main()

def main():
    months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
    while True:
        try:
            user_input = input("Date: ").strip()
            if "/" in user_input:
                month, day, year = user_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in user_input:               
                month_and_day , year = user_input.split(",")
                month_name , day = month_and_day.split(" ")
                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int(year)
            else:
                continue
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                
            break
        except (ValueError, KeyError, IndexError):
            pass

if __name__ == "__main__":
    main()'''

def main():
    haha = []
    while True:
        try:
            user_input = input().strip().title()
            haha.append(user_input)
        except (EOFError):
            pass
        
    print(f"The haha you want in life is: {haha}")
        
if __name__ == "__main__":
    main()
        

