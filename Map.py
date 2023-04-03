class MapParams(object):
    def __init__(self):
        self.lat = 53.642277  # Координаты центра карты на старте. БГУ
        self.lon = 55.941746
        self.zoom = 14  # Масштаб карты на старте. Изменяется от 1 до 19
        self.type = "map"  # Другие значения "sat", "sat,skl"

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def get_ll(self):
        return str(self.lon) + "," + str(self.lat)

    def change_zoom(self, up=True):
        if up:
            self.zoom = min(19, self.zoom + 1)
        else:
            self.zoom = max(1, self.zoom - 1)
