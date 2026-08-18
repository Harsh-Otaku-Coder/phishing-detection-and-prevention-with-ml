import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier


path = "data/url_features.csv"

df = pd.read_csv(path)

print("data shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nlable distribution")
print(df["label"].value_counts())

x = df.drop(columns=["label"])
y = df["label"]

print("\nX shape:")
print(x.shape)

print("\nY shape:" )
print(y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:")
print(X_train.shape)
print(Y_train.shape)

print("\nTesting data:")
print(X_test.shape)
print(Y_test.shape)

Forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

Forest_model.fit(X_train, Y_train)
Y_pred = Forest_model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print("\nRandom forest accuracy: ")
print(accuracy)

print("\n Classification report:")
print(classification_report(Y_test, Y_pred))

Logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
Logistic_model.fit(X_train, Y_train)
Logistic_pred = Logistic_model.predict(X_test)

logistic_accuracy = accuracy_score(Y_test, Logistic_pred)

print("\nLogistic regression accuracy:")
print(logistic_accuracy)
print("\nlogistic regression classification report:")
print(classification_report(Y_test, Logistic_pred))

gradient_model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)
gradient_model.fit(X_train, Y_train)

gradient_pred = gradient_model.predict(X_test)
gradient_accuracy= accuracy_score(Y_test, gradient_pred)

print("\nGradient boosting accuracy:")
print(gradient_accuracy)

print("\ngradient boosting classification report:")
print(classification_report(Y_test, gradient_pred))

joblib.dump(Forest_model,"models/url_random_forest.pkl")
