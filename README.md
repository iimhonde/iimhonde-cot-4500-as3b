# COT-4500-AS3B

# Programming Assignment 3

##  Overview
This assignment implements numerical methods in Python, including:
    gaussian jordan
    LU factorization
    diagonally dominant, 
    positive definite

The project follows a structured format to ensure modularity and testability.

---

##  Project Structure
cot-4500-as3b/ │-- src/ │ │-- main/ │ │ │-- assignment_3.py # Main implementation │ │-- test/ │ │ │-- test_assignment_3.py # Test cases │-- requirements.txt # Dependencies │-- README.md # Documentation


---

##  Installation & Setup

### ** Install Dependencies**
This project requires third-party libraries listed in `requirements.txt`.  
Run the following command to install them:
```bash
pip install -r requirements.txt

## To execute the numerical methods, run:
python -m unittest discover -s src/test

