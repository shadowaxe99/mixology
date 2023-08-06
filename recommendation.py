from typing import List


def recommend_cocktails(available_ingredients: List[str], user_preferences: List[str]) -> List[str]:
    # Your recommendation algorithm implementation here
    # Example implementation:
    recommended_cocktails = []
    for ingredient in available_ingredients:
        if ingredient in user_preferences:
            recommended_cocktails.append(ingredient)
    return recommended_cocktails
