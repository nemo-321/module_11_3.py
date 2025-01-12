# Эта функция принимает один аргумент `obj`, который является объектом, информацию о котором мы хотим получить.
def introspection_info(obj):

    # Инициализируем пустой словарь `info`, в который будем добавлять информацию об объекте.
    info = {}

    # Определение типа объекта
    info['type'] = type(obj).__name__

    # Определение атрибутов объекта
    # Функция `dir()` возвращает список всех атрибутов и методов объекта, и мы сохраняем его в словаре.
    info['attributes'] = dir(obj)

    # Определение методов объекта
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Определение модуля, к которому принадлежит объект
    info['module'] = obj.__mod__

    # Определение документации объекта (если есть)
    info['docstring'] = obj.__doc__ if obj.__doc__ else "No docstring available"

    return info

# Пример работы
number_info = introspection_info(42)

# Вывод на консоль
print(number_info)