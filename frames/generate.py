import customtkinter as ctk
import socket
import errno

class Generate(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.number = 0

        # declare description
        self.description = ctk.CTkLabel(self, text="Click below to generate a random Pokédex entry.")

        # declare buttons
        self.generate_button = ctk.CTkButton(self, text="Generate Pokémon", command=self.request_data, width=200, height=50)
        self.back_button = ctk.CTkButton(self, text="Go back", command=self.go_back, width=200, height=50)

        # error message
        self.error_message = ctk.CTkLabel(self)

        # place widgets
        self.description.grid(row=0, column=0, padx=(200,0), pady=(150,40))
        self.generate_button.grid(row=2, column=0, padx=(200,0), pady=10)
        self.back_button.grid(row=3, column=0, padx=(200,0), pady=10)

    # methods

    def request_data(self):
        try:
            # create a socket at client side
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # connect server and port number on local computer
            server_address = ('localhost', 10000)
            client_sock.connect(server_address)

            # receive message
            random_num = client_sock.recv(1024).decode()
            message = f'Data received: {random_num}'
            print(f'\n{message}')
            print("...Socket now closing... ")
            client_sock.close()

            # save number
            self.number = random_num
        
            # generate the page
            self.generate_entry(self.number)
        
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                self.error_message.configure(text="Error: microservice not running.")
                self.error_message.grid(row=1, pady=10)
    
    def generate_entry(self, rand_number):
        self.master.show_frame('pokemon_entry', args={'back_link': 'generate', 'national_number': rand_number})

    def go_back(self):
        self.master.show_frame('main_menu')
