import random
import os
import colorama
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
reset = colorama.Fore.RESET
light_white = colorama.Fore.LIGHTWHITE_EX

class Field:
    def __init__(self, size):
        self.size = size
        self.number_of_ships = self.size
        self.number_of_alive_ships = self.number_of_ships
        self.grid = []
        for _ in range(self.size):
            self.grid.append([])
        for i in range(self.size):
            for i in range(self.size):
                self.grid[i].append(None)

    def show_my_field(self):
        print("Ваше поле:")
        print(light_white + "  A B C D E F G H")
        for i in range(self.size):
            print(light_white + f"{i+1} {self.grid[i][0]} {self.grid[i][1]} {self.grid[i][2]} {self.grid[i][3]} {self.grid[i][4]} {self.grid[i][5]} {self.grid[i][6]} {self.grid[i][7]}".replace("None", blue + "⌀" + reset).replace("S", green + "⌂" + reset).replace("X", red + "⁘" + reset).replace("C", light_white + "※" + reset))
    def show_computer_field(self):
        print("Поле компьютера:")
        print(light_white + "  A B C D E F G H")
        for i in range(self.size):
            print(light_white + f"{i+1} {self.grid[i][0]} {self.grid[i][1]} {self.grid[i][2]} {self.grid[i][3]} {self.grid[i][4]} {self.grid[i][5]} {self.grid[i][6]} {self.grid[i][7]}".replace("None", blue + "⌀" + reset).replace("S", blue + "⌀" + reset).replace("X", red + "⁘" + reset).replace("C", light_white + "※" + reset) + reset)
    def place_ships_randomly(self):
        for i in range(self.size):
            self.grid[i][random.randint(0, self.size-1)] = "S"

class BattleshipGame:
    def __init__(self):
        self.user_field = Field(8)
        self.computer_field = Field(8)
    def play(self):
        self.user_field.place_ships_randomly()
        self.computer_field.place_ships_randomly()
        while self.computer_field.number_of_alive_ships > 0 and self.user_field.number_of_alive_ships > 0:            
            self.user_field.show_my_field()
            self.computer_field.show_computer_field()
            try:
                user_y_coordinates = int(input("Введите номер РЯДА, в который Вы хотите выстрелить: "))-1
                user_x_coordinates = input("Введите букву КОЛОНКИ, в которую Вы хотите выстрелить: ").upper().strip()
                coords = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
                user_x_coordinates = coords[user_x_coordinates]
                self.check_players_coords(user_x_coordinates, user_y_coordinates)
            except KeyError:
                print("Введено некорректное значение, Вы пропускаете ход!")
            except ValueError:
                print("Введено некорректное значение, Вы пропускаете ход!")
            except IndexError:
                print("Введено некорректное значение! Вы пропускаете ход!")
            computer_x_coord = random.randint(0, self.user_field.size-1)
            computer_y_coord = random.randint(0, self.user_field.size-1)
            while not self.check_computers_coords(computer_x_coord, computer_y_coord):
                computer_x_coord = random.randint(0, self.user_field.size-1)
                computer_y_coord = random.randint(0, self.user_field.size-1)
            input("Для продолжения нажмите Enter.")
            os.system("cls")
        if self.user_field.number_of_alive_ships > 0:
            print(f"Вы победили! Компьютер завалил {self.user_field.number_of_ships - self.user_field.number_of_alive_ships} кор. из {self.user_field.number_of_ships}.")
        else:
            print("Вы потерпели разгромное поражение. Противник усмехается, глядя Вам в лицо.")
    def check_players_coords(self, x, y):
        if self.computer_field.grid[y][x] == "S":
            self.computer_field.grid[y][x] = "X"
            self.computer_field.number_of_alive_ships -= 1
            print("Вы попали и затопили вражеский корабль.")
        elif self.computer_field.grid[y][x] == "X" or self.computer_field.grid[y][x] == "C":
            print("Вы уже стреляли в это поле, Вы пропускаете ход.")
        else:
            self.computer_field.grid[y][x] = "C"
            print("Вы промахнулись!")
    def check_computers_coords(self, x, y):
        if self.user_field.grid[y][x] == "S":
            self.user_field.grid[y][x] = "X"
            self.user_field.number_of_alive_ships -= 1
            print("Компьютер завалил Ваш корабль!")
            return True
        elif self.user_field.grid[y][x] == "C" or self.user_field.grid[y][x] == "X":
            return False
        elif "X" in self.user_field.grid[y]:
            return False
        else:
            self.user_field.grid[y][x] = "C"
            print("Компьютер выстрелил, но промахнулся!")
            return True


if __name__ == "__main__":
    game = BattleshipGame()
    game.play()