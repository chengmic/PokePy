import customtkinter as ctk
from frames.main_menu import MainMenu
from frames.regions import Regions
from frames.pokemon_list import PokemonList
from frames.pokemon_entry import PokemonEntry
from frames.search import Search
from frames.search_by_name import SearchByName
from frames.search_by_number import SearchByNumber
from frames.generate import Generate

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PokePy")
        self.geometry("700x700")

        self.main_menu_frame = MainMenu(self)
        self.regions_frame = Regions(self)
        self.pokemon_list_frame = PokemonList(self)
        self.pokemon_entry_frame = PokemonEntry(self)
        self.search_frame = Search(self)
        self.search_by_name_frame = SearchByName(self)
        self.search_by_number_frame = SearchByNumber(self)
        self.generate_frame = Generate(self)
        
        self.frames = {
            'main_menu': self.main_menu_frame,
            'regions': self.regions_frame,
            'pokemon_list': self.pokemon_list_frame,
            'pokemon_entry': self.pokemon_entry_frame,
            'search': self.search_frame,
            'search_by_name': self.search_by_name_frame,
            'search_by_number': self.search_by_number_frame,
            'generate': self.generate_frame
        }

        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.regions_frame.grid(row=0, column=0, sticky="nsew")
        self.pokemon_list_frame.grid(row=0, column=0, stick="nsew")
        self.pokemon_entry_frame.grid(row=0, column=0, sticky="nsew")
        self.search_frame.grid(row=0, column=0, stick="nsew")
        self.search_by_name_frame.grid(row=0, column=0, stick="nsew")
        self.search_by_number_frame.grid(row=0, column=0, sticky="nsew")
        self.generate_frame.grid(row=0, column=0, sticky="nsew")

        frame = self.frames['main_menu']
        frame.tkraise()

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise() 

app = App()
app.mainloop()