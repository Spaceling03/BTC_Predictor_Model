# app.py
from flask import Flask, jsonify
from flask_cors import CORS # Import CORS
# Import the function from your existing file
from predictor_api import make_prediction

# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS for your app
# You can configure CORS more specifically if needed.
# For development, allowing all origins is common:
CORS(app) 

# If you want to restrict to specific origins, use:
# CORS(app, resources={r"/predict": {"origins": "http://localhost:8000"}})
# Or for multiple origins:
# CORS(app, resources={r"/predict": {"origins": ["http://localhost:8000", "https://your-frontend-domain.com"]}})

@app.route('/predict', methods=['GET'])
def predict():
    """
    Runs the prediction and returns it as JSON.
    """
    try:
        result = make_prediction()
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500

# Optional: Add a root endpoint for health checks
@app.route('/', methods=['GET'])
def health_check():
    return "API is running."

if __name__ == '__main__':
    # When deploying, debug=True should be set to False
    app.run(debug=True)
