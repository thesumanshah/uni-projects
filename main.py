 #display ascii art
import random
from game_data import data
from art import logo,vs
score=0
account_b=random.choice(data)

def format_data(account):
   account_name=account["name"]
   account_description=account["description"]
   account_country=account["country"]
   return(f'{account_name}, a {account_description}, from {account_country}')
 

def check_answer(user_ask, a_follower,b_follower):
    """take a users guess and followers counts and returns if they got it right """
    if a_follower>b_follower:
        return user_ask=="a"
    else:
        return user_ask=="b"

print(logo)
 ## generate random account form the game data
final_game=True
while final_game==True:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
        
    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    ## format the account data into printable format
    ##ask user for the guess 

    ask=input("Who has more followers? Type A or B: ").lower()
    print("\n"*20)

    # check if user is corrrect
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    
    
    #get followr count of each account
    is_correct=check_answer(ask,a_follower_count,b_follower_count)

    #use if statement to check if user is correct
    if is_correct:
        score+=1
        print(f"your are right final score is {score}")
    else:
        print(f"sorry, that's Wrong final score is {score}")
        final_game=False
     
 #give user feedback on their guess
 #score keeping
 #make game reapeatable
 #making account at position B become the next account at postion A
 