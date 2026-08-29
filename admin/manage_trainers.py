from utils.file_handler import read_data, write_data


def manage_trainers():
    while True:
        trainers = read_data("data/trainers.json")

        print("\n===== MANAGE TRAINERS =====")
        print("1. View Trainers")
        print("2. Add Trainer")
        print("3. Delete Trainer")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(trainers) == 0:
                print("No trainers found.")
            else:
                for trainer in trainers:
                    print(
                        "ID:", trainer["id"],
                        "| Name:", trainer["name"],
                        "| Email:", trainer["email"]
                    )

        elif choice == "2":
            name = input("Enter trainer name: ")
            email = input("Enter trainer email: ")

            trainer_id = len(trainers) + 1

            new_trainer = {
                "id": trainer_id,
                "name": name,
                "email": email
            }

            trainers.append(new_trainer)

            write_data("data/trainers.json", trainers)

            print("Trainer added successfully.")

        elif choice == "3":
            trainer_id = int(input("Enter trainer ID to delete: "))

            found = False

            for trainer in trainers:
                if trainer["id"] == trainer_id:
                    trainers.remove(trainer)
                    found = True
                    break

            if found:
                write_data("data/trainers.json", trainers)
                print("Trainer deleted successfully.")
            else:
                print("Trainer not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")