import sys
import game

def main():
    Game = game.game()
    Game.setUp()
    
    while Game.running == True:
        Game.HandleEvents()
        Game.Update()
        Game.Render()
    Game.Exit()
    return 0
sys.exit(main())