import pygame
import sys
import pygame_gui
import requests
import os
import Map
import map_switcher


# Создание карты с соответствующими параметрами.
def load_map(mp):
    search_server = "https://static-maps.yandex.ru/1.x/"
    search_params = {"ll": mp.get_ll(),
                     "z": mp.zoom,
                     "l": mp.map_type,
                     "size": "600,450"}
    response = requests.get(search_server, params=search_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = Map.MapParams()
    manager = pygame_gui.UIManager((600, 450))
    switcher = map_switcher.Swticher(relative_rect=pygame.Rect((470, 10), (130, 25)), manager=manager, text="Сменить режим")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Выход из программы
                running = False
            if event.type == pygame.KEYDOWN:
                mp.update(event)
                print(mp.zoom)
                print(mp.get_ll())
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    switcher.change_map_type(mp)
            manager.process_events(event)

        # Создаем файл
        map_file = load_map(mp)
        # Рисуем картинку, загружаемую из только что созданного файла.
        manager.update(1)
        screen.blit(pygame.image.load(map_file), (0, 0))
        manager.draw_ui(screen)
        pygame.display.flip()
        os.remove(map_file)
    pygame.quit()


if __name__ == "__main__":
    main()
