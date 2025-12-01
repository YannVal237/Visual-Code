users={}
def registeraccount():
    username=input("enter the name:")
    if username in users:
        print("username already exist")
        return
    password=input("enter 5-digits personnal numbers: ")
    if not password.isdigit() or len(password)<5:
        print("password is invalid")
        return  
    users[username]= {"password":password , "balance":0 , "transactions":[]}
    print("the account created with success")
def log_a_user():
    print("DOWNLOAD")
    username=input("enter the name of the users: ")
    password=input("Password: ")
    if username in users and users[username]["password"]== password:
        print("downlaod successfully")
        return username 
    else:
        print("username or password are not accepted")
        return None 
def Balance(username):
    print("BALANCE")
    balance= users[username]["balance"]
    print(f"your balance is: {balance} FCFA")
    users[username]["transactions"].append(f"Check balance: {balance} FCFA" )
def Send_Money(username):
    print("SEND_MONEY")
    receiver= input("enter the receiver username: ")
    amount= int(input("enter the amount: "))
    if amount<=0:
        print("amount invalid")
        return amount
    if receiver not in users:
        print("Receiver doesn't exists")
        return receiver
    if users[username]["balance"]<amount:
        print("balance is insufficient")
        return amount 
    users[username]["balance"] -= amount
    users[receiver]["balance"] += amount
    users[username]["transaction"].append(f"sent: {amount} FCFA to {receiver}")
    users[receiver]["transaction"].append("rceived: {amount} FCFA from {username}")
    print("successfull sending")
def Define_Transaction(username):
    print("SUMMARY_TRANSATION")
    history=users[username]["transactions"]
    if not history:
        print("not transactios yet")
    else:
        for item in history:
            print("-" + item)


def Step_by_Step():
    while True:
        print("MOBILE_MONEY_SYSTEM")
        print("1. Register")
        print("2. Download")
        print("3. Exit")
        choice= input("choose an option: ")
        if choice=="1":
            registeraccount()
        elif choice=="2":
            user=log_a_user()
            if user:
                user_menu(user)
        elif choice=="3":
            print("Goodbye and Thank you")
            break
        else:
            print("Choice invalid, Restart")
def user_menu(username):
    while True:
        print("WELCOME" , username)
        print("1- Check balance")
        print("2- Send money")
        print("3- Transaction summary")
        print("4- Logout")
        choice = input("choose an option: ")
        if choice=="1":
            Balance(username)
        elif choice=="2":
            Send_Money(username)
        elif choice=="3":
            Define_Transaction(username)
        elif choice=="4":
            print("Logged successfully")
            break
        else:
            print("invalid option")
Step_by_Step()