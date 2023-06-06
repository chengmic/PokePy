import customtkinter as ctk
import requests


class PokemonList(ctk.CTkFrame):
    def __init__(self, master, region):
        super().__init__(master)
        self.region = region

        # description
        self.description = ctk.CTkLabel(self, text="Select a Pokémon.")

        # call API
        url = f'https://pokeapi.co/api/v2/region/{self.region}'
        response = requests.get(url)
        data = response.json()
        
        # call API again
        url = data['pokedexes'][0]['url']
        response = requests.get(url)
        data = response.json()

        # create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, height=500)
        self.scrollable_frame.grid(row=1, column=0, padx=250)
        
        # create buttons
        self.pokemon_buttons = []

        for d in data['pokemon_entries']:
            pokemon_name = d['pokemon_species']['name']
            regional_number = d['entry_number']    # this is their regional dex number
            self.pokemon_buttons.append(ctk.CTkButton(self.scrollable_frame, text =f'{regional_number}. {pokemon_name.title()}', \
                                                      command=lambda id=regional_number: self.show_pokemon_entry(id), width=200))
    
        
        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        
        # place description
        self.description.grid(row=0, column=0, pady=(15,0))

        # place pokemon buttons
        row = 0
        column = 0
        for button in self.pokemon_buttons:
            button.grid(row=row, column=column, padx=3, pady=3)
            row += 1


        # place back button    
        self.back_button.grid(row=24, column=0, pady=10)

    # button callbacks
    def show_pokemon_entry(self, regional_number):
       self.master.show_frame('pokemon_entry', args={'back_link': 'pokemon_list', 'region': self.region, 'regional_number': regional_number})

    def go_back(self):
       self.master.show_frame('regions')