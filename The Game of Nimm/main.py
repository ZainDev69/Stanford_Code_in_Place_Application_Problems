def main():
    stones = 20
    player = 1

    while stones > 0:
        print("There are " + str(stones) + " stones left.")
        
        user_input = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        
        # Milestone 3: validate input
        while user_input != 1 and user_input != 2:
            user_input = int(input("Please enter 1 or 2: "))
        
        stones -= user_input
        
        # Milestone 4: check if game over
        if stones <= 0:
            # The player who took the last stone loses
            # So the OTHER player wins
            if player == 1:
                winner = 2
            else:
                winner = 1
            print("Player " + str(winner) + " wins!")
            return
        
        print()  # empty print for spacing
        
        # Switch player (Milestone 2)
        if player == 1:
            player = 2
        else:
            player = 1

if __name__ == '__main__':
    main()