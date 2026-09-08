def camel_to_snake(text):
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

