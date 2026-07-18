# Like a main menu of the game
print('•New Game\n•Settings\n•Leaderboard')
while True:
    s = input().lower()
    if s == "settings":
        pass
    elif s == "new game":
        from basicstructure import play_game

        choice = input("Play or Exit? ").lower()

        if choice == "play":
            play_game()
            
    elif s == "leaderboard":
        pass
    elif s == "break":
        break
    else:
        print("Please Choose from above")
    