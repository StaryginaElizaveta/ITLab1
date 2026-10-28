
def add_in_base(a: str, b: str, base: int) -> str:
    """Ð¡ÐºÐ»Ð°Ð´Ñ‹Ð²Ð°ÐµÑ‚ Ð´Ð²Ð° Ñ‡Ð¸ÑÐ»Ð° Ð² ÑÐ¸ÑÑ‚ÐµÐ¼Ðµ ÑÑ‡Ð¸ÑÐ»ÐµÐ½Ð¸Ñ Ñ Ð·Ð°Ð´Ð°Ð½Ð½Ñ‹Ð¼ Ð¾ÑÐ½Ð¾Ð²Ð°Ð½Ð¸ÐµÐ¼."""

    if not isinstance(base, int) or isinstance(base, bool):
        raise ValueError("ÐžÑÐ½Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð´Ð¾Ð»Ð¶Ð½Ð¾ Ð±Ñ‹Ñ‚ÑŒ Ñ†ÐµÐ»Ñ‹Ð¼ Ñ‡Ð¸ÑÐ»Ð¾Ð¼")

    if base < 2 or base > 36:
        raise ValueError("ÐžÑÐ½Ð¾Ð²Ð°Ð½Ð¸Ðµ Ð´Ð¾Ð»Ð¶Ð½Ð¾ Ð±Ñ‹Ñ‚ÑŒ Ð¾Ñ‚ 2 Ð´Ð¾ 36")

    if not isinstance(a, str) or not isinstance(b, str) or not a or not b:
        raise ValueError("Ð§Ð¸ÑÐ»Ð° Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ Ð½ÐµÐ¿ÑƒÑÑ‚Ñ‹Ð¼Ð¸ ÑÑ‚Ñ€Ð¾ÐºÐ°Ð¼Ð¸")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    values = {char: value for value, char in enumerate(digits)}

    a = a.upper()
    b = b.upper()

    for number in (a, b):
        for char in number:
            if char not in values or values[char] >= base:
                raise ValueError(
                    f"ÐÐµÐ´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼Ð°Ñ Ñ†Ð¸Ñ„Ñ€Ð° {char!r} Ð´Ð»Ñ Ð¾ÑÐ½Ð¾Ð²Ð°Ð½Ð¸Ñ {base}"
                )

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
