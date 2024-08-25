Gambling Simulation with Multiprocessing
========================================

Overview
--------

This project simulates a gambling scenario using Python, leveraging multiprocessing for efficient parallel processing. Each simulation set runs independently, and the results are saved to an Excel file for analysis.

Requirements
------------

*   Python 3.x (check requirements.txt)
*   `pandas` library
*   `openpyxl` library (automatically installed with `pandas`)
*   (Optional) `numpy` for numeric operations (if needed in future enhancements)

Installation
------------

    git clone https://github.com/your-username/gambling-simulation.git

    cd gambling-simulation

### Install dependencies:

    pip install pandas openpyxl

### Run the simulation:

    python gambling_simulation.py

Usage
-----

*   Adjust `sets_to_simulate` and `iterations_per_set` in `gambling_simulation.py` to modify simulation parameters.
*   Results are saved in `gambling_simulation_results.xlsx` by default. Modify `save_results_to_excel()` in `GamblingSimulation` class for custom file names or paths.

File Structure
--------------

*   `gambling_simulation.py`: Main script containing the `GamblingSimulation` class and multiprocessing logic.
*   `README.md`: This file, providing project overview, installation instructions, and usage guidelines.
*   `gambling_simulation_results.xlsx`: Default output file for simulation results.

Contributing
------------

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure the code follows PEP 8 style guidelines and include tests if applicable.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
