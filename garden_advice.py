def get_season_advice(season):
    """Return gardening advice based on the entered season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice based on the entered plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Collect user input and display the appropriate gardening advice."""
    season = input(
        "Enter the season (summer or winter): "
    ).strip().lower()

    plant_type = input(
        "Enter the plant type (flower or vegetable): "
    ).strip().lower()

    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)

    print("\nGardening advice:")
    print(season_advice)
    print(plant_advice)


if __name__ == "__main__":
    main()