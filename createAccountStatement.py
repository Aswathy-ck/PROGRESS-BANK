import datetime
def createEntry(username,amount,transactiontype):
    statementfile=open("accountStatement.txt","a")

    currentDate=datetime.datetime.now()
    currentDateConverted = str(currentDate)
    statementfile.write((username+" "+str(amount)+" "+ transactiontype+" "+currentDateConverted+"\n"))

