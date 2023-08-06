from typing import List


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


if __name__ == '__main__':
    available_ingredients = get_ingredients()
    user_preferences = []
    recommended_cocktails = recommend_cocktails(available_ingredients, user_preferences)
    if recommended_cocktails:
        print('Recommended cocktails:', recommended_cocktails)
    else:
        print('No cocktails found')
