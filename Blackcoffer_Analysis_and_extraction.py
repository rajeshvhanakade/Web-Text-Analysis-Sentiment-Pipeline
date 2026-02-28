import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Load input data
input_data = pd.read_excel("Input.xlsx")

# URLs to exclude
exclude_urls = [
    "https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/",
    "https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/"
]

# Function to extract text from URL
def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    if article:
        # Extract article title
        title = article.find('h1').text.strip()
        # Extract article text
        paragraphs = article.find_all('p')
        text = ' '.join([p.text.strip() for p in paragraphs])
        return title, text
    else:
        return None, None

# Function to clean text
def clean_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Convert tokens to lowercase
    tokens = [word.lower() for word in tokens]
    # Remove punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # Remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]
    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]
    # Join words back into text
    cleaned_text = ' '.join(words)
    return cleaned_text

# Function to calculate text analysis variables
def calculate_variables(text):
    # Sentiment Analysis using Vader
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    positive_score = scores['pos']
    negative_score = scores['neg']
    polarity_score = scores['compound']
    # Subjectivity Score (using absolute value of compound score as proxy)
    subjectivity_score = abs(polarity_score)
    
    # Readability Analysis
    sentences = sent_tokenize(text)
    total_words = len(word_tokenize(text))
    avg_sentence_length = total_words / len(sentences)
    words = [word for word in word_tokenize(text) if word.isalpha()]
    complex_words = [word for word in words if len(word) > 2]
    percentage_complex_words = (len(complex_words) / len(words)) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # Other Variables
    avg_word_length = sum(len(word) for word in words) / len(words)
    complex_word_count = len(complex_words)
    word_count = len(words)
    syllable_count = sum([sum(map(lambda w: w.lower().count('a')+w.lower().count('e')+w.lower().count('i')+w.lower().count('o')+w.lower().count('u'),word)) for word in words])
    avg_syllable_per_word = syllable_count / len(words)
    personal_pronouns = sum(1 for word in word_tokenize(text) if word.lower() in ['i', 'we', 'my', 'ours', 'us'])
    
    return (positive_score, negative_score, polarity_score, subjectivity_score,
            avg_sentence_length, percentage_complex_words, fog_index, 
            avg_word_length, complex_word_count, word_count, 
            avg_syllable_per_word, personal_pronouns)

# Create a DataFrame to store the output
output_columns = ['URL_ID', 'URL', 'Title', 'Text', 'Positive Score', 'Negative Score', 
                  'Polarity Score', 'Subjectivity Score', 'Avg Sentence Length', 
                  'Percentage of Complex Words', 'Fog Index', 'Avg Word Length', 
                  'Complex Word Count', 'Word Count', 'Syllable Per Word', 'Personal Pronouns']
output_data = pd.DataFrame(columns=output_columns)

# Iterate through each URL in the input data
for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    if url not in exclude_urls:
        title, text = extract_text(url)
        if text:
            cleaned_text = clean_text(text)
            variables = calculate_variables(cleaned_text)
            # Append a new row to the DataFrame
            if output_data.empty:
                output_data = pd.DataFrame([[url_id, url] + list(variables)], columns=['URL_ID', 'URL'] + output_columns[4:])
            else:
                output_data = pd.concat([output_data, pd.DataFrame([[url_id, url] + list(variables)], columns=['URL_ID', 'URL'] + output_columns[4:])], ignore_index=True)

# Save output to Excel file
output_data.to_excel("Output Data Structure.xlsx", index=False)
