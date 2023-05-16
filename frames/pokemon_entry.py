import customtkinter as ctk
from PIL import Image, ImageTk
import requests
import io



class PokemonEntry(ctk.CTkFrame):
    def __init__(self, master, region, entry_no):
        super().__init__(master)
        
        self.region = region
        self.entry_no = entry_no

        # call API for region
        url = f'https://pokeapi.co/api/v2/region/{self.region}'
        response = requests.get(url)
        data = response.json()
        
        # call API again to get region dex
        url = data['pokedexes'][0]['url']
        response = requests.get(url)
        data = response.json()
        dex_id = data['id']
        
        # get regional dex endpoint
        url = f'https://pokeapi.co/api/v2/pokedex/{dex_id}'
        response = requests.get(url)
        data = response.json()

        # get national entry number
        entry_url = data['pokemon_entries'][self.entry_no - 1]['pokemon_species']['url']
        response = requests.get(entry_url)
        data = response.json()

        self.national_number = data['id']


        # Name
        name = data['name']
        self.name= ctk.CTkLabel(self, text=name.title())


        # Entry no
        self.entry_number = ctk.CTkLabel(self, text=f"No. {self.national_number}")

        # image
        url = f'https://pokeapi.co/api/v2/pokemon/{self.national_number}'
        response =requests.get(url)
        data = response.json()

        img_url = data['sprites']['other']['official-artwork']['front_default']

        response = requests.get(img_url)
        img_data = response.content

        img_data = Image.open(io.BytesIO(img_data))

        img = ctk.CTkImage(img_data, size=(200,200))
        self.image = ctk.CTkLabel(self, image=img, text=None)

        # category
        url = f'https://pokeapi.co/api/v2/pokemon-species/{self.national_number}'
        response = requests.get(url)
        data = response.json()

        for d in data['genera']:
            if d['language']['name'] == 'en':
                genus = d['genus']
                break
        self.category = ctk.CTkLabel(self, text=genus)
        
        # description
        for d in data['flavor_text_entries']:
            if d['language']['name'] == 'en':
                description = d['flavor_text']
                break
        self.description =ctk.CTkLabel(self, text=description)

        # type
        url = f'https://pokeapi.co/api/v2/pokemon/{self.national_number}'
        response =requests.get(url)
        data = response.json()
        
        type_list =[]
        for d in data['types']:
            type = d['type']['name']
            type_list.append(type)

        self.type= ctk.CTkLabel(self, text=f"Type: {type_list}")

        # delcare show more button
        self.more_button = ctk.CTkButton(self, text="Show Alternate Description", width=200, height=50)

        # delcare back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        
        # place widgets 
        row=0

        self.name.grid(row=row, column=0)
        self.entry_number.grid(row=row+1, column=0)
        self.image.grid(row=row+2, column=0)
        self.category.grid(row=row+3, column=0)
        self.description.grid(row=row+4, column=0)
        self.type.grid(row=row+5, column=0)

        self.more_button.grid(row=row+6, column=0, pady=10)
        self.back_button.grid(row=row+7, column=0, pady=10)

    # button callbacks
    def go_back(self):
        self.master.show_frame('pokemon_list', args ={'region' : self.region})