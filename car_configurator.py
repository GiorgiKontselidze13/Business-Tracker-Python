def configure_audi():
    # 1. Creating the Dictionary (Default Settings)
    my_audi = {
        "model": "Audi RS6 GT",
        "engine": "V8 Twin-Turbo",
        "horsepower": 621,
        "color": "Nardo Grey",  # Default color
        "price_usd": 250000
    }

    print("--- Welcome to Audi Configurator ---")
    print(f"Current selection: {my_audi['model']} in {my_audi['color']}")
    
    # 2. Input: Asking user for customization
    print("\n--- Customization Options ---")
    new_color = input("What color would you like? (e.g., Mythos Black): ")
    
    # 3. Updating the Dictionary
    # აქ ჩვენ ვცვლით მონაცემს ლექსიკონში
    my_audi["color"] = new_color
    
    # 4. Final Output
    print("\n--- Order Summary ---")
    print(f"Vehicle: {my_audi['model']}")
    print(f"Engine: {my_audi['engine']} ({my_audi['horsepower']} HP)")
    print(f"Selected Color: {my_audi['color']}") # აქ უკვე ახალი ფერი იქნება
    print("Status: Ready for production!")

# Running the function
configure_audi()
