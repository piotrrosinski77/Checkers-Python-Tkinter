import tkinter as tk
from tkinter import PhotoImage
from .board import Board
from .data import data_loader
from .ai import CheckersAIModel
import math


class CheckersApp:
    def __init__(self, master):
        self.master = master
        self.board = Board()
        self.selected_piece = None
        self.possible_moves = []
        self.player_turn = True

        self.model = CheckersAIModel()
        self.historical_moves = data_loader()
        self.current_move = 0

        self.create_widgets()
        self.train_model()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=600, height=600)
        self.canvas.pack()

        self.draw_board()
        self.draw_pieces()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(
                    col * 75, row * 75, (col + 1) * 75, (row + 1) * 75, fill=color
                )

                if self.selected_piece and (row, col) in self.possible_moves:
                    self.canvas.create_rectangle(
                        col * 75,
                        row * 75,
                        (col + 1) * 75,
                        (row + 1) * 75,
                        fill="green",
                        stipple="gray50",
                    )

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    x = col * 75 + 37.5
                    y = row * 75 + 37.5
                    if piece == "B":
                        self.draw_3d_piece(x, y, "black", "darkgray")
                    else:
                        self.draw_3d_piece(x, y, "white", "lightgray")

    def draw_3d_piece(self, x, y, color, shadow_color):
        self.canvas.create_oval(
            x - 30, y - 30, x + 30, y + 30, fill=shadow_color, outline=shadow_color
        )
        self.canvas.create_oval(
            x - 27, y - 27, x + 27, y + 27, fill=color, outline="black"
        )

    def on_click(self, event):
        if not self.player_turn:
            print("Computer's turn - please wait.")
            return

        row = event.y // 75
        col = event.x // 75

        if (
            row < 0
            or row >= len(self.board.grid)
            or col < 0
            or col >= len(self.board.grid[row])
        ):
            return

        clicked_piece = self.board.grid[row][col]

        if clicked_piece == "W":
            self.selected_piece = (row, col)
            self.possible_moves = self.board.get_possible_moves(row, col)
            print(f"Player selected piece at {self.selected_piece}")
            print(f"with moves {self.possible_moves}")
        elif self.selected_piece and (row, col) in self.possible_moves:
            old_row, old_col = self.selected_piece
            self.board.grid[row][col] = "W"
            self.board.grid[old_row][old_col] = None

            self.selected_piece = None
            self.possible_moves = []

            self.player_turn = False
            print("Player's move completed, switching to computer's turn.")
            self.draw_board()
            self.draw_pieces()

            self.master.after(1000, self.handle_computer_move)

        self.draw_board()
        self.draw_pieces()

    def position_to_coords(self, position):
        row = (position - 1) // 4
        col = ((position - 1) % 4) * 2 + (1 if (row % 2 == 0) else 0)
        print(f"Converted position {position} to coordinates ({row}, {col})")
        return row, col

    def handle_computer_move(self):
        move = self.model.generate_valid_move(self.board.grid)
        print(f"Computer's move: {move}")
        self.process_move(move, "B")
        self.current_move += 1

        self.player_turn = True
        print("Computer's move completed, switching to player's turn.")
        self.draw_board()
        self.draw_pieces()

    def process_move(self, segment, piece_color):
        print(f"Processing move segment: {segment} for piece color {piece_color}")

        if isinstance(segment, list):
            for part in segment:
                self.process_single_move(part, piece_color)
        else:
            self.process_single_move(segment, piece_color)

    def train_model(self):
        self.model.train_model(self.historical_moves)

    def process_single_move(self, move, piece_color):
        if "x" in move:
            
            positions = move.split("x")
            from_pos = int(positions[0])
            
            for to_pos_str in positions[1:]:
                
                to_pos = int(to_pos_str)

                if from_pos in (
                    5,
                    6,
                    7,
                    8,
                    13,
                    14,
                    15,
                    16,
                    21,
                    22,
                    23,
                    24,
                    29,
                    30,
                    31,
                    32,
                ):

                    capture_pos = int(math.floor((from_pos + to_pos) / 2))

                else:

                    capture_pos = int(math.ceil((from_pos + to_pos) / 2))

                capture_coords = self.position_to_coords(capture_pos)

                if piece_color == "B":
                    print(f"Removing captured piece at {capture_coords}")
                    self.board.remove_piece(capture_coords[0], capture_coords[1])

                from_coords = self.position_to_coords(from_pos)
                to_coords = self.position_to_coords(to_pos)

                self.board.move_piece(
                    from_coords[0], from_coords[1], to_coords[0], to_coords[1]
                )
                from_pos = to_pos
        else:
            from_pos, to_pos = map(int, move.split("-"))
            from_coords = self.position_to_coords(from_pos)
            to_coords = self.position_to_coords(to_pos)
            self.board.move_piece(
                from_coords[0], from_coords[1], to_coords[0], to_coords[1]
            )

        self.draw_board()
        self.draw_pieces()

# TO DO:
# IMPORTANT!!!
# - Add a way for the player to remove a piece from the board
# - Add a way for the player to move back not only forward

# optional:
# - Add a way for the player to reset the board to its initial state
# - Add a way for the player to undo the last move
# - Add a way for the player to redo the last move
# - Add a way for the player to save the current game state to a file
# - Add a way for the player to load a game state from a file
# - Change the color of the possible moves (it's much too dark)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Checkers")
    icon_path = "img/icon.png"
    icon_image = PhotoImage(file=icon_path)
    root.call("wm", "iconphoto", root._w, icon_image)
    app = CheckersApp(root)
    root.mainloop()
