import string
from nltk import download
import nltk
from nltk.corpus import stopwords

#download('stopwords')
#nltk.download('punkt')
stop_words = stopwords.words('english')

def basic_tokenizer(sentence):
    punctuation = string.punctuation
    string2 = sentence.lower()
    newstring = ''
    for char in string2:
        if char not in punctuation:
            newstring += char
    stingOfWord = newstring.split(' ')
    return(stingOfWord)

def remove_stopwords(list, stop_words):
    output = []
    for item in list:
        if item not in stop_words:
            output.append(item)
    return output

def preprocess(sentence, stop_words):
    sentence = basic_tokenizer(sentence)
    clean_sentence = remove_stopwords(sentence, stop_words)

    return clean_sentence

print(preprocess("This is a test sentence for the preprocessor", stop_words))