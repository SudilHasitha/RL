from unicodedata import name
from celery import current_app


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

def greedyApproach(current_state, reward = 0):

    if (not isinstance(current_state,dict)):
        # advancing to the next state which is maximunm
        print(f"The total rewards is {reward}")
    else:
        # move to the next state
        new_state = max(current_state.keys())
        reward += new_state
        print(f"Moving to {new_state} from {current_state.keys()} with reward of {new_state}")
        greedyApproach(current_state[new_state], reward)

if __name__=='__main__':
    greedyApproach(MAZE)
    exit(0);
