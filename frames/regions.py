import customtkinter as ctk
import requests 


class Regions(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # description
        self.description = ctk.CTkLabel(self, text="Select the region you would like to see Pokémon for.")

        # Call API
        response = requests.get("https://pokeapi.co/api/v2/region/")
        data = response.json()
        regions = data['results']

        # create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, height=500)
        self.scrollable_frame.grid(row=1, column=0, padx=250)

        # location buttons
        self.region_buttons = []
        number = 0

        for region in regions:
            region_name = region['name']
            number += 1
            self.region_buttons.append(ctk.CTkButton(self.scrollable_frame, text=f'{str(number)}. {region_name.title()}',\
                                                      command=lambda region=region_name: self.show_pokemon_list(region), width=200, height=50))

        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        self.description.grid(row=0, column=0, pady=(15,0))
        
        row = 1
        for button in self.region_buttons:
            button.grid(row=row, column=0, pady=5)
            row += 1
            
        self.back_button.grid(row=row+2, column=0, pady=10)

    # button callbacks
    def show_pokemon_list(self, region):
        self.master.show_frame('pokemon_list', args={'region': region})

    def go_back(self):
        self.master.show_frame('main_menu')