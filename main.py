import sys
import game

def main():
    Game = game.game()
    
    Game.setUp()
    while Game.isRunning() == True:
        Game.HandleEvents()
        Game.Update()
        Game.Render()
        Game.FinishCalculations()
    Game.Exit()
    return 0

sys.exit(main())