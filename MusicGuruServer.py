# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
# this tutorial was used to figure out the framework of the socket connection for both the server and client


import socket
import random

# parser that reads the music_data.txt file and creates a dictionary of the data
music_dictionary = {}
with open('music_data.txt', 'r') as file:
    year = None
    songs = []
    for line in file:
        line = line.strip()
        if line.isdigit():
            year = int(line)
            songs = []
        elif line:
            songs.append(line)
        if year and songs:
            music_dictionary[year] = songs



def server_side():
    host = socket.gethostname()
    port = 5000  
    #connection to socket
    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(2)
    # loop allows for continuous listening for connections
    while True:
        conn, address = server_socket.accept()  
        print("Connection from: " + str(address))
    
        conn.send("Year range: 1950-2010".encode())
        
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        
        if int(data) >=1950 and int(data) <= 2009:
            response = random.choice(music_dictionary[int(data)])
        else:
            response = random.choice(music_dictionary[random.randint(1950, 2009)])

        conn.send(response.encode()) 

        conn.close() 


if __name__ == '__main__':
    server_side()