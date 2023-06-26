# pygame 2.0.0 (SDL 2.0.12, python 3.8.5)

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        print("fire！")
    elif keys[pygame.K_LEFT]:
        print("left move")
    elif keys[pygame.K_RIGHT]:
        print("right move")
        
    # 更新游戏对象的位置、动画等
    # player.update()
    # enemy.update()
    
    # 绘制/渲染对象到屏幕上
    screen.fill((0, 0, 0))
    # player.draw(screen)
    # enemy.draw(screen)
    
    # 刷新屏幕并等待下一帧
    pygame.display.flip()
    clock.tick(60)  # 最大帧率为60帧每秒


pygame.quit()