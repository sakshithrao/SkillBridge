from utils.file_handler import read_data


def placement():
    placements = read_data("data/placements.json")

    print("\n===== PLACEMENT OPPORTUNITIES =====")

    if not placements:
        print("No placement information available.")
        return

    for placement in placements:
        print("Company:", placement["company"])
        print("Role:", placement["role"])
        print("Package:", placement["package"])
        print("------------------------")