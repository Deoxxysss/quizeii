# Like a main menu of the game
from basicstructure import play_game
from leaderboard import leaderboard
def Menu():
    print("=====WELCOME TO QUIZEII=====")
    print()
    print()
    print('•New Game\n•Settings\n•Leaderboard')
    while True:
        s = input().lower()
        if s == "settings":
            pass
        elif s == "new game":

            choice = input("Play or Exit? ").lower()

            if choice == "play":
                play_game()
                break
                
        elif s == "leaderboard":
            leaderboard()
            i = input("Enter back to go to the main screen→:")
            if i == "back":
                Menu()
        elif s == "break":
            break
        else:
            print("Please Choose from above")