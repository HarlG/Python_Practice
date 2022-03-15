import numpy as np
import matplotlib.pyplot as plt

#Create seed
np.random.seed(123)

#Initialise of all walks
all_walks = []
for i in range(500):
# Initialisation of single walks
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        # Rules of the game enacted
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step = step + np.random.randint(1,7)
        # 0.1% chance of going to 0
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]



# Plot random_walk
plt.subplot(2,1,1)
plt.plot(np_aw_t)
plt.xlabel('Dice rolls')
plt.ylabel('N of Steps')

# Plot histogram of ends, display plot
plt.subplot(2,1,2)
plt.hist(ends, bins= 20)
plt.xlabel('Total steps')
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show()
