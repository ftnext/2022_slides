import csv

from fugashi import Tagger


def tokenize(tagger, text):
    return [word.feature.lemma for word in tagger(text)]


def calculate_score(words, word2score):
    score = 0
    for word in words:
        if word in word2score:
            score += word2score[word]
    return score


values = {"ポジ（経験）": 1, "ポジ（評価）": 1, "ネガ（経験）": -1, "ネガ（評価）": -1}

with open("wago.121808.pn") as f:
    reader = csv.reader(f, delimiter="\t")
    word2score = {row[1]: values[row[0]] for row in reader}

tagger = Tagger("-Owakati")

scores = []
with open("splitted_wagahaiha_nekodearu.txt") as f:
    for line in f:
        words = tokenize(tagger, line.strip())
        score = calculate_score(words, word2score)
        scores.append((line.strip(), score))

scores_descending = sorted(scores, key=lambda t: t[1], reverse=True)
