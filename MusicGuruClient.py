import socket
import random

def client_side():
    host = input("Enter ip address: ")
    port = 5000
    
    client_socket = socket.socket()
    client_socket.connect((host,port))
    

    # get date range from server
    data = client_socket.recv(1024).decode()
    print(data)
    print("Type 'end' to exit")
    
    message = input("Choose Year: ")
        
    if int(message) >=1950 and int(message) <= 2009:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
    else:
        rand_year = random.randint(1950, 2009)
        print("Invalid Entry. Using random year: {}".format(rand_year))
        client_socket.send(str(rand_year).encode())
        data = client_socket.recv(1024).decode()

    print(data)
   
    client_socket.close()

    input("Press Enter to exit. ")

if __name__ == '__main__':
    client_side()

