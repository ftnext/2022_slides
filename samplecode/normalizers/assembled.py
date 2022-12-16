import re
import unicodedata
from collections.abc import Sequence as AbcSequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class Normalizer(Protocol):
    def normalize(self, text: str) -> str:
        ...


class Strip(Normalizer):
    def normalize(self, text: str) -> str:
        return text.strip()


class Lowercase(Normalizer):
    """
    >>> Lowercase().normalize("NikkiE")
    'nikkie'
    """

    def normalize(self, text: str) -> str:
        return text.lower()


class NFKC(Normalizer):
    """
    >>> # Return 0X30D7, 0X30ED
    >>> NFKC().normalize("".join([chr(0X30D5), chr(0X309A), chr(0X30ED)]))
    'プロ'
    """

    def normalize(self, text: str) -> str:
        return unicodedata.normalize("NFKC", text)


class UnicodeNormalize(Normalizer):
    def __init__(self, cls) -> None:
        self.cls = cls
        self.nfkc = NFKC()
        self.replace = Replace("－", "-")

    def normalize(self, text: str) -> str:
        pt = re.compile("([{}]+)".format(self.cls))

        def norm(c):
            return self.nfkc.normalize(c) if pt.match(c) else c

        s = "".join(norm(x) for x in re.split(pt, text))
        return self.replace.normalize(s)


class Replace(Normalizer):
    def __init__(self, pattern, repl) -> None:
        self.pattern = pattern
        self.repl = repl

    def normalize(self, text: str) -> str:
        return re.sub(self.pattern, self.repl, text)


class RemoveSpaceBetween(Normalizer):
    def __init__(self, cls1, cls2) -> None:
        self.cls1 = cls1
        self.cls2 = cls2

    def normalize(self, text: str) -> str:
        p = re.compile("([{}]) ([{}])".format(self.cls1, self.cls2))
        while p.search(text):
            text = p.sub(r"\1\2", text)
        return text


class Translate(Normalizer):
    def __init__(self, f, t) -> None:
        self.f = f
        self.t = t

    def maketrans(self):
        return {ord(x): ord(y) for x, y in zip(self.f, self.t)}

    def normalize(self, text: str) -> str:
        return text.translate(self.maketrans())


class Sequence(Normalizer):
    """
    >>> sut = Sequence([Lowercase(), NFKC()])
    >>> sut.normalize("NikkiE")
    'nikkie'
    >>> sut.normalize("".join([chr(0X30D5), chr(0X309A), chr(0X30ED)]))
    'プロ'
    """

    def __init__(self, normalizers: AbcSequence[Normalizer]) -> None:
        self.normalizers = normalizers

    def normalize(self, text: str) -> str:
        normalized = text
        for normalizer in self.normalizers:
            normalized = normalizer.normalize(normalized)
        return normalized


class RemoveExtraSpaces(Normalizer):
    BLOCKS = "".join(
        (
            "\u4E00-\u9FFF",  # CJK UNIFIED IDEOGRAPHS
            "\u3040-\u309F",  # HIRAGANA
            "\u30A0-\u30FF",  # KATAKANA
            "\u3000-\u303F",  # CJK SYMBOLS AND PUNCTUATION
            "\uFF00-\uFFEF",  # HALFWIDTH AND FULLWIDTH FORMS
        )
    )
    BASIC_LATIN = "\u0000-\u007F"

    def __init__(self):
        self.normalizer = Sequence(
            [
                Replace("[ 　]+", " "),
                RemoveSpaceBetween(self.BLOCKS, self.BLOCKS),
                RemoveSpaceBetween(self.BLOCKS, self.BASIC_LATIN),
                RemoveSpaceBetween(self.BASIC_LATIN, self.BLOCKS),
            ]
        )

    def normalize(self, text: str) -> str:
        return self.normalizer.normalize(text)


class NeologdNormalizer(Normalizer):
    def __init__(self) -> None:
        normalizers = [
            Strip(),
            # NFKC(),  # TODO
            UnicodeNormalize("０-９Ａ-Ｚａ-ｚ｡-ﾟ"),
            Replace("[˗֊‐‑‒–⁃⁻₋−]+", "-"),  # normalize hyphens
            Replace("[﹣－ｰ—―─━ー]+", "ー"),  # normalize choonpus
            Replace("[~∼∾〜〰～]", ""),  # remove tildes
            Translate(
                "!\"#$%&'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣",
                "！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」",
            ),
            RemoveExtraSpaces(),
            UnicodeNormalize(
                "！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝〜"
            ),  # keep ＝,・,「,」
            Replace("[’]", "'"),
            Replace("[”]", '"'),
        ]
        self.normalizer = Sequence(normalizers)

    def normalize(self, text: str) -> str:
        return self.normalizer.normalize(text)


def normalize_neologd(s):
    normalizer = NeologdNormalizer()
    return normalizer.normalize(s)


if __name__ == "__main__":
    assert "0123456789" == normalize_neologd("０１２３４５６７８９")
    assert "ABCDEFGHIJKLMNOPQRSTUVWXYZ" == normalize_neologd(
        "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    )
    assert "abcdefghijklmnopqrstuvwxyz" == normalize_neologd(
        "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    )
    assert "!\"#$%&'()*+,-./:;<>?@[¥]^_`{|}" == normalize_neologd(
        "！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝"
    )
    assert "＝。、・「」" == normalize_neologd("＝。、・「」")
    assert "ハンカク" == normalize_neologd("ﾊﾝｶｸ")
    assert "o-o" == normalize_neologd("o₋o")
    assert "majikaー" == normalize_neologd("majika━")
    assert "わい" == normalize_neologd("わ〰い")
    assert "スーパー" == normalize_neologd("スーパーーーー")
    assert "!#" == normalize_neologd("!#")
    assert "ゼンカクスペース" == normalize_neologd("ゼンカク　スペース")
    assert "おお" == normalize_neologd("お             お")
    assert "おお" == normalize_neologd("      おお")
    assert "おお" == normalize_neologd("おお      ")
    assert "検索エンジン自作入門を買いました!!!" == normalize_neologd(
        "検索 エンジン 自作 入門 を 買い ました!!!"
    )
    assert "アルゴリズムC" == normalize_neologd("アルゴリズム C")
    assert "PRML副読本" == normalize_neologd("　　　ＰＲＭＬ　　副　読　本　　　")
    assert "Coding the Matrix" == normalize_neologd("Coding the Matrix")
    assert "南アルプスの天然水Sparking Lemonレモン一絞り" == normalize_neologd(
        "南アルプスの　天然水　Ｓｐａｒｋｉｎｇ　Ｌｅｍｏｎ　レモン一絞り"
    )
    assert "南アルプスの天然水-Sparking*Lemon+レモン一絞り" == normalize_neologd(
        "南アルプスの　天然水-　Ｓｐａｒｋｉｎｇ*　Ｌｅｍｏｎ+　レモン一絞り"
    )
