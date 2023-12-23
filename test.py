class Rectangle():
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def stretch(self, factor: float) -> 'Rectangle':
        return Rectangle(width=self.width * factor, height=self.height * factor)


def foo(num: float) -> float:
    return num ** 2

