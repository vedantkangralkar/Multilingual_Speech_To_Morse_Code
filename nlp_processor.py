import nltk
import string

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def process_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Lowercase and remove stopwords
    words = text.lower().split()
    filtered = [w for w in words if w not in STOPWORDS]
    return ' '.join(filtered)