import time

def check(c, P):
    
    if c >= 15:
        if P == "p1":
            print("Player 2 wins!")
            print("GAME OVER")
        elif P == "p2":
            print("Player 1 wins!")
            print("GAME OVER")
    else:
        pass


if __name__ == "__main__":
    count = 0
    p1 = 0
    p2 = 0

    print("There are 2 players. Player 1 counts upwards from 0, only by 1, 2, or 3. Player 2 does the same, and this repeats. Whoever chooses 15 within their selection loses.")

    while True:
        
        while True:

            try:
                ask1 = int(input("How many numbers p1?_"))
                if 1 <= ask1 <= 3:
                    p1 += ask1
                    count += ask1
                    print("Player 1 chose: " + str(count))
                    check(count, "p1")
                    if count >= 15:
                        time.sleep(4)
                        exit()
                else:
                    print("Choose at least 1 or up to 3 numbers")
                    
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            
            try:
                ask2 = int(input("How many numbers p2?_"))
                
                if 1 <= ask2 <= 3:
                    p2 += ask2
                    count += ask2
                    print("Player 2 chose: " + str(count))
                    check(count, "p2")
                    if count >= 15:
                        time.sleep(4)
                        exit()                        
                else:
                    print("Choose at least 1 or up to 3 numbers")
                    
            except ValueError:
                print("Invalid input. Please enter a number.")
