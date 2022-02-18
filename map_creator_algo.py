# Importing the necessary modules
import random
import turtle


# check function
def check1(selected, position_dict, direction1, path_length1):
    current = position_dict[selected]
    x1, y1 = current
    if direction1 == "NORTH":
        y1 += path_length1
    elif direction1 == "SOUTH":
        y1 -= path_length1
    elif direction1 == "EAST":
        x1 += path_length1
    else:
        x1 -= path_length1
    changed = (x1, y1)
    if changed in position_dict.values():
        return False
    else:
        return True


# Getting the total number of places
total_places = int(input("Enter the number of places, you want in the map\n"))

# Getting the names of the places
# place_name = {0: "Starting Position"}
# for place in range(1, total_places+1):
#     place_name[place] = input("Enter the name of place {}\n".format(place))

# Getting the path length
path_length = int(input("Enter the path length"))

# Initialising the necessary the data structures
direction_list = ["EAST", "WEST", "NORTH", "SOUTH"]
opposite_dir = {"NORTH": "SOUTH", "SOUTH": "NORTH",
                "EAST": "WEST", "WEST": "EAST"}
avail_places = {0}
direction_angle = {"NORTH": 90, "SOUTH": 270, "EAST": 0, "WEST": 180}

# Creating a turtle object and initialising it
location = turtle.Turtle()
location.hideturtle()
location.dot()
location.write("Start", align='center')
pos_dict = {0: tuple(location.pos())}

# Applying the algorithm to randomly generate a map for the places
for place in range(1, total_places+1):
    direction = random.choice(direction_list)
    unavail_places = set()

    while True:
        selected_place = random.choice(list(avail_places - unavail_places))
        c = check1(selected_place, pos_dict, direction, path_length)
        if c:
            if place in range(1, 11):
                location.color("blue")
            elif place in range(11, 21):
                location.color("red")
            elif place in range(21, 31):
                location.color("green")
            avail_places.add(place)
            location.penup()
            turtle_initial_pos = pos_dict[selected_place]
            location.goto(turtle_initial_pos)
            location.pendown()
            location.setheading(direction_angle[direction])
            location.fd(path_length)
            location.dot()
            x, y = tuple(location.pos())
            x = round(x)
            y = round(y)

            pos_dict[place] = (x, y)
            location.setheading(0)
            break
        else:
            unavail_places.add(selected_place)

turtle.done()
