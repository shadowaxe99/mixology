class Cocktail:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


class Ingredient:
    def __init__(self, name):
        self.name = name


def get_cocktails():
    # This is a placeholder. In a real application, this data would probably come from a database.
    cocktails = [
        Cocktail('Margarita', [Ingredient('Tequila'), Ingredient('Triple Sec'), Ingredient('Lime Juice')]),
        Cocktail('Old Fashioned', [Ingredient('Whiskey'), Ingredient('Sugar'), Ingredient('Bitters')]),
        Cocktail('Mojito', [Ingredient('White Rum'), Ingredient('Sugar'), Ingredient('Lime Juice'), Ingredient('Soda Water')])
    ]
    return cocktails


def get_ingredients():
    # This is a placeholder. In a real application, this data would probably come from a database.
    ingredients = [
        Ingredient('Tequila'),
        Ingredient('Triple Sec'),
        Ingredient('Lime Juice'),
        Ingredient('Whiskey'),
        Ingredient('Sugar'),
        Ingredient('Bitters'),
        Ingredient('White Rum'),
        Ingredient('Soda Water')
    ]
    return ingredients