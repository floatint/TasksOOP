class GameItem:

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, val):
        self.__val = val

    @property
    def is_available(self):
        return self.__is_avail

    @property
    def is_deleted(self):
        return self.__is_deleted

    @is_deleted.setter
    def is_deleted(self, v):
        self.__is_deleted = v

    def __init__(self, is_avail):
        self.__val = 0
        self.__is_avail = is_avail
        self.__is_deleted = False
