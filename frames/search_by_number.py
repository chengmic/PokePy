import customtkinter as ctk
import requests

class SearchByNumber(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # declare description
        self.description = ctk.CTkLabel(self, text="Type the entry number of the Pokémon you would like to search below.")

        # declare input
        self.user_input = ctk.CTkEntry(self, placeholder_text= "Entry no.", width=200, height=50)
        self.user_input.configure

        # declare buttons
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_for_pokemon, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        row = 0
        self.description.grid(row=row, column=0)
        self.user_input.grid(row=row+1, column=0, pady=10)
        self.search_button.grid(row=row+2, column=0, pady=10)
        self.back_button.grid(row=row+3, column=0, pady=10)

    # methods
    def search_for_pokemon(self):
        pokemon_number = self.user_input.get().lower()

        if pokemon_number:
            # call API
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}'
            response = requests.get(url)

            # check if search is valid
            if response.status_code == 200:
                data = response.json()
                print(f"Pokemon found: No. {data['id']}: {data['name']}")
            else:
                error_message = f"Pokemon '{pokemon_number}' not found."
                print(error_message)

    def go_back(self):
        self.master.show_frame('main_menu')
