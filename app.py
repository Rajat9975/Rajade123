from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the serialized Random Forest model and TF-IDF vectorizer
model = joblib.load('random_forest_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

class TextData(BaseModel):
    text: str

@app.post("/predict/")
def predict(data: TextData):
    # Transform the input text to the appropriate format
    transformed_data = vectorizer.transform([data.text])
    # Predict the class using the Random Forest model
    prediction = model.predict(transformed_data)
    # Return the predicted class
    return {"prediction": prediction[0]}
