from abc import ABC, abstractmethod


class Transport(ABC):
    brand: str
    model: str
    issue_year: int
    color: str
    mileage: int

    def __init__(self, brand, model, issue_year, color):
        self.mileage = 0
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    @abstractmethod
    def move(self, mileage, num: int):
        self.mileage = mileage
        if num > 0:
            self.mileage += num
        else:
            raise ValueError('Расстояние должно быть положительным числом')


class Car(Transport):
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, mileage, num):
        super().move(mileage,num)
        return print(f'{self.brand} {self.model} ({self.color}-{self.issue_year}) проехала {self.mileage} км')


class Airplane(Transport):
    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, mileage, num):
        super().move(mileage, num)
        return print(f'{self.brand} {self.model} ({self.color}-{self.issue_year}) пролетела  {self.mileage} км')



Car('Renault','Megane',2017,'black','dizel').move(215000,14000)
Airplane('Boeing','747',2010,'silver',2.0).move(215000,14000)
