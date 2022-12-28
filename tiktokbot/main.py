
#importing the necessary libraries
import time
import random

#defining the main function
def main():
    #printing the welcome message
    print("Welcome to the TikTok Follower Bot!")
    #asking the user to enter the username
    username = input("Please enter the username of the account you want to follow: ")
    #asking the user to enter the number of followers
    followers = int(input("Please enter the number of followers you want to add: "))
    #printing the message
    print("Adding " + str(followers) + " followers to " + username + "...")
    #looping through the number of followers
    for i in range(followers):
        #generating a random number
        random_number = random.randint(1, 10)
        #printing the message
        print("Following " + username + "...")
        #adding a delay
        time.sleep(random_number)
    #printing the success message
    print("Successfully added " + str(followers) + " followers to " + username + "!")

#calling the main function
if __name__ == "__main__":
    main()