from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_spare_change():
    # Get the purchase amounts from the request
    data = request.json
    if not data or "purchases" not in data:
        return jsonify({"error": "Please provide a list of purchases in the 'purchases' field."}), 400

    purchases = data["purchases"]
    if not isinstance(purchases, list) or not all(isinstance(amount, (int, float)) for amount in purchases):
        return jsonify({"error": "Purchases should be a list of numbers."}), 400

    # Calculate spare change
    spare_change = sum([math.ceil(amount) - amount for amount in purchases])
    total_saved = round(spare_change, 2)

    # Project savings with simple interest (5% for one year)
    interest_rate = 0.05
    savings_with_interest = round(total_saved * (1 + interest_rate), 2)

    # Add a random "savings personality"
    personalities = [
        "The Coffee Connoisseur Saver",
        "The Grocery Guru",
        "The Late-Night Snacker Investor",
        "The Impulse Buyer Turned Saver",
    ]
    from random import choice
    personality = choice(personalities)

    # Prepare the response
    response = {
        "total_spare_change_saved": f"${total_saved}",
        "projected_savings_with_interest": f"${savings_with_interest}",
        "savings_personality": f"You are {personality}!"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)