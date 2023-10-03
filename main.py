initialAccountNumber=60000000
import json
import createAccountStatement
def updatefile():
    userfile = open("user.txt", "w")
    contentstring = ""
    for i in userlistconverted:
        contentstring = contentstring + str(i) + "\n"

    userfile.write(contentstring)
def viewaccountdetails():
    for i in userdata:
        if(i=="PASSWORD"):
            continue
        print(i, " : ",userdata[i])
def deposit(user):
    amount=float(input("ENTER AMOUNT TO DEPOSIT : "))

    for i in userlistconverted:
        if i["USERNAME"]==user:
            i["ACCOUNT BALANCE"]=i["ACCOUNT BALANCE"]+amount

    updatefile()
    print("DEPOPOSITED SUCCESSFULLY !")
    createAccountStatement.createEntry(user,amount,"credit")

def withdraw(user):
    amount = float(input("ENTER AMOUNT TO WITHDRAW : "))
    if amount>userdata["ACCOUNT BALANCE"]:
        print("NOT ENOUGH BALANCE IN YOUR ACCOUNT")
        return
    for i in userlistconverted:
        if i["USERNAME"] == user:
            i["ACCOUNT BALANCE"] = i["ACCOUNT BALANCE"] - amount

    updatefile()
    print("WITHDRAW SUCCESSFULLY !")
    createAccountStatement.createEntry(user, amount, "Debit")

def transfer(user):
   accountnumber = int(input("ENTER THE ACCONT NUMBER WHICH YOU WANT TO TRANSFER MONEY : "))
   amount = float(input("ENTER AMOUNT TO DEPOSIT : "))

   if amount > userdata["ACCOUNT BALANCE"]:
       print("NOT ENOUGH BALANCE IN YOUR ACCOUNT")
       return

   for i in userlistconverted:

       if (i["USERNAME"] == user):
           i["ACCOUNT BALANCE"] = i["ACCOUNT BALANCE"] - amount
       if (i["ACCOUNT NUMBER"] == accountnumber):
           i["ACCOUNT BALANCE"] = i["ACCOUNT BALANCE"] + amount


   updatefile()
   print("TRANSFER SUCCESSFULLY !")
   createAccountStatement.createEntry(user, amount, "Debit")


def viewaccountstatement():
    statementfile = open("accountStatement.txt")
    filecontent = statementfile.read()
    filecontentsplit = filecontent.split("\n")
    for i in filecontentsplit:
        linesplit = i.split(" ")
        if linesplit[0]==userName:
            print(i)
userdata={}
userlistconverted=list()
def validateuser(username,password):
    global userdata
    global  userlistconverted
    userfile = open("user.txt")
    filecontent=userfile.read()
    filecontentsplit= filecontent.split("\n")

    userlistconverted = list()
    for i in filecontentsplit:
        if i == "":
            continue
        stringconverted = i.replace("'","\"")
        userlistconverted.append(json.loads(stringconverted))

    userfound = 0
    foundpassword = ""
    for value in userlistconverted:
        if(value["USERNAME"]==username):
            userfound=1
            foundpassword = value["PASSWORD"]
            userdata=value
    if userfound==0:
        print("Invalid username")
    elif userfound==1:
        if(foundpassword==password):
            return "success"

        else:
            print("Invalid password")


def getNumberofUsers():
    userfile = open("user.txt")
    filecontent=userfile.read()
    filecontentsplit=filecontent.split("\n")
    NumberOfUsers=len(filecontentsplit)
    return NumberOfUsers


def register():
    usercount=getNumberofUsers()
    accountnumber=initialAccountNumber+usercount
    name = input("ENTER YOUR NAME : ")
    phonenumber=input("ENTER YOUR PHONE NUMBER : ")
    email=input("ENTER YOUR EMAIL : ")
    address=input("ENTER YOUR ADDRESS : ")
    username = input("ENTER YOUR USERNAME : ")
    password = input("ENTER YOUR PASSWORD : ")
    print("REGISTRATION SUCCESSFULL")
    userfile = open("user.txt","a")
    userdata={
        "NAME":name,
        "PHONENUMBER":phonenumber,
        "EMAIL":email,
        "ADDRESS":address,
        "USERNAME":username,
        "PASSWORD":password,
        "ACCOUNT NUMBER":accountnumber,
        "ACCOUNT BALANCE":0
    }
    userconverted = str(userdata)
    userconverted=userconverted+"\n"
    userfile.write(userconverted)
print("registration successfully !!")
print("--------------------------------------------------------------")
print("WELCOME TO PROGRESS BANK")
print("--------------------------------------------------------------")
print("Please choose one of the following option")
option=input("1.LOGIN\t2.REGISTER : ")
if option=="1":
    userName = input("ENTER USERNAME : ")
    password = input("ENTER THE PASSWORD : ")


    validateresult=validateuser(userName,password)
    if(validateresult=="success"):
        print("------------------------------------------------------")
        print("Please select one of the following option \n 1.VIEW ACCOUNT DETAILS \n 2.DEPOSIT \n 3.WITHDRAW \n 4.TRANSFER \n 5.VIEW ACCOUNT STATEMENT")
        option2=input()
        if(option2=="1"):
            viewaccountdetails()
        elif(option2=="2"):
            deposit(userName)
        elif(option2=="3"):
            withdraw(userName)
        elif(option2=="4"):
            transfer(userName)
        elif(option2=="5"):
            viewaccountstatement()
        else:
            print("invalid choice")
elif option=="2":
    print("---------------------------------------------")
    print("REGISTER")
    print("---------------------------------------------")
    register()
else:
    print("invalid choice")



