import datetime

coffee_menu = {
    "1": ["Espresso", 85],
    "2": ["Americano", 85],
    "3": ["Cafe Latte", 100],
    "4": ["Cappuccino", 110],
    "5": ["Mocha", 100],
    "6": ["Caramel Macchiato", 130]
    }

coffee_list = []
coffee_price = []

def user_login():
    print("Please Login".center(50, "-"))
    user_name = input("Input Name : ")
    user_password = input("Input Password : ")
    while True:
        if user_name == "admin1" and user_password == "1234":
            print("Welcome admin :", user_name)
            print("Please Select Coffee Menu".center(50, "-"))
            return True
        else:
            print("Username or Password that you've entered is incorrect!!")
            return user_login()

def coffee_menu_list():
    print("1", coffee_menu["1"][0], "price", coffee_menu["1"][1], "baht")
    print("2", coffee_menu["2"][0], "price", coffee_menu["2"][1], "baht")
    print("3", coffee_menu["3"][0], "price", coffee_menu["3"][1], "baht")
    print("4", coffee_menu["4"][0], "price", coffee_menu["4"][1], "baht")
    print("5", coffee_menu["5"][0], "price", coffee_menu["5"][1], "baht")
    print("6", coffee_menu["6"][0], "price", coffee_menu["6"][1], "baht")
    print("(Enter 0 for bill)".center(50, "-"))
    while True:
        coffee_number = input("Please Enter Menu :")
        if (coffee_number == "0"):
            print("exit")
            break
        else:
            coffee_list.append(coffee_menu[coffee_number])
            coffee_price.append(coffee_menu[coffee_number][1])

def show_bill():
    print("Coffee House".center(50, "-"))
    for number in range(len(coffee_list)):
        print(coffee_list[number][0]," price ".center(20,"."), coffee_list[number][1], "baht")
    return True

def vat_totalPrice():
    summary = sum(coffee_price)
    vat = summary*7/100
    total_result = summary + vat
    print("-".center(50, "-"))
    print("Summary price : ", summary, "baht")
    print("Vat 7% : ", vat)
    print("Total price : ", total_result, "baht")
    print("(Include Service Charge)")
    print("Thank you".center(50, "-"))

def bill_date():
    x = datetime.datetime.now()
    print(x.strftime("%d/%m/%Y, %H:%M:%S"))

user_login()
coffee_menu_list()
show_bill()
vat_totalPrice()
bill_date()