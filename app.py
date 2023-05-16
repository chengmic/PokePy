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

        self.current_frame = MainMenu(self)
        self.current_frame.pack()

    def show_frame(self, frame_name, args=None):
        self.current_frame.destroy()
        if frame_name == 'main_menu':
            self.current_frame = MainMenu(self)
            
        elif frame_name == 'regions':
            self.current_frame = Regions(self)

        elif frame_name == 'pokemon_list':
            self.current_frame = PokemonList(self, args['region'])

        elif frame_name == 'pokemon_entry':
            self.current_frame = PokemonEntry(self, args['region'], args['entry_no'])

        elif frame_name == 'search':
            self.current_frame = Search(self)

        elif frame_name == 'search_by_name':
            self.current_frame = SearchByName(self)

        elif frame_name == 'search_by_number':
            self.current_frame = SearchByNumber(self)

        elif frame_name == 'generate':
            self.current_frame = Generate(self)

        self.current_frame.pack(expand = True)

app = App()
app.mainloop()