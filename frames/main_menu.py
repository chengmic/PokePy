import customtkinter as ctk
from PIL import Image

class MainMenu(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # declare widgets
        logo = ctk.CTkImage(Image.open("img/logo.png"), size=(278,123))
        self.logo = ctk.CTkLabel(self, image=logo, text=None)

        self.button1 = ctk.CTkButton(self, text="Explore Pokédex", command=self.show_regions, width=200, height=50)
        self.button2 = ctk.CTkButton(self, text="Search for Pokémon", command=self.show_search, width=200, height=50)
        self.button3 = ctk.CTkButton(self, text="Generate Random Pokémon", command=self.show_generate, width=200, height=50)

        self.description = ctk.CTkLabel(self, text="Welcome to PokéPy.\n\nPokéPy is a python-based Pokédex application\nthat displays information about Pokémon from\n the Pokémon franchise by Nintendo, Game Freak, Creatures.\n\nUse the buttons below to navigate.", width=500)

        # place widgets
        self.logo.grid(row=0, column=0, padx=200, pady=(50,10))
        self.description.grid(row=1,column=0, padx=10, pady=(10, 20))
        self.button1.grid(row=2, column=0, padx=10, pady=10)
        self.button2.grid(row=3, column=0, padx=10, pady=10)
        self.button3.grid(row=4, column=0, padx=10, pady=10)

    # button callbacks
    def show_regions(self):
        self.master.show_frame('regions')

    def show_search(self):
        self.master.show_frame('search')

    def show_generate(self):
        self.master.show_frame('generate')