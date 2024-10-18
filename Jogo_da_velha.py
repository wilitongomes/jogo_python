# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screem = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da velha')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sams ms', 100, True, True)
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'blue')
cor_fundo = 1 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo >3):
                cor_fundo = 1
        
        pygame.draw.line(screem, 'white', (175, 25), (175, 475), 10)
        pygame.draw.line(screem, 'white', (325, 25), (325, 475), 10)
        pygame.draw.line(screem, 'white', (25, 175), (475, 175), 10)
        pygame.draw.line(screem, 'white', (25, 325), (475, 325), 10)

        screem.blit(personagem_x,(50,60))
        screem.blit(personagem_y,(210,60))
        screem.blit(personagem_y,(400,60))
        
    # flip() the display to put your work on screem
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

