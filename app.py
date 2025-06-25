from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__)

# Define the route for the home page, accepting GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""  # Initialize the message variable
    if request.method == "POST":
        # Get the 'name' value from the submitted form
        name = request.form.get("name")
        # Create a personalized welcome message
        message = f"Hello {name}, Welcome to the Kubernetes test application"
    # Render the 'index.html' template, passing the message variable
    return render_template("index.html", message=message)

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)