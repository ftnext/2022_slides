def transform(input_: str) -> str:
    if not isinstance(input_, str):
        raise TypeError("Expected string parameter")

    result = ""
    for character in input_:
        char_code = ord(character)
        result += transform_letter(char_code)
    return result


def transform_letter(char_code: int) -> str:
    if is_between(char_code, "a", "m") or is_between(char_code, "A", "M"):
        char_code += 13
    elif is_between(char_code, "n", "z") or is_between(char_code, "N", "Z"):
        char_code -= 13
    return chr(char_code)


def is_between(char_code: int, first_letter: str, last_letter: str) -> bool:
    return code_for(first_letter) <= char_code <= code_for(last_letter)


def code_for(letter: str) -> int:
    return ord(letter)
