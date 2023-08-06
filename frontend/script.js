document.getElementById('ingredients-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var ingredients = document.getElementById('ingredients').value.split(',').map(function(ingredient) { return ingredient.trim(); });
    var preferences = document.getElementById('preferences').value.split(',').map(function(cocktail) { return cocktail.trim(); });
    // Call the backend with the ingredients and preferences to get the recommended cocktails
    // This is a placeholder and needs to be replaced with the actual backend call
    var recommendedCocktails = ['Margarita', 'Old Fashioned'];
    var recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = '';
    if (recommendedCocktails.length > 0) {
        recommendationsDiv.innerHTML = '<h2>Here are some cocktails you can make:</h2>' + recommendedCocktails.map(function(cocktail) { return '<p>' + cocktail + '</p>'; }).join('');
    } else {
        recommendationsDiv.innerHTML = '<p>Sorry, no cocktails found with the ingredients you have.</p>';
    }
});