from typing import List
from flask import Flask, jsonify

app = Flask(__name__)


def recommend_cocktails(available_ingredients: List[str], user_preferences: List[str]) -> List[str]:
    # Your recommendation algorithm implementation here
    # Example implementation:
    recommended_cocktails = []
    for ingredient in available_ingredients:
        if ingredient in user_preferences:
            recommended_cocktails.append(ingredient)
    return recommended_cocktails


def get_ingredients() -> List[str]:
    # Your database query implementation here
    # Example implementation:
    return ['vodka', 'orange juice', 'cranberry juice']


@app.route('/')
def home():
    available_ingredients = get_ingredients()
    user_preferences = []
    recommended_cocktails = recommend_cocktails(available_ingredients, user_preferences)
    if recommended_cocktails:
        return jsonify({'message': 'Recommended cocktails', 'cocktails': recommended_cocktails})
    else:
        return jsonify({'message': 'No cocktails found'})


if __name__ == '__main__':
    app.run()
