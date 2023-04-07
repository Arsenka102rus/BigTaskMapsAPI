import pygame
import sys
import requests
import os
import Map


# Создание карты с соответствующими параметрами.
def load_map(mp):
    search_server = "https://static-maps.yandex.ru/1.x/"
    search_params = {"ll": mp.get_ll(),
                     "z": mp.zoom,
                     "l": mp.map_type}
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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Выход из программы
                running = False
            if event.type == pygame.KEYDOWN:
                mp.update(event)
                print(mp.zoom)
                print(mp.get_ll())

        # Создаем файл
        map_file = load_map(mp)
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
        os.remove(map_file)
    pygame.quit()


if __name__ == "__main__":
    main()
