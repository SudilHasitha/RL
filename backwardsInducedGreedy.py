
from turtle import up


MAZE = {
    3: {
        8:{
            99:"End"
        }
    },
    12:{
        6:{
            5:"End"
        }
    }
}

# take a list or a element is list then just add if element then append
def flat_map(array):
    new_array = []
    for a in array:
        if isinstance(a,list):
            new_array += flat_map(a)
        else:
            new_array.append(a)
    return new_array

# take an array then slice it to remain head and remaining elements
# util the remaining a single element
# The first element of the array tail will be the value of the previous head element
def create_dict(flat_array):
    head, *tail = flat_array
    if len(tail) ==1:
        return {head: tail[0]}
    else:
        return {head:create_dict(tail)}

# take a dictionary nested or not flip the elements and store as list in a list
def invert_dict(dictionary):
    stack = []
    if not isinstance(dictionary,dict):
        return dictionary
    for key,value in dictionary.items():
        stack.append([invert_dict(value),key])
    return stack

# here [1:] removes 'End'
def create_new_maze(dictionary):
    new_maze = {}
    for path in invert_dict(dictionary):
        new_maze.update(create_dict(flat_map(path)[1:]))
    return new_maze

def backwardInducedGreedy(current_state):
    upside_down_maze =create_new_maze(current_state)
    states = []
    while isinstance(upside_down_maze,dict):
        new_state = max(upside_down_maze.keys())
        states = [new_state] + states
        upside_down_maze = upside_down_maze[new_state]
    states = [upside_down_maze]+states
    total_score = 0
    for state in states:
        total_score +=state
        print(f"Move to {state}")
    print(f"Score {total_score}")

if __name__ == "__main__":
    backwardInducedGreedy(MAZE)