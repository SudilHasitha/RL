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

MAZE2 = {
    4: {
        -100:{
            4:"End"
        }
    },
    1: {
        100:{
            2:"End"
        }
    }
}

def discounted_reward(current_State,gamma=0.9):
    if isinstance(current_State,dict):
        return sum([k + gamma*discounted_reward(v) for k,v in current_State.items()])
    else:
        return 0

def bellmanGreedyPolicy(currentState,totalReward=0,gamma=0.9):
    if not isinstance(currentState,dict):
        print(f"Score {totalReward}")
    else:
        bellman_maze = { (k + gamma * discounted_reward(v),k):v for k,v in currentState.items()}
        new_state = max(bellman_maze.keys())
        print(bellman_maze)
        print(f"Move to new state {new_state[1]} with reward {new_state[0]}")
        bellmanGreedyPolicy(bellman_maze[new_state],totalReward+new_state[0])

if __name__ == "__main__":
    bellmanGreedyPolicy(MAZE2)
