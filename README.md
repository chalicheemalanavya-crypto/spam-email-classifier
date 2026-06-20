📧 Spam Email Classifier

Overview

Spam Email Classifier is a Machine Learning project that classifies email messages as Spam or Not Spam using Natural Language Processing (NLP).

Features

- Enter any email message.
- Detect whether the message is Spam or Not Spam.
- Simple and user-friendly interface.
- Built using Streamlit.

Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit
- CountVectorizer
- Naive Bayes

Project Structure

spam-email-classifier/
│
├── app.py
├── spam.csv
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md

Installation

Install required libraries:

pip install -r requirements.txt

Run the Application

streamlit run app.py

Sample Inputs

Spam Message

Congratulations! You won a free iPhone. Claim now!

Normal Message

Please send the assignment by evening.

Author

Navi's spot