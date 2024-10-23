# Ex ample file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screem = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da velha')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sams ms', 100, True, True)
running = True

personagem_x  = fonte_quadrinhos.render('x ', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'blue')
apresenta_personagem = 0 
x = 0
y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user apresenta_personagemed x  to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou')
            click_pos = pygame.mouse.get_pos()
            print('eixo x', click_pos[0])
            print('eixo Y', click_pos[1])
            x = click_pos[0]
            y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem >=10):
                screem.fill('black')
                apresenta_personagem = 0
        #                                   Origem      Destino
        #                                   (x  , Y )    (x  , y) 
        pygame.draw.line(screem, 'white', (175, 25), (175, 475), 10)
        pygame.draw.line(screem, 'white', (325, 25), (325, 475), 10)
        pygame.draw.line(screem, 'white', (25, 175), (475, 175), 10)
        pygame.draw.line(screem, 'white', (25, 325), (475, 325), 10)

        #Primeira Linha
        if x > 0 and x < 200 and y < 200:
            screem.blit(personagem_x ,(60,60)) #primeiro
        elif x >= 200 and x < 400 and y < 200:    
            screem.blit(personagem_y,(215,60)) #segundo
        elif x >= 400 and y < 200:
            screem.blit(personagem_y,(380,60)) #terceiro
        #Segunda Linha
        elif x < 200 and y>= 200 and y< 400:
            screem.blit(personagem_x ,(60,220)) #Quarta
        elif x >= 200 and x < 400 and y>= 200 and y<400:  
            screem.blit(personagem_y,(215,215)) #Quinta
        elif x >= 400 and y>= 200 and y< 400:
             screem.blit(personagem_y,(380,210)) #Sexto
        #Terceira Linha
        elif x < 200 and y>= 400:
            screem.blit(personagem_x ,(60,380)) #Setimo
        elif x >= 200 and x < 400 and y>= 400:
            screem.blit(personagem_y,(215,380)) #Oitavo
        elif x >= 400 and y>= 400:  
            screem.blit(personagem_y,(380,380)) #Nono        
    # flip() the display to put your work on screem
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

