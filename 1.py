# 情感分析
lemmatized_text_title_list = ['happy', 'sad', 'angry', 'excited', 'bored']
import pandas as pd

from nltk.sentiment import SentimentIntensityAnalyzer
# 创建情感分析器
sia = SentimentIntensityAnalyzer()
# 对lemmatized_text_title_list中的词进行情感指数计算
sentiment_scores = []
for word in lemmatized_text_title_list:
    score = sia.polarity_scores(word)
    sentiment_scores.append(score)
# 将情感分数转换为DataFrame
sentiment_df = pd.DataFrame(sentiment_scores)
print(sentiment_df)
