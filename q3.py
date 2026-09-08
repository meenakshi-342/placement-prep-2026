'''def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount due: ", amount_due)
        coin = int(input("insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due = amount_due - coin
    print(f"change owed: {abs(amount_due)}")

if __name__ =="__main__":
    main()

def main():
    text = "data"
    result = ""
    for char in text:
       result = char + result
    print(f"The reversed text is: {result}")
if __name__ =="__main__":
    main()

def main():
    sentence = "banana"
    counts = {}
    for char in sentence:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(f"{counts}")

if __name__ =="__main__":
    main()'''

def main():
    inventory = {
    "apples": 50,
    "bananas": 4,
    "cherries": 15,
    "dates": 2,
    "elderberries": 0
}
    
    reorder_list = []
    for  items , count in inventory.items():
        Count: {count}
        if  count < 10:
            reorder_list.append(items)
    print(f"the stock list is: {reorder_list}")
if __name__ =="__main__":
    main()



