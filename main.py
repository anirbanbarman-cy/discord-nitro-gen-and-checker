import requests
import random
import string
import time
from replit import clear

clear()
print(" ")
print("Updating")
time.sleep(.250)
clear()
print(" ")
print("Updating.")
time.sleep(.250)
clear()
print(" ")
print("Updating..")
time.sleep(.250)
clear()
print(" ")
print("Updating...")

import pkg_resources
import subprocess
import sys

required = {'pyfiglet'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
  python = sys.executable
  subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import pyfiglet
import random

clear()
nitro_gen = pyfiglet.figlet_format("Nitro Gen")
print(nitro_gen)
print(" ")
print("1 - Nitro Generator")
print(" ")
print("2 - Creidts ")
print(" ")
print("3 - Exit")
print(" ")
print(" ")

choice = input("> ")

if choice == "1":
 clear()
 print(nitro_gen)
 num = int(input('Generate > '))

 clear()
 print(nitro_gen)

 with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
 
     start = time.time()

     for i in range(num):
         code = "".join(random.choices(
             string.ascii_uppercase + string.digits + string.ascii_lowercase,
             k = 16
         ))

         file.write(f"https://discord.gift/{code}\n")

     print(f"Succsesfully Generated {num} Nitro Codes! \n")

 with open("Nitro Codes.txt") as file:
     for line in file.readlines():
         nitro = line.strip("\n")

         url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

         r = requests.get(url)

         if r.status_code == 200:
             print(f" [Valid] | {nitro} ")
             break
         else:
             print(f" [Invalid] | {nitro} ")

elif choice == "2":
 credits = open("credits.txt")
 contents = credits.read()
 credits.close()
 clear()
 print(nitro_gen) 
 print(" ")
 print(contents)

elif choice == "3":
 clear()
 print(nitro_gen)
 print(" ")
 print("Exiting...")
 print(" ")
 time.sleep(2)
 exit()

else:
  clear()
  print(nitro_gen)
  print(" ")
  print("Invalid Input!")
  print(" ")
  exit()