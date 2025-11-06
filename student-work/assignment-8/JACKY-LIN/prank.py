from colorama import Fore, Back, Style

password = "helloworld"
userentry = input(Fore.CYAN + f"Enter password (just this time the password is {password}) :")

#if password is incorrect
while userentry != password:
    print(Fore.RED + "INVALID ENTRY. Please try again.")
    userentry = input("Enter password: ")

# If the password is correct
print(Fore.GREEN + "VALID ENTRY")

#fake stall now time
import time 
time.sleep(2)
print(Style.RESET_ALL)
# Generate a random integer between 1 and 10 (inclusive)
import random
count = 0
numlist = []
while count != 10:
    time.sleep(1)
    count += 1
    number = random.random()
    numlist.append(number)
    print(numlist)

print("Beginning Prank Algorithm")
while count != 100000:
    count += 1
    print("Running Application")
    number = random.randint(1, 100000000000000000)
    print(Fore.RED + str(number))

tostart = ""
while tostart != "enter":
    print(Fore.GREEN + "Brute Force ready to begin")
    tostart = input("type \"enter\" to begin: ")
    if tostart != "enter":
        print(Fore.RED + "error, try again")
    else:
        break

print(Style.RESET_ALL)
print(Fore.GREEN + "LOADING")
time.sleep(3)
print(Style.RESET_ALL)
print("Starting Brute Force....")

for i in range(10, -1, -1):
    time.sleep(1)
    print("Attack Starting In...." + str(i))
print(Fore.GREEN + "Initializing ....")
time.sleep(5)
count = -1
#FOREVER LOOP
while True:
    count += 1
    print(Fore.BLUE + "NOW TRYING " + str(count))
    print(Fore.RED + "ERROR, FATAL PATTERN DETECTED")
    print(Back.GREEN + "ACCESS DENIED")
    time.sleep(0.1)
