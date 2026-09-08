'''def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    return float(hour + (minute / 60.0))
def main():
    user_input = input("enter time: ")
    clean_input = user_input.strip()
    time = convert(clean_input)
    if 7.0 <= time <= 8.0:
        print("BREAKFAST")
    elif 12.0 <= time <= 13.0:
        print("LUNCH")
    elif 18.0 <= time <= 19.0:
        print("DINNER")
    else:
        print("not eating time")

    
if __name__=="__main__":
    main()

def is_leap_year(year):
    if (year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
        return (True)
    else:
        return (False)

def main():
    your_year = int(input("Enter your year: "))
    value = is_leap_year(your_year)
    print(f"The year prompted is {value}")
if __name__=="__main__":
    main( )


def evaluate_roots(a, b, c):
   if a==0:
      return "Not a real quadratic equation"
   D = (b**2)-4*a*c
   if D > 0:
      return "Two distinct real roots"
   if D == 0:
      return "One real root (repeated)"
   if D < 0:
      return "Complex (imaginary) roots"

def main():
   a = float(input("Enter a: "))
   b = float(input("Enter b: "))
   c = float(input("Enter c: "))
   results = evaluate_roots(a, b, c)
   print(f"The results of the equations are {results}")
if __name__=="__main__":
   main()'''

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 5 == 0 and n % 3 !=0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return "BOHOO!!"

def main():
    n = int(input("Enter your number: "))
    value = fizz_buzz(n)
    print(f"The number you gave is {value}!!")

if __name__ == "__main__":
    main()