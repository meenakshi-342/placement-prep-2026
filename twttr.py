def shorten(word):
    result=""
    for char in word:
        if char.lower() in "aeiou":
            pass
        else:
            result += char
    return result

def main():
    user_input = str(input("Enter your words: "))
    user_output = shorten(user_input)
    print(f"Output: {user_output}")

if __name__ == "__main__":
    main()