'''
import tkinter as tk
import random
from tkinter import PhotoImage
from .board import Board
from .data import data_loader  # Importuj funkcję loadera

# Klasa CheckersApp odpowiada za interfejs użytkownika
class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()
        self.selected_piece = None
        self.possible_moves = []
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()
        self.canvas.bind("<Button-1>", self.on_click)
        self.historical_games = data_loader()  # Ładowanie danych historycznych
       
       
    def __init__(self, master):
        self.master = master
        self.board = Board()  # Inicjalizacja planszy
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie płótna o rozmiarach 600x600
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        # Rysowanie planszy
        self.draw_board()

        # Rysowanie pionków
        self.draw_pieces() 
        
def on_click(self, event):
    row = event.y // 75
    col = event.x // 75
    
    # Ensure the click is within the board limits
    if row < 0 or row >= len(self.board.grid) or col < 0 or col >= len(self.board.grid[row]):
        return  # Ignore clicks outside the board

    clicked_piece = self.board.grid[row][col]

    if clicked_piece and clicked_piece == 'W':  # Check if it's a white piece
        self.selected_piece = (row, col)
        self.possible_moves = self.board.get_possible_moves(row, col)
        self.draw_board()
        self.draw_pieces()
    elif (row, col) in self.possible_moves:
        # Move the piece to the selected position
        self.board.move_piece(self.selected_piece[0], self.selected_piece[1], row, col)
        self.selected_piece = None
        self.possible_moves = []

        # Let the computer take its turn
        self.handle_computer_move()

    def draw_board(self):
        # Rysowanie szachownicy, gdzie każde pole ma rozmiar 75x75 (600 / 8)
        self.canvas.delete("all")  # Czyści planszę przed rysowaniem
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col * 75, row * 75,
                                              (col + 1) * 75, (row + 1) * 75,
                                              fill=color)
                # Zaznacz możliwe ruchy na planszy, tylko dla białych pionków
                if self.selected_piece and self.board.grid[self.selected_piece[0]][self.selected_piece[1]] == 'W':
                    if (row, col) in self.possible_moves:
                        self.canvas.create_rectangle(col * 75, row * 75,
                                                      (col + 1) * 75, (row + 1) * 75,
                                                      fill='green', stipple='gray50')

    def draw_pieces(self):
        # Rysowanie pionków na planszy z efektem 3D
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5  # Środek pola w osi x
                    y = row * 75 + 37.5  # Środek pola w osi y
                    if piece == 'B':
                        self.draw_3d_piece(x, y, 'black', 'darkgray')
                    else:
                        self.draw_3d_piece(x, y, 'white', 'lightgray')

    def draw_3d_piece(self, x, y, color, shadow_color):
        # Rysowanie pionka z efektem 3D
        # Pionek z cieniem
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color)
        # Pionek główny
        self.canvas.create_oval(x - 27, y - 27, x + 27, y + 27, fill=color, outline='black')

def handle_computer_move(self):
    computer_move = self.get_computer_move()
    if computer_move:
        from_row, from_col, (to_row, to_col) = computer_move
        self.board.move_piece(from_row, from_col, to_row, to_col)

    # Draw the board and pieces after all moves
    self.draw_board()
    self.draw_pieces()

def get_computer_move(self):
    # Load historical games if not already done
    if not hasattr(self, 'historical_games'):
        self.historical_games = data_loader()

    # Randomly select a game and a move
    import random
    random_game = random.choice(self.historical_games)
    random_move = random.choice(random_game)

    # Extract the starting and ending coordinates
    from_row, from_col = random_move[0]
    to_row, to_col = random_move[1]

    # Ensure the move is valid before returning it
    if self.board.is_valid_move(from_row, from_col, to_row, to_col):
        return (from_row, from_col, (to_row, to_col))
    else:
        return None  # If the move is not valid, return None



# Funkcja główna do uruchamiania aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Ustawienie rozmiaru okna na 600x600
    root.title("Warcaby")
    icon_path = "img/icon.png"  # Upewnij się, że ta ścieżka jest poprawna
    icon_image = PhotoImage(file=icon_path)  # Tworzenie instancji PhotoImage
    root.call("wm", "iconphoto", root._w, icon_image)  # Ustawienie ikony
    app = CheckersApp(root)
    root.mainloop()

# Klasa CheckersApp odpowiada za interfejs użytkownika
class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()  # Inicjalizacja planszy
        self.selected_piece = None  # Aktualnie wybrany pionek
        self.possible_moves = []    # Lista możliwych ruchów dla wybranego pionka
        self.historical_games = data_loader()  # Ładowanie danych historycznych
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie płótna o rozmiarach 600x600
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        # Rysowanie planszy
        self.draw_board()

        # Rysowanie pionków
        self.draw_pieces()

        # Dodanie obsługi kliknięć
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        # Rysowanie szachownicy, gdzie każde pole ma rozmiar 75x75 (600 / 8)
        self.canvas.delete("all")  # Czyści planszę przed rysowaniem
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col * 75, row * 75,
                                              (col + 1) * 75, (row + 1) * 75,
                                              fill=color)
                # Zaznacz możliwe ruchy na planszy, tylko dla białych pionków
                if self.selected_piece and self.board.grid[self.selected_piece[0]][self.selected_piece[1]] == 'W':
                    if (row, col) in self.possible_moves:
                        self.canvas.create_rectangle(col * 75, row * 75,
                                                      (col + 1) * 75, (row + 1) * 75,
                                                      fill='green', stipple='gray50')

    def draw_pieces(self):
        # Rysowanie pionków na planszy z efektem 3D
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5  # Środek pola w osi x
                    y = row * 75 + 37.5  # Środek pola w osi y
                    if piece == 'B':
                        self.draw_3d_piece(x, y, 'black', 'darkgray')
                    else:
                        self.draw_3d_piece(x, y, 'white', 'lightgray')

    def draw_3d_piece(self, x, y, color, shadow_color):
        # Rysowanie pionka z efektem 3D
        # Pionek z cieniem
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color)
        # Pionek główny
        self.canvas.create_oval(x - 27, y - 27, x + 27, y + 27, fill=color, outline='black')

def on_click(self, event):
    # Pobieramy wiersz i kolumnę klikniętego miejsca na planszy
    row = event.y // 75
    col = event.x // 75
    clicked_piece = self.board.grid[row][col]

    if clicked_piece:
        # Jeśli kliknięto pionek, zaznacz go i pokaż możliwe ruchy, tylko dla białych pionków
        if clicked_piece == 'W':
            self.selected_piece = (row, col)
            self.possible_moves = self.board.get_possible_moves(row, col)
        else:
            self.selected_piece = None
            self.possible_moves = []
    elif self.selected_piece and (row, col) in self.possible_moves:
        # Jeśli kliknięto zielone pole, przesuń pionek
        old_row, old_col = self.selected_piece
        self.board.grid[row][col] = 'W'  # Przenieś pionka na nowe pole
        self.board.grid[old_row][old_col] = None  # Usuń pionka z starego pola

        # Zresetuj wybór i możliwe ruchy
        self.selected_piece = None
        self.possible_moves = []

        # Rysuj planszę i pionki po ruchu gracza
        self.draw_board()
        self.draw_pieces()

        # Komputer wykonuje ruch po gracza
        self.handle_computer_move()

def handle_computer_move(self):
    # Pobierz ruch komputera
    computer_move = self.get_computer_move()

    if computer_move:
        from_row, from_col, (to_row, to_col) = computer_move
        # Sprawdź czy ruch jest poprawny zanim go wykonasz
        if self.board.is_valid_move(from_row, from_col, to_row, to_col):
            self.board.move_piece(from_row, from_col, to_row, to_col)
        
    # Rysuj planszę i pionki po ruchu komputera
    self.draw_board()
    self.draw_pieces()

def get_computer_move(self):
    # Wczytaj historyczne gry, jeśli jeszcze tego nie zrobiłeś
    if not hasattr(self, 'historical_games'):
        self.historical_games = data_loader()

    # Losowo wybierz grę i ruch
    import random
    random_game = random.choice(self.historical_games)
    random_move = random.choice(random_game)

    # Wyodrębnij współrzędne startowe i końcowe
    from_row, from_col = random_move[0]
    to_row, to_col = random_move[1]

    # Sprawdź, czy ruch jest poprawny przed zwróceniem go
    if self.board.is_valid_move(from_row, from_col, to_row, to_col):
        return (from_row, from_col, (to_row, to_col))
    else:
        return None  # Jeśli ruch nie jest poprawny, zwróć None



# Funkcja główna do uruchamiania aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Ustawienie rozmiaru okna na 600x600
    root.title("Warcaby")
    icon_path = "img/icon.png"  # Upewnij się, że ta ścieżka jest poprawna
    icon_image = PhotoImage(file=icon_path)  # Tworzenie instancji PhotoImage
    root.call("wm", "iconphoto", root._w, icon_image)  # Ustawienie ikony
    app = CheckersApp(root)
    root.mainloop()


import tkinter as tk
import random
from tkinter import PhotoImage
from .board import Board
from .data import data_loader  # Importuj funkcję loadera


# Klasa CheckersApp odpowiada za interfejs użytkownika
class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()  # Inicjalizacja planszy
        self.selected_piece = None  # Aktualnie wybrany pionek
        self.possible_moves = []    # Lista możliwych ruchów dla wybranego pionka
        self.historical_games = data_loader()  # Ładowanie danych historycznych
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie płótna o rozmiarach 600x600
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        # Rysowanie planszy
        self.draw_board()

        # Rysowanie pionków
        self.draw_pieces()

        # Dodanie obsługi kliknięć
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        # Rysowanie szachownicy, gdzie każde pole ma rozmiar 75x75 (600 / 8)
        self.canvas.delete("all")  # Czyści planszę przed rysowaniem
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col * 75, row * 75,
                                              (col + 1) * 75, (row + 1) * 75,
                                              fill=color)
                # Zaznacz możliwe ruchy na planszy, tylko dla białych pionków
                if self.selected_piece and self.board.grid[self.selected_piece[0]][self.selected_piece[1]] == 'W':
                    if (row, col) in self.possible_moves:
                        self.canvas.create_rectangle(col * 75, row * 75,
                                                      (col + 1) * 75, (row + 1) * 75,
                                                      fill='green', stipple='gray50')

    def draw_pieces(self):
        # Rysowanie pionków na planszy z efektem 3D
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5  # Środek pola w osi x
                    y = row * 75 + 37.5  # Środek pola w osi y
                    if piece == 'B':
                        self.draw_3d_piece(x, y, 'black', 'darkgray')
                    else:
                        self.draw_3d_piece(x, y, 'white', 'lightgray')

    def draw_3d_piece(self, x, y, color, shadow_color):
        # Rysowanie pionka z efektem 3D
        # Pionek z cieniem
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color)
        # Pionek główny
        self.canvas.create_oval(x - 27, y - 27, x + 27, y + 27, fill=color, outline='black')

    def on_click(self, event):
        # Pobieramy wiersz i kolumnę klikniętego miejsca na planszy
        row = event.y // 75
        col = event.x // 75

        # Ensure the click is within the board limits
        if row < 0 or row >= len(self.board.grid) or col < 0 or col >= len(self.board.grid[row]):
            return  # Ignore clicks outside the board

        clicked_piece = self.board.grid[row][col]

        if clicked_piece:
            # Jeśli kliknięto pionek, zaznacz go i pokaż możliwe ruchy, tylko dla białych pionków
            if clicked_piece == 'W':
                self.selected_piece = (row, col)
                self.possible_moves = self.board.get_possible_moves(row, col)
            else:
                self.selected_piece = None
                self.possible_moves = []
        elif self.selected_piece and (row, col) in self.possible_moves:
            # Jeśli kliknięto zielone pole, przesuń pionek
            old_row, old_col = self.selected_piece
            self.board.grid[row][col] = 'W'  # Przenieś pionka na nowe pole
            self.board.grid[old_row][old_col] = None  # Usuń pionka z starego pola

            # Zresetuj wybór i możliwe ruchy
            self.selected_piece = None
            self.possible_moves = []

            # Rysuj planszę i pionki po ruchu gracza
            self.draw_board()
            self.draw_pieces()

            # Komputer wykonuje ruch po gracza
            self.handle_computer_move()

    def handle_computer_move(self):
        # Pobierz ruch komputera
        computer_move = self.get_computer_move()

        if computer_move:
            from_row, from_col, (to_row, to_col) = computer_move
            # Sprawdź czy ruch jest poprawny zanim go wykonasz
            if self.board.is_valid_move(from_row, from_col, to_row, to_col):
                self.board.move_piece(from_row, from_col, to_row, to_col)

        # Rysuj planszę i pionki po ruchu komputera
        self.draw_board()
        self.draw_pieces()

    def get_computer_move(self):
        # Wczytaj historyczne gry, jeśli jeszcze tego nie zrobiłeś
        if not hasattr(self, 'historical_games'):
            self.historical_games = data_loader()

        # Losowo wybierz grę i ruch
        random_game = random.choice(self.historical_games)
        random_move = random.choice(random_game)

        # Wyodrębnij współrzędne startowe i końcowe
        from_row, from_col = random_move[0]
        to_row, to_col = random_move[1]

        # Sprawdź, czy ruch jest poprawny przed zwróceniem go
        if self.board.is_valid_move(from_row, from_col, to_row, to_col):
            return (from_row, from_col, (to_row, to_col))
        else:
            return None  # Jeśli ruch nie jest poprawny, zwróć None


# Funkcja główna do uruchamiania aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Ustawienie rozmiaru okna na 600x600
    root.title("Warcaby")
    icon_path = "img/icon.png"  # Upewnij się, że ta ścieżka jest poprawna
    icon_image = PhotoImage(file=icon_path)  # Tworzenie instancji PhotoImage
    root.call("wm", "iconphoto", root._w, icon_image)  # Ustawienie ikony
    app = CheckersApp(root)
    root.mainloop()

import tkinter as tk
import random
from tkinter import PhotoImage
from .board import Board
from .data import data_loader  # Importuj funkcję loadera


# Klasa CheckersApp odpowiada za interfejs użytkownika
class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()  # Inicjalizacja planszy
        self.selected_piece = None  # Aktualnie wybrany pionek
        self.possible_moves = []    # Lista możliwych ruchów dla wybranego pionka
        self.historical_games = data_loader()  # Ładowanie danych historycznych
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie płótna o rozmiarach 600x600
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        # Rysowanie planszy
        self.draw_board()

        # Rysowanie pionków
        self.draw_pieces()

        # Dodanie obsługi kliknięć
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        # Rysowanie szachownicy, gdzie każde pole ma rozmiar 75x75 (600 / 8)
        self.canvas.delete("all")  # Czyści planszę przed rysowaniem
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col * 75, row * 75,
                                              (col + 1) * 75, (row + 1) * 75,
                                              fill=color)
                # Zaznacz możliwe ruchy na planszy
                if self.selected_piece and (row, col) in self.possible_moves:
                    self.canvas.create_rectangle(col * 75, row * 75,
                                                  (col + 1) * 75, (row + 1) * 75,
                                                  fill='green', stipple='gray50')

    def draw_pieces(self):
        # Rysowanie pionków na planszy z efektem 3D
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5  # Środek pola w osi x
                    y = row * 75 + 37.5  # Środek pola w osi y
                    if piece == 'B':
                        self.draw_3d_piece(x, y, 'black', 'darkgray')
                    else:
                        self.draw_3d_piece(x, y, 'white', 'lightgray')

    def draw_3d_piece(self, x, y, color, shadow_color):
        # Rysowanie pionka z efektem 3D
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color)
        self.canvas.create_oval(x - 27, y - 27, x + 27, y + 27, fill=color, outline='black')

    def on_click(self, event):
        # Pobieramy wiersz i kolumnę klikniętego miejsca na planszy
        row = event.y // 75
        col = event.x // 75

        # Ensure the click is within the board limits
        if row < 0 or row >= len(self.board.grid) or col < 0 or col >= len(self.board.grid[row]):
            return  # Ignore clicks outside the board

        clicked_piece = self.board.grid[row][col]

        if clicked_piece == 'W':  # If the player clicks on a white piece
            # Select the piece and show possible moves
            self.selected_piece = (row, col)
            self.possible_moves = self.board.get_possible_moves(row, col)
        elif self.selected_piece and (row, col) in self.possible_moves:
            # If a valid move was clicked, move the piece
            old_row, old_col = self.selected_piece
            self.board.grid[row][col] = 'W'  # Przenieś pionek na nowe pole
            self.board.grid[old_row][old_col] = None  # Usuń pionka z poprzedniego pola

            # Reset the selection and possible moves
            self.selected_piece = None
            self.possible_moves = []

            # Let the computer take its turn
            self.handle_computer_move()

        # Redraw the board and pieces after every click
        self.draw_board()
        self.draw_pieces()

    def handle_computer_move(self):
        # Pobierz ruch komputera
        computer_move = self.get_computer_move()

        if computer_move:
            from_row, from_col, (to_row, to_col) = computer_move
            # Sprawdź czy ruch jest poprawny zanim go wykonasz
            if self.board.is_valid_move(from_row, from_col, to_row, to_col):
                self.board.move_piece(from_row, from_col, to_row, to_col)

        # Rysuj planszę i pionki po ruchu komputera
        self.draw_board()
        self.draw_pieces()

    def get_computer_move(self):
        # Wczytaj historyczne gry, jeśli jeszcze tego nie zrobiłeś
        if not hasattr(self, 'historical_games'):
            self.historical_games = data_loader()

        # Losowo wybierz grę i ruch
        random_game = random.choice(self.historical_games)
        random_move = random.choice(random_game)

        # Wyodrębnij współrzędne startowe i końcowe
        from_row, from_col = random_move[0]
        to_row, to_col = random_move[1]

        # Sprawdź, czy ruch jest poprawny przed zwróceniem go
        if self.board.is_valid_move(from_row, from_col, to_row, to_col):
            return (from_row, from_col, (to_row, to_col))
        else:
            return None  # Jeśli ruch nie jest poprawny, zwróć None


# Funkcja główna do uruchamiania aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Ustawienie rozmiaru okna na 600x600
    root.title("Warcaby")
    icon_path = "img/icon.png"  # Upewnij się, że ta ścieżka jest poprawna
    icon_image = PhotoImage(file=icon_path)  # Tworzenie instancji PhotoImage
    root.call("wm", "iconphoto", root._w, icon_image)  # Ustawienie ikony
    app = CheckersApp(root)
    root.mainloop()
'''

import tkinter as tk
import random
from tkinter import PhotoImage
from .board import Board
from .data import data_loader  # Assuming both scripts are in the same directory

class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()  # Inicjalizacja planszy
        self.selected_piece = None  # Aktualnie wybrany pionek
        self.possible_moves = []    # Lista możliwych ruchów dla wybranego pionka

        # Load historical moves using the data_loader function
        self.historical_moves = data_loader()

        # You can use self.historical_moves for analyzing or playing games

        self.current_move = 0
        self.create_widgets()

    def create_widgets(self):
        # Tworzenie płótna o rozmiarach 600x600
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        # Rysowanie planszy
        self.draw_board()

        # Rysowanie pionków
        self.draw_pieces()

        # Dodanie obsługi kliknięć
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        # Rysowanie szachownicy, gdzie każde pole ma rozmiar 75x75 (600 / 8)
        self.canvas.delete("all")  # Czyści planszę przed rysowaniem
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.canvas.create_rectangle(col * 75, row * 75,
                                              (col + 1) * 75, (row + 1) * 75,
                                              fill=color)
                # Zaznacz możliwe ruchy na planszy
                if self.selected_piece and (row, col) in self.possible_moves:
                    self.canvas.create_rectangle(col * 75, row * 75,
                                                  (col + 1) * 75, (row + 1) * 75,
                                                  fill='green', stipple='gray50')

    def draw_pieces(self):
        # Rysowanie pionków na planszy z efektem 3D
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5  # Środek pola w osi x
                    y = row * 75 + 37.5  # Środek pola w osi y
                    if piece == 'B':
                        self.draw_3d_piece(x, y, 'black', 'darkgray')
                    else:
                        self.draw_3d_piece(x, y, 'white', 'lightgray')

    def draw_3d_piece(self, x, y, color, shadow_color):
        # Rysowanie pionka z efektem 3D
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color)
        self.canvas.create_oval(x - 27, y - 27, x + 27, y + 27, fill=color, outline='black')

    def on_click(self, event):
        # Pobieramy wiersz i kolumnę klikniętego miejsca na planszy
        row = event.y // 75
        col = event.x // 75

        # Ensure the click is within the board limits
        if row < 0 or row >= len(self.board.grid) or col < 0 or col >= len(self.board.grid[row]):
            return  # Ignore clicks outside the board

        clicked_piece = self.board.grid[row][col]

        if clicked_piece == 'W':  # If the player clicks on a white piece
            # Select the piece and show possible moves
            self.selected_piece = (row, col)
            self.possible_moves = self.board.get_possible_moves(row, col)
        elif self.selected_piece and (row, col) in self.possible_moves:
            # If a valid move was clicked, move the piece
            old_row, old_col = self.selected_piece
            self.board.grid[row][col] = 'W'  # Przenieś pionek na nowe pole
            self.board.grid[old_row][old_col] = None  # Usuń pionka z poprzedniego pola

            # Reset the selection and possible moves
            self.selected_piece = None
            self.possible_moves = []

            # Let the computer take its turn
            self.handle_computer_move()

        # Redraw the board and pieces after every click
        self.draw_board()
        self.draw_pieces()

    def handle_computer_move(self):
        # Get the next historical move from the dataset
        if self.current_move < len(self.historical_moves):
            from_coords, to_coords = self.historical_moves[self.current_move]

            # Convert the coordinates from string to integer
            from_coords = (int(from_coords[0]), int(from_coords[1]))
            to_coords = (int(to_coords[0]), int(to_coords[1]))

            # Perform the move on the board
            self.board.move_piece(from_coords[0], from_coords[1], to_coords[0], to_coords[1])
            self.current_move += 1

        # Rysuj planszę i pionki po ruchu komputera
        self.draw_board()
        self.draw_pieces()


# Funkcja główna do uruchamiania aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Ustawienie rozmiaru okna na 600x600
    root.title("Warcaby")
    app = CheckersApp(root)
    root.mainloop()
