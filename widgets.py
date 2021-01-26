import tkinter as tk

class Widgets():
    """A class to model the widgets."""

    def __init__(self):
        """Initialize attributes to represent the widgets."""
        self.padx, self.pady = 5, 5
        self.label_width = 20
        self.title_width = 20


    def make_entries(self, root, multipliers, spells, extra_damages):
        """Creates the entries to input values."""
        entries = {}

        self.create_title_tab(root, "Multipliers: ")
        self.create_entry_tab(root, entries, multipliers)
        self.create_title_tab(root, "Spells: ")
        self.create_entry_tab(root, entries, spells)
        self.create_title_tab(root, "Extra damage sources: ")
        self.create_entry_tab(root, entries, extra_damages)

        return entries

    def create_entry_tab(self, root, entries, fields):
        """Create the entries to input values."""
        for field in fields:
            # Frame for each field and set labels 
            # and entries inside the frame.
            row = tk.Frame(root)
            label = tk.Label(row, width=self.label_width, text=field,
                anchor='w')
            entry = tk.Entry(row, width=4)
            # Position the Label and entry in the frame
            row.pack(side=tk.TOP, fill=tk.X, padx=self.padx, pady=self.pady)
            label.pack(side=tk.LEFT)
            entry.pack(side=tk.LEFT)
            entries[field] = entry

    def create_title_tab(self, root, title=""):
        """Create the a title for entry tab."""
        row = tk.Frame(root)
        label = tk.Label(row, width=self.title_width, text=title, anchor='n')

        row.pack(side=tk.TOP, fill=tk.X, padx=self.padx, pady=self.pady)
        label.pack()

    def make_output_label(self, root, calculator):
        """Create the output label."""
        row = tk.Frame(root, bg='black', bd=2)
        label = tk.Label(row, width=self.title_width,
            text="Total damage output = ", anchor='w')
        self.total_label = tk.Label(row, text=calculator.total_damage_output,
            anchor='w')

        row.pack(side=tk.TOP, fill=tk.X, padx=self.padx, pady=self.pady)
        label.pack(fill=tk.X, side=tk.LEFT)
        self.total_label.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)        

    def make_buttons(self, root, entries, calculator):
        """Creates the Calculate, Reset and Quit buttons."""
        # Create buttons inside root.
        calculate_button = tk.Button(root, text='Calculate',
            command=lambda: self.calculate_and_update(root, entries, calculator))
        reset_button = tk.Button(root, text="Reset",
            command=lambda: self.reset_entries(entries))
        quit_button = tk.Button(root, text="Quit",
            command=root.quit)

        # Set the buttons possition.
        calculate_button.pack(side=tk.LEFT, padx=self.padx, pady=self.pady)
        reset_button.pack(side=tk.LEFT, padx=25, pady=self.pady)
        quit_button.pack(side=tk.RIGHT, padx=self.padx, pady=self.pady)

    def calculate_and_update(self, root, entries, calculator):
        """Calculate the value of total damage output and display it."""
        calculator.update_total_damage(entries)
        self.total_label['text'] = calculator.total_damage_output

    def reset_entries(self, entries):
        """Resets all entries to blank."""
        for entry in entries.values():
            entry.delete(0, tk.END)

    def prepare_interface(self, root, multipliers, spells, extra_damages,
            calculator):
        """Prepare all interface widgets."""
        entries = self.make_entries(root, multipliers, spells, extra_damages)
        self.make_output_label(root, calculator)
        self.make_buttons(root, entries, calculator)