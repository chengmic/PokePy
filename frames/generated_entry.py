import customtkinter as ctk
import requests
import io
from PIL import Image


class GeneratedEntry(ctk.CTkFrame):
    def __init__(self, master, generated_number):
        super().__init__(master)
        
        # get entry number
        self.entry_number = generated_number

        # name
        url = f'https://pokeapi.co/api/v2/pokemon/{self.entry_number}'
        response =requests.get(url)
        data = response.json()
        name = data['species']['name']
        self.name = ctk.CTkLabel(self, text=name.title())
        self.name.grid(row=0, column=0)
        
        # entry number
        id = data['id']
        self.id = ctk.CTkLabel(self,text=f'No. {str(id)}')
        self.id.grid(row=1, column=0)

        # image
        url = f'https://pokeapi.co/api/v2/pokemon/{self.entry_number}'
        response =requests.get(url)
        data = response.json()
        
        img_url = data['sprites']['other']['official-artwork']['front_default']
        response = requests.get(img_url)
        img_data = response.content

        img_data = Image.open(io.BytesIO(img_data))
        img = ctk.CTkImage(img_data, size=(200,200))

        self.image = ctk.CTkLabel(self, image=img, text=None)
        self.image.grid(row=2, column=0)

        # category
        url = f'https://pokeapi.co/api/v2/pokemon/{self.entry_number}'
        response = requests.get(url)
        data = response.json()
        
        url = data['species']['url']
        response = requests.get(url)
        data = response.json()

        for d in data['genera']:
            if d['language']['name'] == 'en':
                genus = d['genus']
                break

        self.category = ctk.CTkLabel(self, text=genus)
        self.category.grid(row=3, column=0)

        # description
        url = f'https://pokeapi.co/api/v2/pokemon/{self.entry_number}'
        response = requests.get(url)
        data = response.json()
        
        url = data['species']['url']
        response = requests.get(url)
        data = response.json()
        
        description = None
        for d in data['flavor_text_entries']:
            if d['language']['name'] == 'en':
                description = d['flavor_text']
                break
        
        self.description =ctk.CTkLabel(self, text=description)
        self.description.grid(row=4, column=0)
       
        # type
        url = f'https://pokeapi.co/api/v2/pokemon/{self.entry_number}'
        response =requests.get(url)
        data = response.json()
        
        type_list =[]
        for d in data['types']:
            type = d['type']['name']
            type_list.append(type)

        self.type= ctk.CTkLabel(self, text=f"Type: {', '.join(type_list).title()}")
        self.type.grid(row=5, column=0)

        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        self.back_button.grid(row=6, column=0)
    
    # methods
    def go_back(self):
        self.master.show_frame('generate')
