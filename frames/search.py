import customtkinter as ctk

class Search(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # declare description
        self.description = ctk.CTkLabel(self, text="Select how you would like to search for a Pokémon.")


        # declare buttons
        self.search_by_name_button = ctk.CTkButton(self, text="Search by Name", command=self.show_search_by_name, width=200, height=50)
        self.search_by_number_button = ctk.CTkButton(self, text="Search by Number", command=self.show_search_by_number, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # place widgets
        row = 0
        self.description.grid(row=row, column=0)
        self.search_by_name_button.grid(row=row + 1, column=0, pady=10)
        self.search_by_number_button.grid(row=row+2, column=0, pady=10)
        self.back_button.grid(row=row+3, column=0, pady=10)

    # button callbacks
    def show_search_by_name(self):
        self.master.show_frame('search_by_name')

    def show_search_by_number(self):
        self.master.show_frame('search_by_number')
        
    def go_back(self):
        self.master.show_frame('main_menu')