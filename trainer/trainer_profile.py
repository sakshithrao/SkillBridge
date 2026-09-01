from utils.file_handler import read_data


def trainer_profile():
    trainers = read_data("data/trainers.json")

    print("\n===== TRAINER PROFILE =====")

    if len(trainers) == 0:
        print("No trainer profile found.")
        return

    for trainer in trainers:
        print("ID:", trainer["id"])
        print("Name:", trainer["name"])
        print("Email:", trainer["email"])
        print()