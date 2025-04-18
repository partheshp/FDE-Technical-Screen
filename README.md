## Package Sorting Function
This repository implements a function that sorts packages based on their volume and mass. The objective of this function is to classify the packages into different stacks according to the provided rules.

## Problem Overview

In the factory, robotic arms dispatch packages into different stacks based on these criteria:

### Rules for classification:

**1. Bulky Packages:**
  - A package is considered bulky if:
      - Its volume is greater than or equal to 1,000,000 cm³, OR
      - Any of its dimensions (width, height, or length) is greater than or equal to 150 cm.

**2. Heavy Packages:**
  - A package is considered heavy if its mass is greater than or equal to 20 kg.

### Stack Classification:
- **STANDARD:** If the package is neither bulky or heavy
- **SPECIAL:** If the package is either bulky or heavy (but not both)
- **REJECTED:**  If the package is both bulky and heavy

The function classifies the package into one of the three stacks and returns a corresponding string: "STANDARD", "SPECIAL", or "REJECTED".

## Function:
```
sort(width, height, length, mass)
```
This function receives the dimensions (width, height, length) and the mass of a package and returns a string indicating the stack where the package should go: "STANDARD", "SPECIAL", or "REJECTED".

### Parameters:
- width (int/float): The width of the package in centimeters.
- height (int/float): The height of the package in centimeters.
- length (int/float): The length of the package in centimeters.
- mass (float): The mass of the package in kilograms.

## Testing:
To test the function, you can run the unit tests provided in the ```test.py``` file. The test cases cover various scenarios and edge cases, ensuring the function works as expected.

### Running the tests:
1. Clone or download this repository
```
git clone https://github.com/partheshp/FDE-Technical-Screen.git
```
2. Install any necessary dependencies (if required, such as ```unittest```)
3. Run the test cases using Python's built-in unittest framework:
```
python -m unittest test.py
```
This will execute all the test cases and output the results to the console.
