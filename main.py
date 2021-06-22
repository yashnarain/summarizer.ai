# Import Libraries
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    # URL text
    url = utext.get('1.0', "end").strip()

    # create an article object
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    authors.config(state='normal')
    publish.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', article.authors)

    publish.delete('1.0', 'end')
    publish.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity} | Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    authors.config(state='disabled')
    publish.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root = tk.Tk()

root.title("Summarizer.ai")
root.geometry('1200x600')

# Title Label and Text Box

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Author Label and Text Box

alabel = tk.Label(root, text="Author(s)")
alabel.pack()

authors = tk.Text(root, height=1, width=140)
authors.config(state='disabled', bg='#dddddd')
authors.pack()

# Publication Label and Text Box

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publish = tk.Text(root, height=1, width=140)
publish.config(state='disabled', bg='#dddddd')
publish.pack()

# Summary Label and Text Box

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment Label and Text Box

sentlabel = tk.Label(root, text="Sentiment")
sentlabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL Label and Text Box

urllabel = tk.Label(root, text="URL")
urllabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Summarize Button

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()