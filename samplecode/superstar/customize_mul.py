from __future__ import annotations

from collections import UserString


class CouplableStr(UserString):
    """「掛け算」ができる文字列クラス

    >>> CouplableStr("ゆう") * CouplableStr("ぽむ")
    'ゆうぽむ'
    >>> CouplableStr("🖤") * CouplableStr("🎀")
    '🖤🎀'
    >>> CouplableStr("ぽむ") * 3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for *: 'CouplableStr' and 'int'
    """

    def __mul__(self, other: CouplableStr) -> str:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return f"{self.data}{other.data}"
