from socket import *
def main():
    serverPort = 12301
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))
    print("The Server is ready to receive")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()              #message.decode = modified message
        modifiedMessage= decryption(modifiedMessage)                #take the modified message in the decryption part of the function
        print(modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
def decryption(message):
    String = ""
    arr = message.split(" ")                #In the last of array we have space,we split in the array
    for i in arr:
        no1 = int(i) - 11                      #Then we reverse part
        no2 = no1 / 11
        bin = int(no2)                          #once subs 11 and divide with 11
        binaryForm= str(bin)                       #Change with the String form and change with binary form
        IntChar = int(binaryForm, 2)
        mychar = chr(IntChar)
        String = String + mychar                        #Then change with character the return of the string we add
    return String

main()