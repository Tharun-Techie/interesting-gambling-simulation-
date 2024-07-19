import random as rm
import pandas as pd

counter_win = 0
counter_lose = 0
wallet = 100
bet_val = 1
iterations = 0  # Initialize total iterations
results = []

while iterations < 50000:  # Run for 5000 iterations (250 sets)
    set_results = []
    for _ in range(250):  # Run 250 iterations per set
        result = rm.random() * 100
        if result > 50:
            wallet += bet_val * 0.98
            bet_val = 1  # Reset bet value after a win
            counter_win += 1
            set_results.append("Won")
        else:
            wallet -= bet_val
            bet_val *= 2  # Double the bet value after a loss
            counter_lose += 1
            set_results.append("Lost")
    
    # Store results of the set
    results.append({
        "Set Number": len(results) + 1,
        "Wins": counter_win,
        "Losses": counter_lose,
        "Final Wallet Balance": wallet
    })
    
    # Reset counters for the next set
    counter_win = 0
    counter_lose = 0
    wallet = 100
    bet_val = 1
    
    iterations += 250  # Increment total iterations

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save DataFrame to Excel file
file_name = "gambling_simulation_results.xlsx"
df.to_excel(file_name, index=False)

print(f"Simulation results saved to {file_name}")
