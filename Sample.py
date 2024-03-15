import time
from SymmetricTree import SymmetricTree

# a simple symmetric tree shape with 10 choices at each level and 3 values tracked at the leaf
symmtree_shape = [

    # lets say the leaf of our tree has 10 possible choices
    (10 , 0 , 1),

    # the next level down also has 10 possible choices
    (10, 0, 10 * 10),

    # the next level down also has 10 possible choices
    (10, 0, 10 * 10 * 10),

    # and at the bottom of our tree with have some float value to track
    # for each of those paths, lets suppose they are 3 (regrets, strategy, and statistics)
    (3, 1, 10 * 10 * 10 * 10)

]

# create a new symmetric tree with that shape
print("Creating Symmetric Tree")
symm_tree = SymmetricTree(shape=symmtree_shape,namespace="SymMTreeTest")

# lets get a sample path
path = [
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3)
]

# test at 100k iterations
iterations = 10 ** 5
print(f"Executing {iterations} gets and sets...")

# get a start time
starttime = int(time.time())

for n in range(iterations):

    # write a value
    symm_tree.set( path , 69.2)

    # read a value
    x = symm_tree.get(path)

# get some stats on the run
endtime = int(time.time())
elapsedtime = endtime-starttime
speed = iterations / elapsedtime

# write some stats
print(f"Completed {iterations} in {elapsedtime} seconds at {speed:.1f} per second")


#perform the same test with a dictionary
control_dict = {1:{1:{1:{1:0.0}}}}

# get a start time
starttime = int(time.time())
for n in range(iterations):

    # write a value
    control_dict[1][1][1][1] = 69.2

    # read a value
    x = control_dict[1][1][1][1]

# get some stats on the run
endtime = int(time.time())
elapsedtime = endtime-starttime + 0.01
speed = iterations / elapsedtime
print(f"Completed {iterations} in {elapsedtime} seconds at {speed:.1f} per second")

# unload that namespace
#symm_tree.unload()