import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
# You can download the dataset from: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
# For demo purposes, we'll use a direct URL to a CSV version
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"

# Read dataset
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# 2. Preprocessing
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})  # Encode labels

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label_num'], test_size=0.2, random_state=42)

# 4. Vectorize text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Predict on new message
def predict_message(msg):
    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)
    return "Spam" if prediction[0] == 1 else "Ham"

# Test the function
print("\nPrediction:", predict_message("Congratulations! You've won a free ticket to Bahamas. Call now!"))
print("Prediction:", predict_message("Hey, are we still meeting for lunch today?"))
