import joblib
import pandas as pd
 
# Load the saved model
model = joblib.load("Branko_Jankovic_Task3/model/final_linear_svm_model.pkl")
 
print("Model loaded successfully!")
print("Type 'exit' at any point to stop.\n")
 
while True:
      
    title = input(" Enter product: ").strip()
    if title.lower() == "exit":
        print("Exiting...")
        break

    # Provera praznog unosa 
    if not title: 
       print("Molimo vas unesite naslov proizvoda.\n") 
       continue
 
    # Predict sentiment
    prediction = model.predict([title])
    print(f" Predicted sentiment: {prediction}\n" + "-" * 40)
    