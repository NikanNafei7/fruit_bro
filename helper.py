import pygame
import pygame_gui

pygame.init()

size = (800, 600)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Shop Example")

manager = pygame_gui.UIManager(size)
clock = pygame.time.Clock()

# پول و جون بازیکن
player_gold = 100
player_hp = 100

# دکمه‌های شاپ
buy_hp_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 100), (150, 50)),
    text='Buy +20 HP (50 gold)',
    manager=manager
)

buy_sword_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 200), (150, 50)),
    text='Buy Sword (75 gold)',
    manager=manager
)

gold_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((100, 50), (200, 30)),
    text=f'Gold: {player_gold}',
    manager=manager
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == buy_hp_button and player_gold >= 50:
                    player_gold -= 50
                    player_hp += 20
                    gold_label.set_text(f'Gold: {player_gold}')
                    print(f'Bought HP. HP = {player_hp}')

                if event.ui_element == buy_sword_button and player_gold >= 75:
                    player_gold -= 75
                    gold_label.set_text(f'Gold: {player_gold}')
                    print('Bought Sword!')

        manager.process_events(event)

    manager.update(time_delta)

    window.fill((30, 30, 30))
    manager.draw_ui(window)
    pygame.display.flip()

pygame.quit()
