import tkinter as tk

from widgets import Widgets
from calculator import Calculator


# Create the window and set its name.
root = tk.Tk()
root.title("Il'gynoth otk calculator")

# Define entries for each field.
multipliers = ["Spell Damage", "Mo'arg Artificer"]
spells = ["Felscream Blast", "Eye Beam", "Soul Cleave"]
extra_damages = ["Hero Attack", "Life Steal? (y/n)",
    "Taunt in the way? (y/n)", "Board attack"]

# Make an instance of the widgets and calculator.
widgets = Widgets()
calculator = Calculator()

# Create labels, entries and buttons.
widgets.prepare_interface(root, multipliers, spells, extra_damages,
    calculator)

# Run the window.
root.mainloop()