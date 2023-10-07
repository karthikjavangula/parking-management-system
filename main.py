'''
Let me briefly explain you the concept:
1. There is a 2-D array of Cell objects which makes up the Parking Lot.
2. Each Cell object in turn contains a Vehicle object which is stored in the status variable. If status = None, then it signifies that the cell is empty.
3. We are supposed to assign a free cell to an incoming vehicle using a function.
4. There are 2 Types of Vehicles, Cars and Bikes. Bikes take up one single cell, but cars take 4 cells. Those 4 cells need to be consecutive, in a square shape, for example, ((0, 0), (0, 1), (1, 0), (1, 1)) are 4 cells that can fit 1 Car.
5. Normally, the parking lot is a grid of 2 * n size. We have 2 different ranges of cells for Bikes and Cars. Virtually, each Car cell is 4 consecutive square shaped normal cells.
6. We fill the range of bikes with bikes, and cars with cars, but the challenge is, if the entire range allotted for bikes is full, but the Car range is not, then we need to be able to convert a single Car cell into 4 Bike cells and allot it, and Vice versa, We need to be able to find 4 square-arranged empty cells in the bike range and allot it to a Car in case the Car range is full and Bike range is not full.
7. We need to make sure that an entire car cell is inaccessible to other cars even if only 1 bike is parked in it.

Now, how do I implement this in code? How do I go about having 2 different intended ranges?

Please add to my code:

ChatGPT conversation link: https://chat.openai.com/share/072e4af0-1980-4fc3-9e33-b1607dce19d1

'''

ROWS = 2
COLS = 12

# The first 4 columns are for bikes, the next 8 are for cars
# Let's initialize bike range which is a list of coordinates of cells:
bike_range = [(0, 0), (0, 1), (1, 0), (1, 1)]    

class Cell:
    status = None # Usually status will be assigned to a Vehicle object
    constraints = None # List of other Cell objects that this Cell is constrained by
    def __init__(self, x, y, status, constraints):
        self.status = status
        self.constraints = constraints

class Vehicle:
    type = None # Whether it is a car or a bike
    in_time = None # Time at which the vehicle entered the parking lot
    out_time = None # Time at which the vehicle is expected to leave the parking lot
    id = None # Unique identifier for the vehicle (PK in the Vehicle table)
    def __init__(self, type, in_time, out_time, registration):
        self.type = type
        self.in_time = in_time
        self.out_time = out_time
        self.registration = registration

class ParkingLot:
    rows = None
    cols = None
    cells = None
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell for x in range(cols)] for y in range(rows)] # 2D array of Cell objects, which in turn contain Vehicle objects

