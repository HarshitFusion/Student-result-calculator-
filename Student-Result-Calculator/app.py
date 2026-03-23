from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    math = int(request.form["math"])
    science = int(request.form["science"])
    english = int(request.form["english"])

    total = math + science + english
    percentage = round((total / 3), 2)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        
        grade = "D"

    return render_template(
        "result.html",
        total=total,
        percentage=percentage,
        grade=grade
    )

if __name__ == "__main__":
    app.run(debug=True)