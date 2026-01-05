import pygame
from network import Network
from player import Player

pygame.init()

FONT = pygame.font.Font(None, 64)

width = 800
height = 800
window = pygame.display.set_mode((width, height))


def main():
    run = True
    clock = pygame.time.Clock()

    nickname = input("Nickname: ")
    
    network = Network(nickname)
    player = network.getObject()

    while run:
        clock.tick(60)
        window.fill((255, 255, 255))

        entities = network.send(player)
        if not entities == None:
            for entity in entities:
                entity.draw(window)

        player.update()

        player.draw(window)

        render = FONT.render(f"{player.nickname}'s screen", False, (0, 0, 0))
        window.blit(render, (0, 0))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

main()
