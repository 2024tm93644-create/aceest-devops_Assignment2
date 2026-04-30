import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest Fitness DevOps Application Running"

@app.route("/ab")
def ab_test():
    version = random.choice(["A", "B"])
    
    if version == "A":
        return "Version A - Basic UI"
    else:
        return "Version B - Improved UI"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)