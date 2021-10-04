print("welcome to my no. guess game")
my_number = 48
guess = 0
max_guess = 9
game_loop= True
while game_loop:
    guess += 1
    max_guess -= 1
    guess_no = int(input("Enter your no.= "))
    if my_number == guess_no:
        print("Congrats you win\n", "in times= ",guess,"& left guesses =",max_guess)
        game_loop= False
    elif my_number > guess_no:
        print("Your no. is smaller then my no. please try again\n","your guesses left=",max_guess)
        if max_guess == 0:
            print("Game over you lost your max guesses is reached")
            game_loop= False
    elif my_number < guess_no:
        print("Your no. is greater then my no. please try again\n", "your guesses left=", max_guess)
        if max_guess == 0:
            print("Game over you lost your max guesses is reached")
            game_loop= False