from tkinter import *
from tkinter import ttk
from calculations import calculate_tgpa1, calculate_tgpa2, calculate_cgpa
from database import save_to_database, fetch_from_database


class CGPACalculatorApp:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("680x750")
        self.win.title('CGPA Calculator')

        self.setup_widgets()

    def setup_widgets(self):
        """Setup the widgets for the application."""
        # Define and place GUI components (Entry fields, Buttons, Labels)
        # You can modularize widget placement further if needed
        
        # Example:
        self.name1 = StringVar()
        Label(self.win, text="Student Name").pack()
        Entry(self.win, textvariable=self.name1).pack()

        # Define more entry fields, labels, and buttons
        Button(self.win, text="Calculate", command=self.on_calculate_button_click).pack()

    def run(self):
        """Run the application."""
        self.win.mainloop()

    def on_calculate_button_click(self):
        """Handles the calculation and saving of TGPA/CGPA on button click."""
        name = self.name1.get()
        reg = self.reg1.get()
        tgpa1 = calculate_tgpa1(self.a1, self.c1, self.e1, self.g1, self.i1, self.k1)
        tgpa2 = calculate_tgpa2(self.a2, self.c2, self.e2, self.g2, self.i2, self.k2)
        cgpa = calculate_cgpa(tgpa1, tgpa2)

        if tgpa1 and tgpa2 and cgpa:
            save_to_database(name, reg, tgpa1, tgpa2, cgpa)
        else:
            # Handle errors
            pass

    def reset_fields(self):
        """Resets all input fields."""
        # Reset input fields logic
        pass
