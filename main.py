import pygame as pg
import ToolBox

pg.init()
pg.display.set_caption('UnderPong')

while ToolBox.Game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ToolBox.Game = False
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                ToolBox.Game=False
    while ToolBox.FrontScreen == True:
        ToolBox.OptionPage = True
        ToolBox.PlayerPick = True
        ToolBox.screen.fill(ToolBox.BLACK)
        ToolBox.screen.blit(ToolBox.Logo,(40,110))
        ToolBox.StartButton.draw()
        ToolBox.OptionButton.draw()
        ToolBox.QuitButton.draw()
        pg.display.flip()
        ToolBox.clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ToolBox.FrontScreen = False
                ToolBox.Game = False
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    ToolBox.Game=False
                    ToolBox.FrontScreen = False    
            elif ToolBox.StartButton.draw():
                while ToolBox.PlayerPick == True:
                    ToolBox.screen.fill(ToolBox.BLACK)
                    ToolBox.screen.blit(ToolBox.Logo,(40,50))
                    ToolBox.OnePlayButton.draw()
                    ToolBox.TwoPlayButton.draw()
                    ToolBox.BackButton.draw()
                    pg.display.flip()
                    ToolBox.clock.tick(60)
                    for event in pg.event.get():
                        if ToolBox.OnePlayButton.draw():
                            ToolBox.PlayerPick = False
                            ToolBox.FrontScreen = False
                            while ToolBox.Level == True:
                                ToolBox.screen.fill(ToolBox.BLACK)
                                ToolBox.screen.blit(ToolBox.Logo,(40,50))
                                #This needs Code
                        if ToolBox.TwoPlayButton.draw():
                            ToolBox.PlayerPick = False
                            ToolBox.FrontScreen = False   
                        if ToolBox.BackButton.draw():
                            ToolBox.PlayerPick = False
            elif ToolBox.QuitButton.draw():
                ToolBox.Game = False
                ToolBox.FrontScreen = False
            elif ToolBox.OptionButton.draw():
                while ToolBox.OptionPage == True:
                    ToolBox.screen.fill(ToolBox.BLACK)
                    ToolBox.screen.blit(ToolBox.Option,(40,50))
                    ToolBox.BackButton.draw()
                    pg.display.flip()
                    ToolBox.clock.tick(60)
                    for event in pg.event.get():
                        if ToolBox.BackButton.draw():
                            ToolBox.OptionPage = False

    ToolBox.screen.fill(ToolBox.BLACK)
    pg.draw.line(ToolBox.screen, ToolBox.WHITE, [349, 0], [349, 500], 5)
    ToolBox.all_sprites_list.draw(ToolBox.screen)
    
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        ToolBox.paddleA.moveUp(5)
    if keys[pg.K_s]:
        ToolBox.paddleA.moveDown(5)
    if keys[pg.K_UP]:
        ToolBox.paddleB.moveUp(5)
    if keys[pg.K_DOWN]:
        ToolBox.paddleB.moveDown(5) 

    ToolBox.all_sprites_list.update()

    if ToolBox.ball.rect.x>=690:
        ToolBox.ScoreA+=1
        ToolBox.ball.rect.x = 345
        ToolBox.ball.rect.y = 195
        ToolBox.ball.velocity[0] = -ToolBox.ball.velocity[0]
    if ToolBox.ball.rect.x<=0:
        ToolBox.ScoreB +=1
        ToolBox.ball.rect.x = 345
        ToolBox.ball.rect.y = 195
        ToolBox.ball.velocity[0] = -ToolBox.ball.velocity[0]
    if ToolBox.ball.rect.y>490:
        ToolBox.ball.velocity[1] = -ToolBox.ball.velocity[1]
    if ToolBox.ball.rect.y<0:
        ToolBox.ball.velocity[1] = -ToolBox.ball.velocity[1] 
    
    if pg.sprite.collide_mask(ToolBox.ball, ToolBox.paddleA) or pg.sprite.collide_mask(ToolBox.ball, ToolBox.paddleB):
      ToolBox.ball.bounce()
    
#Display scores:
    font = pg.font.Font(None, 74)
    text = font.render(str(ToolBox.ScoreA), 1, ToolBox.WHITE)
    ToolBox.screen.blit(text, (250,10))
    text = font.render(str(ToolBox.ScoreB), 1, ToolBox.WHITE)
    ToolBox.screen.blit(text, (420,10))
#This will be character heads
    ToolBox.screen.blit(ToolBox.SansHead1,(550,10))
    ToolBox.screen.blit(ToolBox.friskHead,(50,10))
    
    pg.display.flip()

    ToolBox.clock.tick(ToolBox.Speed[ToolBox.Level])
pg.quit()