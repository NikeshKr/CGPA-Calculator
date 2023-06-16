from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    num_semesters = int(request.form["num-semesters"])
    total_credits = 0
    weighted_cgpa_sum = 0.0

    for i in range(1, num_semesters + 1):
        cgpa = float(request.form[f"cgpa-{i}"])
        credits = int(request.form[f"credits-{i}"])
        total_credits += credits
        weighted_cgpa_sum += (cgpa * credits)

    overall_cgpa = weighted_cgpa_sum / total_credits

    return render_template("result.html", overall_cgpa=overall_cgpa)


if __name__ == "__main__":
    app.run()
