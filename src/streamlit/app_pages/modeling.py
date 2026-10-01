from pathlib import Path

import joblib
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

st.title("Modeling")

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_PATH = BASE_DIR / "src/streamlit/train.csv"
MODELS_DIR = BASE_DIR / "models"

df = pd.read_csv(DATA_PATH)

df = df.drop(
    columns=["PassengerId", "Name", "Ticket", "Cabin"],
    errors="ignore",
)

y = df["Survived"]

X_cat = df[["Pclass", "Sex", "Embarked"]].copy()
X_num = df[["Age", "Fare", "SibSp", "Parch"]].copy()

for column in X_cat.columns:
    X_cat[column] = X_cat[column].fillna(X_cat[column].mode()[0])

for column in X_num.columns:
    X_num[column] = X_num[column].fillna(X_num[column].median())

X_cat_encoded = pd.get_dummies(
    X_cat,
    columns=X_cat.columns,
)

X = pd.concat([X_cat_encoded, X_num], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=123,
    stratify=y,
)

scaler = StandardScaler()

X_train = X_train.copy()
X_test = X_test.copy()

X_train[X_num.columns] = scaler.fit_transform(
    X_train[X_num.columns],
)

X_test[X_num.columns] = scaler.transform(
    X_test[X_num.columns],
)


def create_classifier(model_name):
    if model_name == "Random Forest":
        return RandomForestClassifier(
            random_state=123,
        )

    if model_name == "SVC":
        return SVC()

    if model_name == "Logistic Regression":
        return LogisticRegression(
            max_iter=1000,
        )

    raise ValueError(f"Unknown model: {model_name}")


model_name = st.selectbox(
    "Choice of the model",
    [
        "Random Forest",
        "SVC",
        "Logistic Regression",
    ],
)

classifier = create_classifier(model_name)
classifier.fit(X_train, y_train)

st.write("The chosen model is:", model_name)

display_option = st.radio(
    "What do you want to show?",
    ["Accuracy", "Confusion matrix"],
)

if display_option == "Accuracy":
    accuracy = classifier.score(X_test, y_test)
    st.metric("Accuracy", f"{accuracy:.3f}")

else:
    predictions = classifier.predict(X_test)
    matrix = confusion_matrix(y_test, predictions)

    st.dataframe(
        pd.DataFrame(
            matrix,
            index=["Actual 0", "Actual 1"],
            columns=["Predicted 0", "Predicted 1"],
        ),
    )

MODELS_DIR.mkdir(exist_ok=True)

selected_model_path = MODELS_DIR / "selected_model.joblib"
joblib.dump(classifier, selected_model_path)

st.success(f"Model saved to: {selected_model_path}")

rf_model_path = MODELS_DIR / "rf.joblib"

if rf_model_path.exists():
    rf = joblib.load(rf_model_path)
    st.write("Random Forest model loaded successfully.")
    st.write(rf)
else:
    st.info("models/rf.joblib could not be found.")
