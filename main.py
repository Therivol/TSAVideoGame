from game.Game import Game


if __name__ == "__main__":

    game = Game()
    game.start()

    while not game.should_close:
        game.calculate_dt()
        game.poll_events()
        game.early_update()
        game.update()
        game.late_update()
        game.draw()
