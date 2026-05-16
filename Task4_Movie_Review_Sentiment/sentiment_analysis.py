import pandas as pd
import string
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk

# Download stopwords (run once)
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("reviews.csv")

# Stopwords
stop_words = set(stopwords.words('english'))

# Clean text function
def clean_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Apply cleaning
df['Cleaned_Review'] = df['Review'].apply(clean_text)

# Sentiment analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Cleaned_Review'].apply(get_sentiment)

# Count results
sentiment_counts = df['Sentiment'].value_counts()

print("\n===== SENTIMENT COUNTS =====")
print(sentiment_counts)

# Top 3 positive reviews
print("\n===== TOP 3 POSITIVE REVIEWS =====")
print(df[df['Sentiment'] == 'Positive'][['Review', 'Sentiment']].head(3))

# Top 3 negative reviews
print("\n===== TOP 3 NEGATIVE REVIEWS =====")
print(df[df['Sentiment'] == 'Negative'][['Review', 'Sentiment']].head(3))

# Save result
df.to_csv("result.csv", index=False)

print("\n✔ Result saved as result.csv")

# Simple text-based visualization (NO matplotlib)
print("\n===== SIMPLE VISUALIZATION =====")
for sentiment, count in sentiment_counts.items():
    print(f"{sentiment}: {'█' * count} ({count})")