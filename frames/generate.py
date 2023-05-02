import customtkinter as ctk

class Generate(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # declare description
        self.description = ctk.CTkLabel(self, text="Click below to generate a random Pokémon entry.")


        # declare buttons
        self.generate_button = ctk.CTkButton(self, text="Generate Pokémon", width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        row = 0
        self.description.grid(row=row, column=0)
        self.generate_button.grid(row=row+1, column=0)
        self.back_button.grid(row=row+2, column=0, pady=10)

    # button callbacks
    def go_back(self):
        self.master.show_frame('main_menu')
