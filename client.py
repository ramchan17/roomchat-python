import socket, threading

HOST ="127.0.0.1"
PORT = 1234

def listen_for_messages(client):
     
     while 1:
            message = client.recv(2048).decode('utf-8')
            if message !='':
                
                username = message.split("~")[0]
                content = message.split("~")[1]
               
                print(f"[{username}] : {content}")
            else:
                print("Message from the server is empty")

def send_message_to_server(client):
    
    while 1:
        message = input("Message: ")
        if message != '':
            client.sendall(message.encode())
            
        else:
            print("Message cannot be empty")

def communicate_to_server(client):
    
    username = input("Enter your username: ")
    if username != '':
        client.sendall(username.encode())
    else:
        print("Your username cannot be  empty")
        exit(0)
    threading.Thread(target=listen_for_messages,args=(client,)).start()

    send_message_to_server(client)




def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((HOST,PORT))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST} {PORT}")
    
    communicate_to_server(client)

if __name__ =="__main__":
   main()