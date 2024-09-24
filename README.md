# CGPA Calculator with TGPA Encryption

This Python application provides a GUI-based solution to calculate students' TGPA and CGPA using semester marks. It also includes encryption and decryption functionalities to protect student data when stored in a SQLite database.

## Features

- Calculate TGPA for two semesters.
- Compute the combined CGPA for both semesters.
- Store student results securely using simple encryption.
- Fetch student records from a SQLite database.
- User-friendly graphical interface built with Tkinter.

## Installation

### Prerequisites

- Python 3.x
- Tkinter library (comes pre-installed with Python)
- SQLite3 (comes with Python standard library)

### Steps to Install and Run

1. Clone the repository:
    ```bash
    git clone https://github.com/rashmi-murari/cgpa_calculator.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Enter the marks for each subject for semester 1 and semester 2.
2. Click on the `Calculate` button to get TGPA and CGPA.
3. Use the `Save` button to store the results securely in the database.
4. You can fetch records by entering the student ID and clicking `Search`.

## Project Structure

```bash
cgpa_calculator/
│
├── app.py                 # Entry point for the application
├── gui.py                 # Contains GUI logic
├── encryption.py          # Encryption and decryption functions
├── calculations.py        # TGPA and CGPA calculation logic
├── database.py            # Database interaction functions
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── mysql.db               # SQLite database (auto-generated)
