class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class MyClass:
    def countable(self, value):
        if value < 0:
            raise MyException("Значение не может быть отрицательным!")
        else:
            return f"Значение: {value}"

if __name__ == "__main__":
    my_class = MyClass()

    try:
        result = my_class.countable(-5)
        print(result)
    except MyException as e:
        print(f"Произошло исключение: {e.message}")
