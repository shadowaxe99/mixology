from flask import Flask, request, jsonify
from recommendation import recommend_cocktails
from database import get_ingredients, db

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400

        available_ingredients = data.get('ingredients')
        user_preferences = data.get('preferences')

        if not available_ingredients or not user_preferences:
            return jsonify({'error': 'Missing required fields'}), 400

        recommended_cocktails = recommend_cocktails(available_ingredients, user_preferences)

        if not recommended_cocktails:
            return jsonify({'message': 'No cocktails found'})

        return jsonify([cocktail.name for cocktail in recommended_cocktails])

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
