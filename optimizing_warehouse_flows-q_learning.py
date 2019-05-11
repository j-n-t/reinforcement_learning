# Optimizing Warehouse Flows with Q-Learning

# Importing the libraries
import numpy as np

# Setting the parameters gamma and alpha for the Q-Learning
gamma = 0.75
alpha = 0.9


# DEFINING THE ENVIRONMENT

# Defining the states
location_to_state = {'A': 0, 
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8,
                     'J': 9,
                     'K': 10,
                     'L': 11}

# Defining the actions
actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Defining the rewards
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
              [1,0,1,0,0,1,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,1,0,0,0],
              [0,1,0,0,0,0,0,0,0,1,0,0],
              [0,0,1,0,0,0,1,1,0,0,0,0],
              [0,0,0,1,0,0,1,0,0,0,0,1],
              [0,0,0,0,1,0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0,0,1,0,1,0],
              [0,0,0,0,0,0,0,0,0,1,0,1],
              [0,0,0,0,0,0,0,1,0,0,1,0]])


# BUILDING THE SOLUTION WITH Q-LEARNING
    
# Mapping states to locations
state_to_location = {state: location for location, state in location_to_state.items()}

# Function that will return the optimal route
def route(starting_location, ending_location):
    R_new = np.copy(R)
    ending_state = location_to_state[ending_location]
    R_new[ending_state, ending_state] = 1000 # defining the reward for the desired ending location
    Q = np.array(np.zeros([12,12])) # initializing the Q-Values
    # implementing the Q-Learning process
    for i in range(1000): # for 1000 steps
        current_state = np.random.randint(0,12) # we have 12 possible states
        playable_actions = []
        for j in range(12):
            if R_new[current_state, j] > 0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state] # computing the temporal difference
        Q[current_state, next_state] += alpha * TD # updating the Q-Values
    # defining the optimal route
    route = [starting_location]
    next_location = starting_location
    while(next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

# USE CASE PASSING BY AN INTERMEDIARY LOCATION

# Function that will return the optimal route passing by an intermediary location
def best_route(starting_location, intermediary_location, ending_location):
    return route(starting_location, intermediary_location) + route(intermediary_location, ending_location)[1:]

# Defining the final route passing by an intermediary location
start = input("What is the starting location? ")
interm = input("What is the intermediary location? ")
end = input("What is the ending location? ")

print(f"The best route is: {best_route(start, interm, end)}.")










