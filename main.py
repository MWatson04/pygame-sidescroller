import engine

engine.display.pygame.init()
engine_obj = engine.Engine()
engine.display.pygame.display.set_caption("Pixel Scroller")

while True:
    engine_obj.run_game()
    