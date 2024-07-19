<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gambling Simulation with Multiprocessing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 4px;
            font-family: "Courier New", Courier, monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            white-space: pre-wrap;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        .important {
            color: #c0392b;
            font-weight: bold;
        }
        .note {
            color: #3498db;
        }
        .code-block {
            background-color: #f8f9fa;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <h1>Gambling Simulation with Multiprocessing</h1>

    <h2>Overview</h2>
    <p>This project simulates a gambling scenario using Python, leveraging multiprocessing for efficient parallel processing. Each simulation set runs independently, and the results are saved to an Excel file for analysis.</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>pandas</code> library</li>
        <li><code>openpyxl</code> library (automatically installed with <code>pandas</code>)</li>
        <li>(Optional) <code>numpy</code> for numeric operations (if needed in future enhancements)</li>
    </ul>

    <h2>Installation</h2>
    <div class="code-block">
        <pre><code>git clone https://github.com/your-username/gambling-simulation.git</code></pre>
        <pre><code>cd gambling-simulation</code></pre>
    </div>

    <div class="code-block">
        <h3>Install dependencies:</h3>
        <pre><code>pip install pandas openpyxl</code></pre>
    </div>

    <div class="code-block">
        <h3>Run the simulation:</h3>
        <pre><code>python gambling_simulation.py</code></pre>
    </div>

    <h2>Usage</h2>
    <ul>
        <li>Adjust <code>sets_to_simulate</code> and <code>iterations_per_set</code> in <code>gambling_simulation.py</code> to modify simulation parameters.</li>
        <li>Results are saved in <code>gambling_simulation_results.xlsx</code> by default. Modify <code>save_results_to_excel()</code> in <code>GamblingSimulation</code> class for custom file names or paths.</li>
    </ul>

    <h2>File Structure</h2>
    <ul>
        <li><code>gambling_simulation.py</code>: Main script containing the <code>GamblingSimulation</code> class and multiprocessing logic.</li>
        <li><code>README.md</code>: This file, providing project overview, installation instructions, and usage guidelines.</li>
        <li><code>gambling_simulation_results.xlsx</code>: Default output file for simulation results.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure the code follows PEP 8 style guidelines and include tests if applicable.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
