def add_in_base(a: str, b: str, base: int) -> str:
    """
    Складывает два числа, записанных в системе счисления с основанием base.

    :param a: первое число, строка (например, "1011")
    :param b: второе число, строка (например, "111")
    :param base: основание системы счисления, 2 <= base <= 36
    :return: сумма в той же системе счисления, строка

    Пример:
        add_in_base("1011", "111", 2) -> "10010"
        add_in_base("FF", "1", 16) -> "100"
    """
    if (base < 2 or base > 36):
        raise ValueError("Основание системы счисления должно быть больше 1 и меньше 37")
    
    # Преобразование букв в значения
    DIGITS  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    VAL     = {}
    for idx, char in enumerate(DIGITS):
        VAL[char] = idx

    i, j = len(a) - 1, len(b) - 1
    carry = 0 # перенос
    out = [] # вывод наоборот
    
    while i >= 0 or j >= 0 or carry:

        # Получение значения для цифр чисел с соответствующими индексами
        da = VAL[a[i]] if i >= 0 else 0
        db = VAL[b[j]] if j >= 0 else 0

        s = da + db + carry
        out.append(DIGITS[s % base])
        carry = s // base
        i -= 1
        j -= 1
    
    return "".join(reversed(out))