
# Three Jugs Problem #11

This project solves the classic "Three Jugs" using Breadth-First Search (BFS). Given three jugs with capacities of 8, 5, and 3 pints, the goal is to achieve exactly 4 pints in one of the jugs. This code simulates the process of pouring water between jugs to reach the target amount.

## Solution Overview

This solution uses BFS to explore all possible jug configurations. Starting with the initial configuration `(8, 0, 0)`, representing 8 pints in the first jug and 0 in the others, it systematically pours water between jugs until one contains exactly 4 pints.


## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This code requires **Python 3.12.0** or higher. You can check if Python is installed by running:

```bash
python --version
```

### Installation

1. **Dependencies**: This code only uses Python's standard library (`collections`) that I used to import "deque", so there are no additional dependencies to install.


## Running the Code

1. **Navigate to the Project Directory**:

   ```bash
   cd three-jugs-solver
   ```

2. **Execute the Code**:

   Run the script directly using Python:

   ```bash
   python Salome Mutemwa_Assignment3.py
   ```

   This will start the BFS search and output each configuration as the code explores possible solutions. When the solution (4 pints in one of the jugs) is found, the program will print the successful configuration and stop.


## Example Output

Upon running, you will see the configurations as the BFS explores each option:

```plaintext
Visited positions are (3, 5, 0)
Visited positions are (5, 0, 3)
Visited positions are (0, 5, 3)
Visited positions are (3, 2, 3)
Visited positions are (5, 3, 0)
Visited positions are (6, 2, 0)
Visited positions are (2, 3, 3)
Visited positions are (6, 0, 2)
Visited positions are (2, 5, 1)
Visited positions are (1, 5, 2)
Visited positions are (7, 0, 1)
Visited positions are (1, 4, 3)
Visited positions are (7, 1, 0)
The puzzle is solved! The position with 4 pints is (1, 4, 3)
```


## Explanation of Key Components

- **`initial_position`**: The starting configuration of the jugs, represented as `(8, 0, 0)`.
- **BFS**: A queue-based approach that explores each configuration step-by-step until the target configuration is found.
- **Pour Operations**: Simulates pouring between jugs by calculating the maximum amount each can hold.

---

## Troubleshooting

If you encounter any issues:
- Verify that you have Python 3.10 or higher installed.
- Ensure that you’re in the correct directory.


## License

This project is open source under the MIT License. Feel free to contribute or modify it as needed!


### Contact

For questions, feel free to reach out at `salome.mutemwa@ashesi.edu.gh`.
