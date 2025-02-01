import time
import os

trunk = input("Enter your name to verify this is your trunk: ")
os.system("cls")
print("loading features...")
time.sleep(2)
os.system("cls")

if trunk == trunk:
    print("Welcome to your trunk you must be", trunk)

answer = input("yes or no: ")

if answer == "yes":
    os.system("cls")
    print("Great let me show you around your trunk", trunk)

if answer == "no":
    print("Alright ending have a great day or night")
    os.system("cls")
    print("Please restart this code it has ended")


