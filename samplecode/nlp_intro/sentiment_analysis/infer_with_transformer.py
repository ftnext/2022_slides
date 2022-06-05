import jsonlines
from tqdm import tqdm
from transformers import pipeline

nlp = pipeline(
    "sentiment-analysis",
    model="daigo/bert-base-japanese-sentiment",
    tokenizer="daigo/bert-base-japanese-sentiment",
    truncation=True,
)

positives = []
negatives = []
with open("splitted_wagahaiha_nekodearu.txt") as fin, jsonlines.open(
    "transformer_scores.jsonl", mode="w"
) as writer:
    for line in tqdm(fin):
        result = nlp(line.strip())
        writer.write({"text": line.strip(), "result": result})
