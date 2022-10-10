class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setType(self, newType):
        self.type = newType
        print("Тип автомобиля -", self.type)

    def setColor(self, newColor):
        self.color = newColor
        print("Цвет автомобиля - ", newColor)

    def setYear(self, newYear):
        self.year = newYear
        print('Год выпуска автомобиля - ', newYear)

    def carInfo(self):
        print(self.color, self.year, self.type)

mazda = Car("Белая", "Легковая", 2009)
mazda.carInfo()                         

