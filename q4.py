'''character_name = "Meenakshi Kumari"
character_age = 56
print("the user name is " , character_name , "and their age is " , character_age)
#problem no 1.
length = 15 
width = 8
area = length*width;
perimeter = 2* (length+width);
print("area of the rectangle:" , area)
print("perimeter of the rectangle:" , perimeter)

#problem no.2
item_count = 3;
price = 12.5;
total = item_count*price;
print("you bought", item_count , "for a total of" , total)

#problem no.3
a = int(input("Enter your number:  "));
if a>0:
    print("positive number");
elif a<0:
    print("negative number");
else:
    print("the number is zero");

#problem no.4
a = int(input("enter your number: "));
if a % 2==0:
    print("even number");
else:
    print("odd number");

#problem no.5
total_sum = 0;
for i in range(1,21):
    total_sum+=i;
print("total sum is:" , total_sum)

#problem no.6
word = "PYTHON"
reversed_word = word[::-2]
print("reversed word: " , reversed_word)

#problem no.7
numbers = [4, 1, 9, 2, 7]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
    if num>largest:
        largest = num
    if num<smallest:
        smallest = num
print("largest:", largest);
print("smallest:", smallest);

#problem no.8
text = "banana"
count = 0
for char in text:
    if char=='a':
        count += 1
print("the count of a is:", count)

#problem no.9
numbers = [10, 15, 20, 25, 30]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num;
print("sum of even numbers:", even_sum)'''

#problem no.10
nums = [1, 2, 3, 4, 5]
squared_nums = []
for num in nums:
    square = num * num
    squared_nums.append(square)
print("squared list:", squared_nums)

#challenge problem
words = ["cat", "elephant", "dog", "hippopotamus"]
num = 0
for num in words:
    if len(num)>4:
        print("greater words:", num)




