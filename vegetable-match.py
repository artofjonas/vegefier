# Veggie list provided courtesy of https://copypastelist.com/food/list/list-of-vegetables
# to do: add some sort of try-except loop to handle bogus input

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