# %%
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import texthero as hero
import pandas as pd
# %%
file = open("../dataset/CTI_Data_English_Cleaning.txt", "r", encoding='UTF-8')
data = file.read()
file.close()

# %%
words = data.split()
print('Number of words in text file :', len(words))

# %%
nltk_sw = stopwords.words('english')
wordcloud = WordCloud(
    stopwords=nltk_sw, background_color='white').generate(data)
