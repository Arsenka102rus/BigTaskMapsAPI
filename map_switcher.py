import pygame_gui


class Swticher(pygame_gui.elements.UIButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maps = ["Спутник", "Гибрид", "Схема"]
        self.cur_type = 0

    def change_map_type(self, map):
        self.cur_type += 1
        if self.cur_type > 2:
            self.cur_type = 0
        map.map_type = map.map_types[self.cur_type]
        self.set_text(self.maps[self.cur_type])
        self.update(1)
