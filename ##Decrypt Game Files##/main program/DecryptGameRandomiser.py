import random

def main_game():
    print("Welcome to - The Decrypt Randomiser! -\nHere you will be able to decide the fate of your 'Adventurer' as you embark on your journey to defeat 'The Master!'")
    invalid = True
    while invalid == True:
        confirm = input("Would you like to run the randomiser? (Y/N): ").upper()
        if confirm == "":
            print("Invalid input, TRY AGAIN")
        elif confirm[0] == "Y":
            print("\nPerfect, let's continue!\n")
            invalid = False
        elif confirm[0] == "N":
            print("OK, see ya'!")
            return
    valid = False
    while valid == False:
        data = []

        choice = input("What would you like to do?\n1.Choose Square Event.\n2.Open effects dictionary.\n3.END the randomiser.\n")
        if choice == "1":
            square_event = input("Please enter your square colour after moving: ").upper()
            if square_event[0] == "B":
                print("Black")
                with open ("BlackEvents.txt","r") as file:
                    for line in file:
                        info = [item.strip() for item in line.split("\n")]
                        data.append(info)
                    rand = random.choice(data)
                    print(rand[0])
                    print("\n")

                    if rand[0] == data[0][0]:
                        with open ("AllPieces.txt","r") as file:
                            for line in file:
                                pieces_info = [item.strip() for item in line.split("\n")]
                                data.append(pieces_info)
                            rand_piece = random.choice(data)
                            print(rand_piece[0])

            elif square_event[0] == "W":
                print("White")
                with open ("WhiteEvents.txt","r") as file:
                    for line in file:
                        info = [item.strip() for item in line.split("\n")]
                        data.append(info)
                    rand = random.choice(data)
                    print(rand[0])
                    print("\n")
                    
                    if rand[0] == data[0][0]:
                        with open ("AllPieces.txt","r") as file:
                            for line in file:
                                pieces_info = [item.strip() for item in line.split("\n")]
                                data.append(pieces_info)
                            rand_piece = random.choice(data)
                            print(rand_piece[0])

                    if rand[0] == data[1][0]:
                        spin = input("Would you like to spin the Wheel of Lucky Things? (Y/N): ").upper()
                        if spin[0] == "Y":
                            with open ("LuckyWheel.txt","r") as file:
                                for line in file:
                                    luck_info = [item.strip() for item in line.split("\n")]
                                    data.append(luck_info)
                                rand_luck = random.choice(data)
                                print(rand_luck[0])
                                print("\n")
                        elif spin[0] == "N":
                            print("Okay...suit yourself\n")
            else:
                print("Wrong! Please enter 'Black' OR 'White'")

        elif choice == "2":
            with open ("EffectsDictionary.txt","r") as file:
                for line in file:
                    info = [item.strip() for item in line.split("\n")]
                    data.append(info)
                for i in range (0,len(data)):
                    print(data[i][0])
                leave = input("Enter anything to EXIT the Dictionary: ")
                if leave or leave == "":
                    print("LEAVING\n")
        elif choice == "3":
            return

main_game()
