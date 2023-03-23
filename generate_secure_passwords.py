import secrets
import string
"""Generate secure passwords with certain conditions such as:

The length has to be 12 characters
There must be at least 1 uppercase character
There must be at least 1 lowercase character
There must be at least 1 number
There must be 1 special character"""
#define some variables that will be used to generate the password
#string containing all the lowercase and uppercase letters and and all the digits
#length of the password

chars = string.ascii_letters + string.digits
special_chars = '_!/?'
length = 12

#loop continues indefinitely until a valid password is generated
#On each iteration of the loop, a password is generated

while True:
    #selects a random character from chars, concatenated into a string using join
  passwd = ''.join([secrets.choice(chars) for i in range(length - 1)]) 
    #add special character to the end of the password
  passwd += secrets.choice(special_chars)
  
  #checks whether the password meets certain requirements
  if (any(s.islower() for s in passwd) and 
   	any(s.isupper() for s in passwd) and 
    any(s.isdigit() for s in passwd)):
        break
      
print(passwd)
# VQvnW1Uy22F?