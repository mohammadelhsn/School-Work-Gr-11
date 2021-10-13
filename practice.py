#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

ask = input("Hello there! What is your name\n")
ask2 = input(f"Hello {ask.capitalize()}! How's your day?\n")


if ask2.lower() == "good" or ask2.lower() == "great":
    print("That's great! I'm glad to hear that")

if ask2.lower() == "bad":
    print("Oh no! I'm sorry to hear that")

if ask2.lower() == "ok":
    print("That's okay")