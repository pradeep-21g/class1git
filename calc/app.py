from flask import Flask, render_template, request

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        a = float(request.form["a"])
        b = float(request.form["b"])
        operator = request.form["operator"]

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            return render_template(
                "index.html",
                error="Invalid operator."
            )

        return render_template(
            "index.html",
            result=result
        )

    except ValueError:
        return render_template(
            "index.html",
            error="Please enter valid numbers."
        )

    except ZeroDivisionError as error:
        return render_template(
            "index.html",
            error=str(error)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

