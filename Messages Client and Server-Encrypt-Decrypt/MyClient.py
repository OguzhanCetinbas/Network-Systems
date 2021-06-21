from socket import *
def main():
    serverPort = 12301
    serverName = "localhost"
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message =input(" Please enter your command ")  # you must write with "deposit 500 " or "withdraw 500" format
    message = encryption(message)       #Send the message in the encryption function to change our message
    print(message + "\t \t \t Encription of our sentences ")    #Encryption form of our message
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode() + " \t \t \t Return of the message(Decryption part)")  #Return of our message
    clientSocket.close()

def encryption(message):
    stringMessage=""
    post = []
    firstTime = False                       #Take the our message sentences
    byteArray = bytearray(message,"utf8")     #Change with byte array
    for i in byteArray:
        binaryForm = bin(i).replace("0b","")      #Change with Ob head of the array
        change =int(binaryForm)*11+11
        post.append(change)                     #Change and the integer form and choose the changing of mulply 11 + 11
    for i in post:
        if(firstTime):
            stringMessage = stringMessage + " "          #Take firstTime boolean type add from string type each of integer
        stringMessage =stringMessage + str(i)            #return of the string
        firstTime = True
    return stringMessage
main()

