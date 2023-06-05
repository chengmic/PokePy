import customtkinter as ctk
import requests

class SearchByNumber(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # description
        self.description = ctk.CTkLabel(self, text="Type the entry # of the Pokémon you would like to search.")

        # input
        self.user_input = ctk.CTkEntry(self, placeholder_text= "Entry no.", width=200, height=50)
        self.user_input.configure

        # buttons
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_for_pokemon, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # error message
        self.error_message = ctk.CTkLabel(self)

        # place widgets
        self.description.grid(row=0, column=0, padx=190, pady=(150, 40))
        self.user_input.grid(row=2, column=0, pady=10)
        self.search_button.grid(row=3, column=0, pady=10)
        self.back_button.grid(row=4, column=0, pady=10)

    # methods
    def search_for_pokemon(self):
        pokemon_number = self.user_input.get().lower()

        # check if input is valid
        if pokemon_number.isdigit() is False:
            self.error_message.configure(self, text="Error: invalid input. Only use positive integers.")
            self.error_message.grid(row=1)

        else:
            # call API
            url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}'
            response = requests.get(url)

            # check if search is valid
            if response.status_code != 200:
                self.error_message.configure(self, text="Error: Pokemon not found.")
                self.error_message.grid(row=1)
            else:
                self.show_pokemon_entry(pokemon_number)
                
    def show_pokemon_entry(self, pokemon_number):
        self.master.show_frame('pokemon_entry', args={'back_link': 'search_by_number', 'national_number': pokemon_number})

    def go_back(self):
        self.master.show_frame('search')
