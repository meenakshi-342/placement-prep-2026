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
    main()'''

def main():
    numbers = [12, 7, 19, 24, 3, 8, 10, 15]
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    print(f"The list with only even numbers are: {evens}")

if __name__ == "__main__":
    main()

