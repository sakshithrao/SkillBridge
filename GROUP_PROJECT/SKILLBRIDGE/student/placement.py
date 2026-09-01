from utils.file_handler import read_data


def placement():
    placements = read_data("data/placements.json")

    print("\n===== PLACEMENT INFORMATION =====")

    if len(placements) == 0:
        print("No placement information available.")
        return

    for placement in placements:
        print(
            "Company:", placement["company"],
            "| Role:", placement["role"],
            "| Package:", placement["package"]
        )