import random as rm
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

class GamblingSimulation:
    def __init__(self, sets_to_simulate=20, iterations_per_set=250):
        self.sets_to_simulate = sets_to_simulate
        self.iterations_per_set = iterations_per_set
        self.results = []
        
    def simulate_set(self, set_number):
        counter_win = 0
        counter_lose = 0
        wallet = 100
        bet_val = 1
        set_results = []

        for _ in range(self.iterations_per_set):
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

        self.results.append({
            "Set Number": set_number,
            "Wins": counter_win,
            "Losses": counter_lose,
            "Final Wallet Balance": wallet
        })

    def run_simulation(self):
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            # Submit tasks for each set number and gather futures
            futures = {executor.submit(self.simulate_set, set_number): set_number for set_number in range(1, self.sets_to_simulate + 1)}
            
            for future in as_completed(futures):
                future.result()  # Ensure all tasks are completed

    def save_results_to_excel(self, file_name="gambling_simulation_results_oops.xlsx"):
        df = pd.DataFrame(self.results)
        df.to_excel(file_name, index=False)
        print(f"Simulation results saved to {file_name}")

if __name__ == "__main__":
    simulation = GamblingSimulation()
    simulation.run_simulation()
    simulation.save_results_to_excel()
