import json

def configure_audi():
    # Initial Car Configuration (Dictionary)
    my_audi = {
        "model": "Audi RS6 GT",
        "engine": "V8 Twin-Turbo",
        "horsepower": 630,
        "color": "Nardo Grey",
        "price_usd": 250000,
        "wheels": "22-inch 5-spoke",
        "status": "Dream Project"
    }

    print("--- Audi RS6 Configurator v2.0 ---")
    print(f"Current Model: {my_audi['model']} ({my_audi['horsepower']} HP)")
    
    # User Customization Section
    print("\n--- Customization ---")
    new_color = input("Enter desired exterior color (e.g., Mythos Black): ")
    
    # Updating the Dictionary
    my_audi["color"] = new_color
    my_audi["status"] = "Ready for Production"
    
    # Displaying Output as formatted JSON string
    print("\n--- Final Specification ---")
    print(json.dumps(my_audi, indent=4))

    # Saving Feature
    save_choice = input("\nDo you want to save this configuration to a file? (y/n): ")
    
    if save_choice.lower() == "y":
        file_name = "audi_config.json"
        # Writing dictionary to a JSON file
        with open(file_name, "w") as file:
            json.dump(my_audi, file, indent=4)
        print(f"Success! Configuration saved to '{file_name}'")
    else:
        print("Data not saved.")

# Entry point of the script
if __name__ == "__main__":
    configure_audi()
