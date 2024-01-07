import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(self) -> None:
        self.name = ""
        self.symbol = ''
    
    def choose_name(self) -> None:
        while True:
            name = input("please, enter your Name (latters only): ")
            if(name.isalpha()):
                self.name = name
                break
            else:
                print(f"invalid Name!, please use latters only")

    def choose_symbol(self) -> None:
        while True:
            symbol = input("please, enter your Name (single latters): ")
            if(symbol.isalpha() and len(symbol) == 1):
                self.symbol = symbol.upper()
                break
            else:
                print(f"invalid symbol!, please use a single latters only")
            
class Menu:
    def display_main_menu(self):
        print("Welcom to tic-tac-toe Game")
        print("1- start Game")
        print("2- Quit Game")
        while(True):
            choise = input("Enter your Choise (1 or 2): ")
            if(Menu.isvalid_choise(choise)):
                return choise
            else:
                print("invalid choise use (1 or 2): ")
        clear_screen()

    def display_end_menu(self):
        print("Game Over")
        print("1- start New Game")
        print("2- Quit Game")
        while(True):
            choise = input("Enter your Choise (1 or 2)")
            if(Menu.isvalid_choise(choise)):
                return choise
            else:
                print("invalid choise use (1 or 2)")
        clear_screen()

    @classmethod
    def isvalid_choise(cls, choise) -> bool:
        if(len(choise) == 1 and (choise == "1" or choise == "2")):
            return True
        else:
            return False
 
class Board:
    def __init__(self) -> None:
        self.board = [str(i) for i in range(1, 10)]

    def display_Board(self):
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))
            if(i<6):
                print('-' * 5)

    def update_board(self, index, symbol) -> bool:
        if(self.is_valid_move(index)):
            self.board[index - 1] = symbol
            # self.display_Board()
            return True
        return False

    def is_valid_move(self, index) -> bool:
        return self.board[index - 1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self) -> None:
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    
    def start_game(self):
        choise = self.menu.display_main_menu()
        if(choise == "1"):
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for index, player in enumerate(self.players, 1):
            print(f"player {index} enter your data")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while(True):
            self.play_turn()
            if(self.check_win() or self.check_draw()):
                choise = self.menu.display_end_menu()
                if(choise == "1"):
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            clear_screen()
                

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_Board()
        while(True):
            player_selection = input("Enter your selection box number (1-9): ")
            if(player_selection.isdigit() and 0 < int(player_selection) < 10  and self.board.update_board(int(player_selection), player.symbol)):
                break
            else:
                print("invaled number use unselected boxes between 1 and 9.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index    

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
            
        return False

    

    def check_draw(self):
        return all(not i.isdigit() for i in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


    def quit_game(self):
        print("Thank you for Playing")


game = Game()
game.start_game()