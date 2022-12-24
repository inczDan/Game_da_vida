import sys, pygame

# parametro de inicialização
size = width, height = 1000, 564

BLACK = (0, 0, 0)

# construindo a janela do game
def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Joguin da vida")

    while 1:
        # capturando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("End.")
                sys.exit()

        # refresh
        screen.fill(BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
