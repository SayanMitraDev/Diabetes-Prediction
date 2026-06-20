from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        data = [
            float(request.form["pregnancies"]),
            float(request.form["glucose"]),
            float(request.form["bp"]),
            float(request.form["skin"]),
            float(request.form["insulin"]),
            float(request.form["bmi"]),
            float(request.form["dpf"]),
            float(request.form["age"]),
        ]

        prediction = predict(data)
        result = "Diabetic" if prediction == 1 else "Not Diabetic"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)