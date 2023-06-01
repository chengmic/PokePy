import customtkinter as ctk
import requests

class SearchByName(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # description
        self.description = ctk.CTkLabel(self, text="Type the name of the Pokémon you would like to search below.")

        # input
        self.user_input = ctk.CTkEntry(self, placeholder_text= "Pokémon name", width=200, height=50)

        # buttons
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_for_pokemon, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # error message
        self.error_message = ctk.CTkLabel(self, text="Error.")

        # place widgets
        self.description.grid(row=0, column=0)
        self.user_input.grid(row=2, column=0, pady=10)
        self.search_button.grid(row=3, column=0, pady=10)
        self.back_button.grid(row=4, column=0, pady=10)

    # methods
    def search_for_pokemon(self):
        pokemon_name = self.user_input.get().lower()

        # check if input is valid
        if pokemon_name.isalpha() is False or not pokemon_name:
            self.error_message.configure(self, text = "Error: invalid input. Only use characters A-z.")
            self.error_message.grid(row=1,pady=10)

        else:
            # call API
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
            response = requests.get(url)

            # if pokemon not found
            if response.status_code != 200:
                self.error_message.configure(self, text= "Error: Pokemon not found.")
                self.error_message.grid(row=1,pady=10)
            
            # check if search is valid
            else:
                self.show_pokemon_entry(pokemon_name)
            
    def show_pokemon_entry(self, pokemon_name):
        self.master.show_frame('pokemon_entry', args={'back_link': 'search_by_name', 'pokemon_name': pokemon_name})
    
    def go_back(self):
        self.master.show_frame('main_menu')
