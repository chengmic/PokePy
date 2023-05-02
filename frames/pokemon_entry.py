import customtkinter as ctk
from PIL import Image

class PokemonEntry(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Name
        self.name = ctk.CTkLabel(self, text="Bidoof")

        # Entry no
        self.entry_no= ctk.CTkLabel(self, text="No. 399")

        # image
        img = ctk.CTkImage(Image.open("img/bidoof.png"), size=(200,200))
        self.image = ctk.CTkLabel(self, image=img, text=None)

        # category
        self.category = ctk.CTkLabel(self, text="Category: Plump Mouse")
        
        # description
        self.description =ctk.CTkLabel(self, text="Description: With nerves of steel, nothing can perturb it. It is more agile and active than it appears.")

        # type
        self.type= ctk.CTkLabel(self, text="Type: Normal")

        # delcare show more button
        self.more_button = ctk.CTkButton(self, text="Show more", width=200, height=50)

        # delcare back button
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)
        
        # place widgets 
        row=0

        self.name.grid(row=row, column=0)
        self.entry_no.grid(row=row+1, column=0)
        self.image.grid(row=row+2, column=0)
        self.category.grid(row=row+3, column=0)
        self.description.grid(row=row+4, column=0)
        self.type.grid(row=row+5, column=0)

        self.more_button.grid(row=row+6, column=0, pady=10)
        self.back_button.grid(row=row+7, column=0, pady=10)

    # button callbacks
    def go_back(self):
        self.master.show_frame('pokemon_list')