# ransomware-python3
Ransomware made with python3

-The ransomware doesn't rely on third party libs, so all you need from the victim machine is just a regular python3 installation ;)

This repo consists of three files:
  1-the encrypt file:
    -it generates a 512-bit key and initiates a connection to a server that you specify in the file.
    -then it initiates a connection to a server that you specify in the file and sends the key to the server.
    -then it starts encrypting the whole system whether it's a linux or a windows system.
    -it relies on XOR encryption technique.
    
  2-the decrypt file:
    -the file takes the key in hexadecimal format and decrypts the files.

  3-the server file:
    -the listener that you will run and wait for the ransomware to send you the encryption key.


-Installation:
  
  1-

      git clone https://github.com/BiLLY-J03l/ransomware-python3.git

  2-
  
      chmod +x *


-DO NOT RUN THE ENCRYPTOR SCRIPT ON YOUR COMPUTER, USE A VIRTUAL MACHINE.
-The perks of the project:
  1-No extra libs are needed other than a clean python3 installation.
  2-uses XOR encryption via bitwise operations.
  3-you can modify the script to not encrypt certain folders which can come in handy.
