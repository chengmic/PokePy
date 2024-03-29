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
        self.resizable(False, False)

        self.current_frame = MainMenu(self)
        self.current_frame.pack(fill=ctk.BOTH, expand=True)

    def show_frame(self, frame_name, args=None):
        self.current_frame.destroy()
        if frame_name == 'main_menu':
            self.current_frame = MainMenu(self)
            
        elif frame_name == 'regions':
            self.current_frame = Regions(self)

        elif frame_name == 'pokemon_list':
            self.current_frame = PokemonList(self, args['region'])

        elif frame_name == 'pokemon_entry':
            if 'regional_number' in args.keys() and 'region' in args.keys():
                self.current_frame = PokemonEntry(self, args['back_link'], region=args['region'], regional_number=args['regional_number'])

            elif 'national_number' in args.keys():
                self.current_frame = PokemonEntry(self, args['back_link'], national_number=args['national_number'])

            elif 'pokemon_name' in args.keys():
                self.current_frame = PokemonEntry(self, args['back_link'], pokemon_name=args['pokemon_name'])

        elif frame_name == 'search':
            self.current_frame = Search(self)

        elif frame_name == 'search_by_name':
            self.current_frame = SearchByName(self)

        elif frame_name == 'search_by_number':
            self.current_frame = SearchByNumber(self)

        elif frame_name == 'generate':
            self.current_frame = Generate(self)

        self.current_frame.pack(fill=ctk.BOTH, expand=True)

app = App()
app.mainloop()