import customtkinter as ctk

class PokemonList(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # description
        self.description = ctk.CTkLabel(self, text="Select a Pokémon.")

        # pokemon buttons
        pokemons = ['Bulbasaur', 'Ivysaur', 'Venasaur']
        self.pokemon_buttons = []
        for pokemon in pokemons:
            self.pokemon_buttons.append(ctk.CTkButton(self, text=pokemon, command=self.show_pokemon_entry, width=200, height=50))

        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        
        # place description
        row = 0

        self.description.grid(row=row, column=0)

        # place pokemon buttons
        for button in self.pokemon_buttons:
            button.grid(row=row+1, column=0, padx=5, pady=5)
            row += 1

        # place back button    
        self.back_button.grid(row=row+2, column=0, pady=10)

    # button callbacks
    def show_pokemon_entry(self):
        self.master.show_frame('pokemon_entry')

    def go_back(self):
        self.master.show_frame('regions')