from socket import *
balance = 1000
def main():
    serverPort = 12301
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))
    print("The Server is ready to receive")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()  #  message.decode = modified message
        print('Encrypted message', modifiedMessage)  #message come in the server part in encrypted form
        modifiedMessage = decryption(modifiedMessage)       #create decryption method to resolve te message and call it
        print('Decrypted message', modifiedMessage)
        words = modifiedMessage.split(" ")
        command = words[0]
        amount = int(words[1])
        message = ""
        print(amount)
        if (command == "deposit"):
            deposit(amount)
            message = str(amount) + " amount of money is deposited. New balance is :" + str(balance)
        elif (command == "withdraw"):
            withdraw(int(amount))
            message = str(amount) + " amount of money is withdrawed. New balance is :" + str(balance)
        else:
            message = "There is a problem"
        serverSocket.sendto(message.encode(), clientAddress)

def deposit(amount):
    global balance
    balance = balance+amount

def withdraw(amount):
    global balance
    balance = balance-amount

def decryption(message):
    String = ""
    arr = message.split(" ")
    for i in arr:
        no1 = int(i) - 11
        no2 = no1 / 11
        bin = int(no2)
        binaryForm= str(bin)
        IntChar = int(binaryForm, 2)
        mychar = chr(IntChar)
        String = String + mychar
    return String

main()