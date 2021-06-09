plant = input("Enter plant name: ")

match plant:
    case "SPATHIPHYLLUM":
        print("Yes - Spathiphyllum is the best plant ever")
    case "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
    case _:
        print("Spathiphyllum not input")
