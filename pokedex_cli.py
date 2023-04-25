import pyfiglet
import climage
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static, Label, ContentSwitcher, Input



class MainMenu(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self) -> ComposeResult:
        # welcome message
        yield Label("\nWelcome to\n" + pyfiglet.figlet_format("PokedexCLI"))
        yield Label("PokedexCLI is a terminal based pokedex application that displays information about Pokemon \nbased on the Pokemon franchise by Nintendo, Gamefreak, and Creatures.\n\n")
        yield Label("Use the buttons below to navigate.\n")
        
        # main menu buttons
        yield Button("Explore Pokedex", id="explore_page")
        yield Button("Search for Pokemon", id="search_page")
        yield Button("Generate Random Pokemon", id="generate_page")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class ExplorePage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self) -> ComposeResult:
        # welcome message
        yield Label("You selected EXPLORE POKEDEX. Please select the region you would like to see Pokemon for. \n")
        yield Button("Kanto", id="kanto")
        yield Button("Go Back", id="main_menu")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class SearchPage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self) -> ComposeResult:
         yield Label("You selected SEARCH POKEMON. Select how you would like to search for Pokemon. \n")
         yield Button("By name", id= "search_by_name_page")
         yield Button("By number (national dex no.)", id= "search_by_number_page")
         yield Button("Go back", id="main_menu")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class GeneratePage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self) -> ComposeResult:
         yield Label("You selected GENERATE RANDOM POKEMON. Click below to generate a random Pokedex entry (includes Pokemon from all regions). \n")
         yield Button("Generate Pokemon", id= "random_entry_page")
         yield Button("Go back", id="main_menu")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class PokemonListPage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    
    def compose(self):
        # message
        yield Label("Select a Pokemon below to see its Pokedex entry. \n")

        # create pokemon buttons
        pokemon_list = ['bulbasaur', 'ivysaur', 'venasaur']
        id_list = ['entry_page', 'page_2', 'page_3']

        for i in range(len(pokemon_list)):
            yield Button(pokemon_list[i], id=id_list[i])

        yield Label(" \n")      # add whitespace between last button

        # back button
        yield Button("Go back", id="explore_page")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class EntryPage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self):
        # no. and name
        yield Label("001")
        yield Label("Bulbasaur")

        # display image
        pokemon_image = climage.convert("test_image.png", width=25)
        yield Label(pokemon_image)

        # text
        yield Label("Type: GRASS, POISON")
        yield Label("There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger. \n")
        
        # buttons
        yield Button("Display More Information")
        yield Button("Go back", id="kanto")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class SearchByNamePage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self):
        yield Label("Type below to look up a Pokemon by name. \n")
        yield Input(placeholder="Pokemon name")

        # buttons
        yield Label(" \n\n")
        yield Button("Search")
        yield Button("Go back", id="search_page")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id

class SearchByNumberPage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self):
        yield Label("Type below to look up a Pokemon by their number. \n")
        yield Input(placeholder="entry no.")

        # buttons
        yield Label(" \n\n")
        yield Button("Search")
        yield Button("Go back", id="search_page")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id


class RandomEntryPage(Container):
    def __init__(self, content_switcher, **kwargs):
        super().__init__(**kwargs)
        self.content_switcher = content_switcher

    def compose(self):
        yield Label("No. 001")
        yield Label("Bulbasaur")

        pokemon_image = climage.convert("test_image.png", width=25)
       
        yield Label(pokemon_image)
        yield Label("Type: GRASS, POISON")
        yield Label("There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger. \n")
        
        yield Button("Display More Information")

        yield Label(" \n\n")
        yield Button("Generate another Pokemon")
        yield Button("Go back", id="kanto")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.content_switcher.current = event.button.id



class PokedexApp(App):
   
    def compose(self) -> ComposeResult:

        with ContentSwitcher(initial="main_menu") as content_switcher:  
            yield MainMenu(id="main_menu", content_switcher=content_switcher)
            yield ExplorePage(id="explore_page", content_switcher=content_switcher)
            yield SearchPage(id="search_page", content_switcher=content_switcher)
            yield GeneratePage(id="generate_page", content_switcher=content_switcher)
            yield PokemonListPage(id="kanto", content_switcher=content_switcher)
            yield EntryPage(id="entry_page", content_switcher=content_switcher)
            yield SearchByNamePage(id="search_by_name_page", content_switcher=content_switcher)
            yield SearchByNumberPage(id="search_by_number_page", content_switcher=content_switcher)
            yield RandomEntryPage(id="random_entry_page", content_switcher=content_switcher)

if __name__ == "__main__":
    app = PokedexApp()
    app.run()