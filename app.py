#Importing the libraries
from flask import Flask, render_template, request
import pickle

#Global variables
app = Flask(__name__)
age_spend = pickle.load(open("age-spend_seg.pkl", "rb"))
income_spend = pickle.load(open("income-spend_seg.pkl","rb"))

#User-defined functions
@app.route("/", methods=["GET"])
def Home():
    return render_template("Segmentation.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    age = int(request.form['age'])
    income = int(request.form['income'])
    spending_score = int(request.form['spending_score'])
    
    age_spend_prediction = age_spend.predict([[age,spending_score]])[0]
    income_spend_prediction = income_spend.predict([[income,spending_score]])[0]

    
    if income_spend_prediction == 0:
        income_spend_prediction = "Priority Customer"
    elif income_spend_prediction==1:
        income_spend_prediction = "Target - High Income"
    elif income_spend_prediction==2:
        income_spend_prediction = "Target - Low Income"
    elif income_spend_prediction==3:
        income_spend_prediction = "Common Customer"
    elif income_spend_prediction==4:
        income_spend_prediction = "Low Priority Customer"

    if age_spend_prediction==0:
        age_spend_prediction  = "Target - Old"
    elif age_spend_prediction==1:
        age_spend_prediction  = "Low Priority Customer"
    elif age_spend_prediction==2:
        age_spend_prediction  = "Priority Customer"
    elif age_spend_prediction==3:
        age_spend_prediction  = "Target - Young"

    return render_template("Segmentation.html", prediction1_output=income_spend_prediction, prediction2_output = age_spend_prediction)


#Main function
if __name__ == "__main__":
    app.run(debug=True)
