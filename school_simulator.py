grades = 50
energy = 100
happiness = 100
day = 1

print("=== School Survival Simulator ===")

while True:
    print("\nDay", day)
    print("Grades:", grades)
    print("Energy:", energy)
    print("Happiness:", happiness)

    print("\n1. Study")
    print("2. Play Games")
    print("3. Sleep")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        grades += 10
        energy -= 20
        happiness -= 10
        print("You studied hard.")

    elif choice == "2":
        happiness += 15
        energy -= 10
        print("You played games.")

    elif choice == "3":
        energy += 30

        if energy > 100:
            energy = 100

        print("You got some rest.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
        continue

    day += 1

    if grades >= 100:
        print("\nCongratulations! You became a top student!")
        break

    if energy <= 0:
        print("\nYou are exhausted. Game Over.")
        break

    if happiness <= 0:
        print("\nYou are burned out. Game Over.")
        break
