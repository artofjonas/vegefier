# Veggie list provided courtesy of https://copypastelist.com/food/list/list-of-vegetables
# to do: add a try-except FileNotFoundError in the event that the vegetable_list.txt file is not found or badly formatted
# to do: add a multiple results function in the event of a partial match, e.g. "pea" returns "pea", "snap pea", "snow pea", etc.

# Open and parse vegetable list
with open("./vegetable_list.txt", "r", encoding="utf-8") as f:
    vegetable_list = [line.strip() for line in f.readlines()]

# search for a vegetable
vegetable = input("Enter a vegetable: ")
match vegetable:
    case _ if vegetable in vegetable_list:
        print(f"{vegetable} is in the list.")
    case _:
        print(f"{vegetable} is not in the list.")