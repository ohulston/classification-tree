#Classification Tree Code

FlowerClassificationTree = [0,"QIs the plant a vascular plant?","QDoes the plant have seeds?","ALiverwort","QIs the plant an angiospermae (a flowering plant)?","AFern",6,7,"QIs the plant a monocot?","APine",10,11,12,13,14,15,"ALily","ASunflower"]

PlaceInTree = 1

print("Answer the questions to identy a plant from the following list: liverwort, fern, pine, sunflower, lily\n")


while FlowerClassificationTree[PlaceInTree][0] == "Q":
    response = input(FlowerClassificationTree[PlaceInTree][1:] + " [y/n]: ").lower()
    if response == "y":
        PlaceInTree = PlaceInTree * 2
    elif response == "n":
        PlaceInTree = (PlaceInTree * 2)  + 1
    else:
        print("Please enter valid response")

print("Is your plant a: ",FlowerClassificationTree[PlaceInTree][1:])
