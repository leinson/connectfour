import pygame
import ui

def main():
    pygame.init()
    window_size = [720, 650]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("ConnectFour")

    ui.ui_pygame(screen)

if __name__ == '__main__':
    main()