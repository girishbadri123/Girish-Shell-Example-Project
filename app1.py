from flask import Flask

print("Creating Flask app...")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    print("Running Flask server...")
    app.run(debug=True)
