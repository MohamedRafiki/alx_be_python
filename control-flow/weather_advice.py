# Demander à l'utilisateur le temps qu'il fait aujourd'hui
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Fournir des recommandations vestimentaires en fonction de la saisie de l'utilisateur
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

