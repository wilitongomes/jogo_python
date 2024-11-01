# Ex ample file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screem = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da velha')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sams ms', 100, True, True)
running = True

personagem_x = fonte_quadrinhos.render('x', True, 'red')
personagem_o = fonte_quadrinhos.render('O', True, 'blue')

jogador_atual = personagem_x
rodadas = 0
tabuleiro_desenhado = False

coordenada_x = 0
coordenada_y = 0
q1 = 0
q2 = 0 
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q7 = 0 
q8 = 0 
q9 = 0
def desenha_tabuleiro(espessura, cor):
    #                                   Origem      Destino
    #                                   (x  , Y )    (x  , y) 
    pygame.draw.line(screem, cor, (175, 25), (175, 475), espessura)
    pygame.draw.line(screem, cor, (325, 25), (325, 475), espessura)
    pygame.draw.line(screem, cor, (25, 175), (475, 175), espessura)
    pygame.draw.line(screem, cor, (25, 325), (475, 325), espessura)
def faz_jogada():    
     #Primeira Linha
        global q1, q2, q3, q4, q5, q6, q7, q8, q9  
        status = True      
        if q1 == 0 and coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
            screem.blit(jogador_atual,(60,60)) #primeiro
            q1 = jogador_atual
        elif q2 == 0 and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:    
            screem.blit(jogador_atual,(215,60)) #segundo
            q2 = jogador_atual
        elif q3 == 0 and coordenada_x >= 400 and coordenada_y < 200:
            screem.blit(jogador_atual,(380,60)) #terceiro
            q3 = jogador_atual
        #Segunda Linha
        elif q4 == 0 and coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
            screem.blit(jogador_atual,(60,220)) #Quarta
            q4 = jogador_atual
        elif q5 == 0 and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y <400:  
            screem.blit(jogador_atual,(215,215)) #Quinta
            q5 = jogador_atual
        elif q6 == 0 and coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:
            screem.blit(jogador_atual,(380,210)) #Sexto
            q6 = jogador_atual
        #Terceira Linha
        elif q7 == 0 and coordenada_x < 200 and coordenada_y >= 400:
            screem.blit(jogador_atual,(60,380)) #Setimo
            q7 = jogador_atual
        elif q8 == 0 and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
            screem.blit(jogador_atual,(215,380)) #Oitavo
            q8 = jogador_atual
        elif q9 == 0 and coordenada_x >= 400 and coordenada_y >= 400:  
            screem.blit(jogador_atual,(380,380)) #Nono    
            q9 = jogador_atual
        else:
            status = False
        return status
       
while running:
    # poll for events
    # pygame.QUIT event means the user apresenta_personagemed x  to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('clicou')
            click_pos = pygame.mouse.get_pos()
            print('coordenada_x', click_pos[0])
            print('coordenada_y', click_pos[1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            if(rodadas >= 9):
                screem.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_Y = 0
                tabuleiro_desenhado = False
            if (faz_jogada()):
                rodadas = rodadas + 1
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x      

            
                
         
                  
    print(q1)
    if tabuleiro_desenhado == False:     
        desenha_tabuleiro(10, 'blue')
        q1 = 0
        q2 = 0 
        q3 = 0
        q4 = 0
        q5 = 0
        q6 = 0
        q7 = 0 
        q8 = 0 
        q9 = 0
        tabuleiro_desenhado = True
   
       
    # flip() the display to put your work on screem
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

