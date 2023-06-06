import customtkinter as ctk
from PIL import Image
import requests
import io



class PokemonEntry(ctk.CTkFrame):
    def __init__(self, master, back_link, region=None, regional_number=None, national_number=None, pokemon_name=None):
        super().__init__(master)
        self.back_link = back_link
        self.region = region
        self.regional_number = regional_number
        self.national_number = national_number
        self.pokemon_name = pokemon_name

        if self.region:
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
            entry_url = data['pokemon_entries'][self.regional_number - 1]['pokemon_species']['url']
            response = requests.get(entry_url)
            data = response.json()
            self.national_number = data['id']       # this is the national id

        if self.pokemon_name:
            # call API using pokemon name and get national id
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_name}'
            response = requests.get(url)
            data = response.json()
            self.national_number = data['id']

        if self.national_number:
            pass

        # ---------- /pokemon-species ENDPOINT ----------
        url = f'https://pokeapi.co/api/v2/pokemon-species/{self.national_number}'
        response = requests.get(url)
        data = response.json()
        
        # category
        for d in data['genera']:
            if d['language']['name'] == 'en':
                genus = d['genus']
                break

        self.category = ctk.CTkLabel(self, text=genus)

        # description
        description = None
        for d in data['flavor_text_entries']:
            if d['language']['name'] == 'en':
                description = d['flavor_text']
                break
        
        self.description =ctk.CTkLabel(self, text=description)


        
        # ----------- /pokemon ENDPOINT ----------
        url = f'https://pokeapi.co/api/v2/pokemon/{self.national_number}'
        response =requests.get(url)
        data = response.json()

        # name
        name = data['species']['name']
        self.name = ctk.CTkLabel(self, text=name.title())
        
        # id
        id = data['id']
        self.id = ctk.CTkLabel(self,text=f'No. {str(id)}')

        # image
        img_url = data['sprites']['other']['official-artwork']['front_default']
        img_response = requests.get(img_url)
        img_data = img_response.content

        img_data = Image.open(io.BytesIO(img_data))
        img = ctk.CTkImage(img_data, size=(200,200))

        self.image = ctk.CTkLabel(self, image=img, text=None)
       
        # type
        type_list =[]
        for d in data['types']:
            type = d['type']['name']
            type_list.append(type)

        self.type= ctk.CTkLabel(self, text=f"Type: {', '.join(type_list).title()}")

        # height and weight
        height = data['height'] / 10
        weight = data['weight'] / 10

        self.height = ctk.CTkLabel(self, text = f"Height: {height}m")
        self.weight = ctk.CTkLabel(self, text = f"Weight: {weight}kg")

        # base stats
        hp = data['stats'][0]['base_stat']
        atk = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        sp_atk = data['stats'][3]['base_stat']
        sp_def = data['stats'][4]['base_stat']
        sp = data['stats'][5]['base_stat']

        # abilities and hidden ability
        ability_list = []
        hidden_ability = None

        abilities = data['abilities']

        for ability in abilities:
            if ability['is_hidden'] is False:
                ability_name = ability['ability']['name']
                ability_list.append(ability_name)

            else:
                hidden_ability = ability['ability']['name']

        self.abilities= ctk.CTkLabel(self, text=f"Abilities: {', '.join(ability_list).title()}")
        
        if hidden_ability:
            self.hidden_ability = ctk.CTkLabel(self, text=f"Hidden Ability: {hidden_ability.title()}")
        else: 
            self.hidden_ability = ctk.CTkLabel(self, text=f"Hidden Ability: None")

        # base stat
        self.base_stats = ctk.CTkLabel(self, text=f"Base Stats: \nHP - {hp} \nAttack - {atk} \n" \
                                       f"Defense: {defense} \nSpecial Attack - {sp_atk} \n" \
                                       f"Special Defense - {sp_def} \nSpeed - {sp}")

        # show more button
        self.info_button = ctk.CTkButton(self, text="Show More Info", width=200, height=50, command=self.toggle_info)

        # back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        
        # place widgets
        self.name.grid(row=0, column=0, padx=(55,30), pady=(15,0))
        self.id.grid(row=1, column=0, padx=(55,30))
        self.image.grid(row=2, column=0, padx=(55,30))
        self.category.grid(row=3, column=0, padx=(55,30), pady=5)
        self.description.grid(row=4, column=0, padx=(55,30), pady=5)
        self.type.grid(row=5, column=0, padx=(55,30), pady=5)

        self.info_button.grid(row=6, column=0, padx=(55,30), pady=10)
        self.back_button.grid(row=7, column=0, padx=(55,30), pady=20)


    # methods
    def toggle_info(self):
        if self.info_button.cget("text") == "Show More Info":
            # change button text
            self.info_button.configure(text="Show Less Info")

            # place additional info
            self.height.grid(row=0, column=1, pady=(15,0))
            self.weight.grid(row=1, column=1)
            self.base_stats.grid(row=2, column=1)
            self.abilities.grid(row=3, column=1)
            self.hidden_ability.grid(row=4, column=1)

        else:
            # change button text
            self.info_button.configure(text="Show More Info")

            # remove additional info
            self.height.grid_forget()
            self.weight.grid_forget()
            self.base_stats.grid_forget()
            self.abilities.grid_forget()
            self.hidden_ability.grid_forget()

    def go_back(self):
        self.master.show_frame(self.back_link, args ={'region' : self.region})