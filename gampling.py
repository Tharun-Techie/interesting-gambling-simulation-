import random as rm

counter_win = 0
counter_lose = 0
wallet = 100
bet_val = 1

iterations = int(input("Enter the number of times to run: "))

while iterations > 0 and wallet > 20 or wallet < 160:
    result = rm.random() * 100
    
    if result > 50:
        print("Won")
        wallet += bet_val * 0.98
        bet_val = 1  # Reset bet value after a win
        counter_win += 1
    else:
        print("Lost")
        wallet -= bet_val
        bet_val *= 2  # Double the bet value after a loss
        counter_lose += 1
    
    print("Bet Value:", bet_val)
    print("Wallet Balance:", wallet)
    print("Wins:", counter_win)
    print("Losses:", counter_lose)
    print("---------------------------------------------")
    
    iterations -= 1

print("Simulation ended.")
