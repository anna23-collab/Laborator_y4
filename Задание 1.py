class Vehicle:
    """
    Базовый класс для всех видов транспортных средств.

    Атрибуты:
        make (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализирует объект Vehicle.

        Аргументы:
            make (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Vehicle.

        Возвращает:
            str: Строковое представление объекта.
        """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Vehicle.

        Возвращает:
            str: Официальное строковое представление объекта.
        """
        return f"Vehicle(make={self.make}, model={self.model}, year={self.year})"

    def start_engine(self) -> None:
        """
        Запускает двигатель транспортного средства.
        """
        print("Engine started.")

class Car(Vehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.

    Атрибуты:
        make (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        num_doors (int): Количество дверей автомобиля.
    """

    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Инициализирует объект Car.

        Аргументы:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            num_doors (int): Количество дверей автомобиля.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.

        Возвращает:
            str: Строковое представление объекта.
        """
        return f"{self.year} {self.make} {self.model} with {self.num_doors} doors"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Car.

        Возвращает:
            str: Официальное строковое представление объекта.
        """
        return f"Car(make={self.make}, model={self.model}, year={self.year}, num_doors={self.num_doors})"

    def start_engine(self) -> None:
        """
        Запускает двигатель автомобиля.

        Перегрузка метода start_engine для добавления специфичной логики для автомобилей.
        """
        print("Car engine started with additional safety checks.")

    def open_trunk(self) -> None:
        """
        Открывает багажник автомобиля.
        """
        print("Trunk opened.")

if __name__ == "__main__":
    # Пример использования классов
    my_car = Car(make="Toyota", model="Corolla", year=2020, num_doors=4)
    print(my_car)
    my_car.start_engine()
    my_car.open_trunk()
