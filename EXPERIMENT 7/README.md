# Text Analytics - DSBDA Experiment

##  Overview
This project demonstrates basic **Text Analytics (Text Mining)** techniques using Python. It includes document preprocessing steps and representation using **TF-IDF (Term Frequency - Inverse Document Frequency)**.

---
## Problem Statement  
Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of document by calculating Term Frequency and Inverse Document
Frequency.


##  Objective
- Apply text preprocessing techniques:
  - Tokenization
  - POS Tagging
  - Stop Words Removal
  - Stemming
  - Lemmatization
- Represent text using **TF-IDF**

---

##  Theory

### 1. Tokenization
Breaking text into smaller units such as words or sentences.

### 2. POS Tagging
Assigning grammatical tags (noun, verb, adjective, etc.) to each word.

### 3. Stop Words Removal
Removing common words (e.g., *is, the, and*) that do not add much meaning.

### 4. Stemming
Reducing words to their root form.
Example: *running → run*

### 5. Lemmatization
Converting words into their base dictionary form.
Example: *better → good*

### 6. Term Frequency (TF)
Measures how often a term appears in a document.

### 7. Inverse Document Frequency (IDF)
Measures how important a word is across multiple documents.

### 8. TF-IDF
Combines TF and IDF to highlight important words.

---

##  Technologies Used
- Python
- NLTK
- Scikit-learn

---

##  Project Workflow
1. Load sample text document
2. Perform tokenization
3. Apply POS tagging
4. Remove stop words
5. Apply stemming
6. Apply lemmatization
7. Generate TF-IDF representation

---

##  Output
- Tokenized words
- POS tagged words
- Filtered words
- Stemmed and lemmatized words
- TF-IDF matrix and feature names

---

##  Conclusion
Text preprocessing is an essential step in Natural Language Processing. TF-IDF helps in identifying the importance of words in a document, which is useful in applications like search engines, recommendation systems, and text classification.

---

