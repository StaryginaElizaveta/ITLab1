
def add_in_base(a: str, b: str, base: int) -> str:
    """Складывает два числа в системе счисления с заданным основанием."""

    if not isinstance(base, int) or isinstance(base, bool) or not 2 <= base <= 36:
        raise ValueError("Основание должно быть от 2 до 36")

    if not isinstance(a, str) or not isinstance(b, str) or not a or not b:
        raise ValueError("Числа должны быть непустыми строками")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    values = {char: value for value, char in enumerate(digits)}

    a = a.upper()
    b = b.upper()

    # Проверяем, что все символы допустимы для указанного основания.
    for number in (a, b):
        for char in number:
            if char not in values or values[char] >= base:
                raise ValueError(
                    f"Недопустимая цифра {char!r} для основания {base}"
                )

    # Складываем числа справа налево, учитывая перенос разряда.
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digit_a = values[a[i]] if i >= 0 else 0
        digit_b = values[b[j]] if j >= 0 else 0

        total = digit_a + digit_b + carry
        result.append(digits[total % base])
        carry = total // base

        i -= 1
        j -= 1

    return "".join(reversed(result)).lstrip("0") or "0"
