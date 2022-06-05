# ref: https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# 全20カテゴリあるが、このチュートリアルでは4カテゴリの分類とする
categories = [
    "alt.atheism",
    "soc.religion.christian",
    "comp.graphics",
    "sci.med",
]

# データ（ニュースグループの投稿）
twenty_train = fetch_20newsgroups(
    subset="train", categories=categories, shuffle=True, random_state=42
)
print(f"{len(twenty_train.data)=}, {len(twenty_train.target)=}")
# 正解ラベル twenty_train.target は整数で表されている

tfidf_vect = TfidfVectorizer()
# テキストを数値(TFIDF)に変換して得られた特徴量
X_train_tfidf = tfidf_vect.fit_transform(twenty_train.data)
print(f"{X_train_tfidf.shape=}")

# 機械学習アルゴリズムはサポートベクターマシン（分類）
clf = SVC()
# モデルの訓練
clf.fit(X_train_tfidf, twenty_train.target)

# 訓練に使っていないテキストで、モデルの性能を確認
docs_new = ["God is love", "OpenGL on the GPU is fast"]
X_new_tfidf = tfidf_vect.transform(docs_new)
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print(f"{doc!r} -> {twenty_train.target_names[category]}")
