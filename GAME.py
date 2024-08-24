import mysql.connector
from random import *

# CONNECTION TO MYSQL DATABASE
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='game_data'
)
cursor = conn.cursor()


# SCORE OF GAME PRIMARILY SET TO 0
SCORE = 0

# CONVERTING COMPUTER CHOICE INTO STRING WORDS
def comp_to_user(COMP):
    if COMP == 0:
        return "STONE"
    elif COMP == 1:
        return "PAPER"
    elif COMP == 2:
        return "SCISSORS"


# CONVERTING USER STRING INPUT INTO WORDS
def usr_to_lett(USER):
    if USER == '0':
        return "STONE"
    elif USER == '1':
        return "PAPER"
    elif USER == '2':
        return "SCISSORS"
    else:
        return "Invalid choice"

# GAME MAIN CODE 
def GAME(USER, COMP):
    global SCORE
    user_choice = int(USER)
    
    if user_choice == COMP:
        return "IT'S A TIE !!!"
    elif (user_choice == 0 and COMP == 2) or (user_choice == 1 and COMP == 0) or (user_choice == 2 and COMP == 1):
        SCORE += 1
        return "YOU WON !!!"
    else:
        SCORE -= 1
        return "COMPUTER WON !!!"


# SQL QUERY
def record_score(username, score):
    query = "INSERT INTO scores (username, score) VALUES (%s, %s)"
    cursor.execute(query, (username, score))
    conn.commit()

username = input("Enter your username: ")



# INFINITE LOOP STATEMENT
while True:
    USER = input("Enter the desired option out of the above for your choice:\n(0 = STONE)\n(1 = PAPER)\n(2 = SCISSORS)\nEnter your choice (or 'q' to quit): ").upper()
    COMP = randint(0, 2)
    
    if USER == "Q":
        print("Thanks for playing!")
        break
    
    if USER not in ['0', '1', '2']:
        print("Invalid choice. Please try again.")
        continue
    
    print(f"Your choice is: {usr_to_lett(USER)}")
    print(f"Computer's choice is: {comp_to_user(COMP)}")
    
    print(GAME(USER, COMP))
    print(f"Your current score is: {SCORE}")
    
    record_score(username, SCORE)

cursor.close()
conn.close()
