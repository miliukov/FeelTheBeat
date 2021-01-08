import pygame
import os
import sys

pygame.font.init()
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')
pygame.display.set_icon(pygame.image.load('data/note.png'))
mouse_pos = (0, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def motion():
    flag = False
    if mouse_pos[0] in range(30, 215):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (29, 135, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(266, 447):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (265, 137, 184, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(502, 686):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (501, 136, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(756, 939):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (755, 136, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(32, 213):
        if mouse_pos[1] in range(274, 372):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (31, 274, 213, 370), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)
    else:
        flag = False
        all_sprites.draw(screen)


class BackGround(pygame.sprite.Sprite):
    image = load_image('menu.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = BackGround.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        all_sprites.draw(screen)
        all_sprites.update()


class JBR:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(140, 240):
                os.startfile('main.pyw')


class AOBTD:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                os.startfile('main.pyw')


class DM:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                os.startfile('main.pyw')


class BG:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                os.startfile('main.pyw')


class MSKWYDITD:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                os.startfile('main.pyw')


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    background = BackGround()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                JBR.click('')
        motion()
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
