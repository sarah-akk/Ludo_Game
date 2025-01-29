from dice import Dice
from constants import Constants
from grid import Grid
from player import Player
from game import Game
from pawn import Pawn
from state import State
from rich.console import Console
import pygame


if __name__ == '__main__' :

    pygame.mixer.init()
    pygame.mixer.music.load("sounds/bg.mp3") 
    pygame.mixer.music.play(-1)  


    player1 = Player(1, 'blue', Constants().Color().BLUE, symbol="\033[94m" , is_human=True)
    player2 = Player(2, 'green', Constants().Color().GREEN, symbol="\033[92m" , is_human=False)
    player3 = Player(3, 'red', Constants().Color().RED, symbol="\033[91m", is_human=False)
    player4 = Player(4, 'yellow', Constants().Color().YELLOW, symbol="\033[93m", is_human=False)

    # player2 = None
    # player3 = None
    # player4 = None


    if(player1):
        player1.set_pawns([
                Pawn(1 + player1.get_id() * 10,2,2,color=player1.get_color(),player_id=player1.get_id(), position=(2, 2), symbol="[blue]1[/blue]"),
                Pawn(2 + player1.get_id() * 10 ,2,5,color=player1.get_color(),player_id=player1.get_id(), position=(5, 2), symbol="[blue]2[/blue]"),
                Pawn(3 + player1.get_id() * 10 ,5,2,color=player1.get_color(),player_id=player1.get_id(), position=(2, 5), symbol="[blue]3[/blue]"),
                Pawn(4 + player1.get_id() * 10 ,5,5,color=player1.get_color(),player_id=player1.get_id(), position=(5, 5), symbol="[blue]4[/blue]")
            ])
    
    if(player2):
        player2.set_pawns([
                Pawn(1 + player2.get_id() * 10 ,2,11,color=player2.get_color(),player_id=player2.get_id(), position=(11, 2), symbol="[green]1[/green]"),
                Pawn(2 + player2.get_id() * 10 ,2,14,color=player2.get_color(),player_id=player2.get_id(), position=(14, 2), symbol="[green]2[/green]"),
                Pawn(3 + player2.get_id() * 10 ,5,11,color=player2.get_color(),player_id=player2.get_id(), position=(11, 5), symbol="[green]3[/green]"),
                Pawn(4 + player2.get_id() * 10 ,5,14,color=player2.get_color(),player_id=player2.get_id(), position=(14, 5), symbol="[green]4[/green]")
            ])
    
    if(player3):
        player3.set_pawns([
                Pawn(1 + player3.get_id() * 10 ,11,11,color=player3.get_color(),player_id=player3.get_id(), position=(11, 11), symbol="[red]1[/red]"),
                Pawn(2 + player3.get_id() * 10 ,11,14,color=player3.get_color(),player_id=player3.get_id(), position=(14, 11), symbol="[red]2[/red]"),
                Pawn(3 + player3.get_id() * 10 ,14,11,color=player3.get_color(),player_id=player3.get_id(), position=(11, 14), symbol="[red]3[/red]"),
                Pawn(4 + player3.get_id() * 10 ,14,14,color=player3.get_color(),player_id=player3.get_id(), position=(14, 14), symbol="[red]4[/red]")
            ])
        
    if(player4):
        player4.set_pawns([
                Pawn(1 + player4.get_id() * 10 ,11,2,color=player4.get_color(),player_id=player4.get_id(), position=(2, 11), symbol="[yellow]1[/yellow]"),
                Pawn(2 + player4.get_id() * 10 ,11,5,color=player4.get_color(),player_id=player4.get_id(), position=(5, 11), symbol="[yellow]2[/yellow]"),
                Pawn(3 + player4.get_id() * 10 ,14,5,color=player4.get_color(),player_id=player4.get_id(), position=(5, 14), symbol="[yellow]3[/yellow]"),
                Pawn(4 + player4.get_id() * 10 ,14,2,color=player4.get_color(),player_id=player4.get_id(), position=(5, 14), symbol="[yellow]4[/yellow]")
            ])

    grid = Grid(player1, player2 , player3  , player4 )


    Game(player1 if player1 else None, player2 if player2 else None , player3 if player3 else None , player4 if player4 else None, grid).play()