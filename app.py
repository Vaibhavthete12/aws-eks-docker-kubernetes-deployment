from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    pizza = request.form["pizza"]
    return f"""
    <h1>✅ Order Confirmed</h1>
    <h2>Your {pizza} Pizza is being prepared 🍕</h2>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)