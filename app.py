from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        try:

            #Flask recieves the height and weight
            height = float(request.form["height"])
            weight = float(request.form["weight"])

            height_meters = height/100
            bmi = round((weight / (height_meters**2)), 2)

            if bmi < 18.5:
                category, color = "Underweight", "lightblue"
            elif 18.5 <= bmi < 24.9:
                category, color = "Normal", "lightgreen"
            elif 25 <= bmi < 29.9:
                category, color = "Overweight", "orange"
            else:
                category, color = "Obese", "red"
            #goes back to the same html file again but now with values in {{bmi}} and {{category}} (render_template values)
            return render_template("index.html", bmi=bmi, category=category, color=color)
            #incase of wrong value
        except ValueError:
            return render_template("index.html", bmi="Invalid Input", category="Numbers Only!")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)