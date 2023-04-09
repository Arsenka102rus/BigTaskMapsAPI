import pygame


class MapParams(object):
    def __init__(self):
        self.lat = 53.642277  # Координаты центра карты на старте. БГУ
        self.lon = 55.941746
        self.zoom = 2  # Масштаб карты на старте. Изменяется от 1 до 19
        self.map_types = ["map", "sat", "sat,skl"]
        self.map_type = "map"  # Другие значения "sat", "sat,skl"
        self.update_step()

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def get_ll(self):
        if self.zoom == 1:
            return "0,0"
        return str(self.lon) + "," + str(self.lat)

    def update_step(self):
        self.step = 0.001 * 2 ** (15 - self.zoom)

    def update(self, event):
        if event.key == pygame.K_PAGEDOWN:  # Изменение масштаба
            self.zoom = max(1, self.zoom - 1)
            self.update_step()
        elif event.key == pygame.K_PAGEUP:
            self.zoom = min(19, self.zoom + 1)
            self.update_step()
        if event.key == pygame.K_LEFT:  # Изменение центра
            self.lon -= self.step
            if self.lon < -180:
                self.lon = -180 + self.step
        if event.key == pygame.K_RIGHT:
            self.lon += self.step
            if self.lon > 180:
                self.lon = 180 - self.step
        if event.key == pygame.K_UP:
            self.lat += self.step
            if self.lat > 70:
                self.lat = 70
        if event.key == pygame.K_DOWN:
            self.lat -= self.step
            if self.lat < -70:
                self.lat = -70

