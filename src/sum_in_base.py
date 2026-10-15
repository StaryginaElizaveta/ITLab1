def add_in_base(a: str, b: str, base: int) -> str:
    # Все цифры для систем счисления от 2 до 36
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Проверяем основание системы счисления
    if base < 2 or base > 36:
        raise ValueError("Неверное основание")

    # Переводим буквы в верхний регистр
    a = a.upper()
    b = b.upper()

    # Проверяем, что числа не пустые и содержат допустимые символы
    if not a or not b or any(x not in digits[:base] for x in a + b):
        raise ValueError("Неверная цифра")

    # Создаём переменные для хранения чисел
    num1 = 0
    num2 = 0

    # Переводим первое число в десятичную систему
    for x in a:
        num1 = num1 * base + digits.index(x)

    # Переводим второе число в десятичную систему
    for x in b:
        num2 = num2 * base + digits.index(x)

    # Складываем полученные числа
    total = num1 + num2

    # Если сумма равна нулю, возвращаем "0"
    if total == 0:
        return "0"

    # Создаём пустую строку для результата
    result = ""

    # Переводим сумму обратно в исходную систему счисления
    while total > 0:
        # Находим последнюю цифру результата
        remainder = total % base

        # Добавляем цифру в начало строки
        result = digits[remainder] + result

        # Убираем уже обработанный разряд
        total = total // base

    # Возвращаем готовый результат
    return result