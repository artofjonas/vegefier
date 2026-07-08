# Veggie list provided courtesy of https://copypastelist.com/food/list/list-of-vegetables

vegetable_list = ["carrot", "broccoli", "spinach", "lettuce", "cucumber", "tomato", "pepper", "onion", "garlic", "potato", "celery", "cauliflower", "asparagus", "brussels sprouts", "kale", "swiss chard"]
vegetable = input("Enter a vegetable: ")
match vegetable:
    case _ if vegetable in vegetable_list:
        print(f"{vegetable} is in the list.")
    case _:
        print(f"{vegetable} is not in the list.")