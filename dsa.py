import random as rm
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

def simulate_set(set_number):
    counter_win = 0
    counter_lose = 0
    wallet = 100
    bet_val = 1
    set_results = []

    for _ in range(250):
        result = rm.random() * 100
        if result > 50:
            wallet += bet_val * 0.98
            bet_val = 1
            counter_win += 1
            set_results.append("Won")
        else:
            wallet -= bet_val
            bet_val *= 2
            counter_lose += 1
            set_results.append("Lost")

    return {
        "Set Number": set_number,
        "Wins": counter_win,
        "Losses": counter_lose,
        "Final Wallet Balance": wallet
    }

if __name__ == "__main__":
    sets_to_simulate = 2000  # Total sets to simulate

    # Create a ProcessPoolExecutor with the number of available CPUs
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # Submit tasks for each set number and gather futures
        futures = {executor.submit(simulate_set, set_number): set_number for set_number in range(1, sets_to_simulate + 1)}
        
        results = []
        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    
    # Save DataFrame to Excel file
    file_name = "DAS_gambling_simulation_results_multiprocessing.xlsx"
    df.to_excel(file_name, index=False)

    print(f"Simulation results saved to {file_name}")
