import customtkinter as ctk
import requests

class Regions(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # description
        self.description = ctk.CTkLabel(self, text="Select the region you would like to see Pokémon for.")

        # Call API
        response = requests.get("https://pokeapi.co/api/v2/region/")
        data = response.json()
        regions = data['results']

        # location buttons
        self.region_buttons = []
        for region in regions:
            self.region_buttons.append(ctk.CTkButton(self, text=region['name'].title(), command=self.show_pokemon_list, width=200, height=50))

        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        row = 0

        self.description.grid(row=row, column=0)

        for button in self.region_buttons:
            button.grid(row=row+1, column=0, pady=5)
            row += 1
            
        self.back_button.grid(row=row+2, column=0, pady=10)

    # button callbacks
    def show_pokemon_list(self):
        self.master.show_frame('pokemon_list')

    def go_back(self):
        self.master.show_frame('main_menu')