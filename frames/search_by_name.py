import customtkinter as ctk
import requests

class SearchByName(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # declare description
        self.description = ctk.CTkLabel(self, text="Type the name of the Pokémon you would like to search below.")

        # declare input
        self.user_input = ctk.CTkEntry(self, placeholder_text= "Pokémon name", width=200, height=50)

        # declare buttons
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_for_pokemon, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        self.description.grid(row=0, column=0)
        self.user_input.grid(row=1, column=0, pady=10)
        self.search_button.grid(row=2, column=0, pady=10)
        self.back_button.grid(row=3, column=0, pady=10)

    # methods
    def search_for_pokemon(self):
        pokemon_name = self.user_input.get().lower()

        if pokemon_name:
            # call API
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
            response = requests.get(url)

            # check if search is valid
            if response.status_code == 200:
                data = response.json()
                print(f"Pokemon found: {data['name']}")
            else:
                error_message = f"Pokemon '{pokemon_name}' not found."
                print(error_message)
    
    def go_back(self):
        self.master.show_frame('main_menu')
