import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# Sample dataset (list of dictionaries)
data = [
    {'label': 'ham', 'message': 'Hey, are you coming to the party tonight?'},
    {'label': 'spam', 'message': 'Congratulations! You have won a free ticket to Bahamas. Call now!'},
    {'label': 'ham', 'message': 'Don’t forget to bring your notebook tomorrow.'},
    {'label': 'spam', 'message': 'You have been selected for a $1000 gift card. Click here!'},
    {'label': 'ham', 'message': 'Let’s meet at 5 PM in the library.'},
    {'label': 'spam', 'message': 'Free entry in a contest. Text WIN to 12345 now!'},
    {'label': 'ham', 'message': 'Lunch at 1?'},
    {'label': 'ham', 'message': 'Sure, I can help with your assignment.'},
    {'label': 'spam', 'message': 'Exclusive offer! Buy 1 get 1 free on all products.'}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Add message length
df['length'] = df['message'].apply(len)

# Plot: Spam vs Ham count
sns.countplot(data=df, x='label')
plt.title("Spam vs Ham Distribution")
plt.show()

# Plot: Message Length Histogram
sns.histplot(data=df, x='length', hue='label', bins=10, kde=True)
plt.title("Message Length Distribution")
plt.show()

# Print average message lengths
print("\nAverage Message Lengths:")
print(df.groupby('label')['length'].mean())

# Generate word clouds
spam_words = " ".join(df[df['label'] == 'spam']['message'])
ham_words = " ".join(df[df['label'] == 'ham']['message'])

spam_wc = WordCloud(width=500, height=300, background_color='black', stopwords=STOPWORDS).generate(spam_words)
ham_wc = WordCloud(width=500, height=300, background_color='white', stopwords=STOPWORDS).generate(ham_words)

# Plot Word Clouds
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Spam Word Cloud")

plt.subplot(1, 2, 2)
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Ham Word Cloud")
plt.tight_layout()
plt.show()
