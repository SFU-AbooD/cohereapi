import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import cohere
model_name = 'multilingual-22-12'
api = '4VmdpRIKe4qdPmNCD4XKhPxwq5hzdqDvfDoJY590'
from sklearn.linear_model import LogisticRegression
obj = pd.read_json("file3.json")
x = obj.content.tolist()
X = np.array(x)
X = X.astype(float)
Y = obj['sentiment'].tolist()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
rf = LogisticRegression()
rf.fit(X_train, y_train)
def predict(message):
    output = rf.predict_proba(cohere.Client(api_key=api).embed(model=model_name,truncate='RIGHT',texts=[message]).embeddings)[0]
    return output
