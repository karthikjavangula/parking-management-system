import datetime

ROWS = 2 # Only focusing on 2 rows currently so keep this constant
COLS = 12 # This has to be even (Although I think I can make it work for odd numbers too)
SEP_INDEX = 4 # Number of columns that are reserved for bikes

'''
Note that I'm using the .id and .type keywords for the Vehicle class, but I'm pretty sure it's not a problem as long as they're not used as function names.
'''

class Cell:
    status = None # Usually status will be assigned to a Vehicle object
    x = None
    y = None
    '''
    For Now we're going to use a simple type of constraint, where it's just a list of cells that have to be free in order to use this cell. No complex conditions
    '''
    constraints = None # List of other Cell objects that this Cell is constrained by
    def __init__(self, status, constraints, x=None, y=None):
        self.status = status
        self.constraints = constraints
        self.x = x
        self.y = y

class Vehicle:
    type = None # Whether it is a car or a bike
    in_time = None # Time at which the vehicle entered the parking lot
    out_time = None # Time at which the vehicle is expected to leave the parking lot
    id = None # Unique identifier for the vehicle (PK in the Vehicle table)

    def __init__(self, type, in_time, out_time, id):
        self.type = type
        self.in_time = in_time
        self.out_time = out_time
        self.id = id

class ParkingLot:
    rows = None
    cols = None
    separator_index = None
    cells = None
    bike_range = None
    car_range = None
    car_cell_groups = None
    car_cell_groups_2 = None
    
    
    def __init__(self, rows, cols, separator_index):
        self.rows = rows
        self.cols = cols
        self.separator_index = separator_index
        self.cells = [[Cell(status=None, constraints=None) for x in range(cols)] for y in range(rows)] # 2D array of Cell objects, which in turn contain Vehicle objects
        
        # write the x and y coordinates of each cell:
        for i in range(rows):
            for j in range(cols):
                self.cells[i][j].x = i
                self.cells[i][j].y = j
        
        # all 1st row cells are constrained by their respective 0th row cells
        for i in range(cols):
            self.cells[1][i].constraints = [self.cells[0][i]]
        
        # for i in range(cols):
        #     print(str(self.cells[1][i].constraints))
        
        self.bike_range = [(i, j) for i in range(2) for j in range(separator_index)]
        self.car_range = [(i, j) for i in range(2) for j in range(separator_index, cols)]
        self.car_cell_groups = [[(0, separator_index + 2*i), (0, separator_index + 2*i + 1), (1, separator_index + 2*i), (1, separator_index + 2*i + 1)] for i in range(int((cols-separator_index)/2))]
        self.car_cell_groups2 = [[(0, 2*i), (0, 2*i + 1), (1, 2*i), (1, 2*i + 1)] for i in range(int((cols)/2))]
    
    def assign_cell(self, vehicle):
        if vehicle.type == 'bike':
            # Iterate through the bike_range and check if any of them are empty
            if self.bike_in_range(vehicle, 0, self.separator_index):
                return self.get_vehicle(vehicle.id)
            elif self.bike_in_car_range(vehicle):
                return self.get_vehicle(vehicle.id)
            else:
                return None
        elif vehicle.type == 'car':
            # Iterate through the car_cell_groups and check if any of them are there such that all 4 cells in each group are empty
            for group in self.car_cell_groups:
                if all(self.cells[i][j].status == None for i, j in group):
                    for i, j in group:
                        self.cells[i][j].status = vehicle
                    return group
                else:
                    return None
        else:
            return None
    

    def remove_vehicle(self, vehicle):
        coords = self.get_vehicle(vehicle.id)
        if coords:
            out_vehicle = self.cells[coords[0]][coords[1]].status
            self.cells[coords[0]][coords[1]].status = None
            return out_vehicle
        else:
            return None
    

    def get_vehicle(self, vehicle_id):
        for cellrows in self.cells:
            for cell in cellrows:
                if cell.status != None:
                    if cell.status.id == vehicle_id:
                        return (cell.x, cell.y)
            
    
    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].status == None:
                    print('[  ]', end=' ')
                elif self.cells[i][j].status.type == 'bike':
                    id_str = str(self.cells[i][j].status.id)
                    id_str = id_str[:2]
                    print(f'[{id_str}]', end=' ')
                elif self.cells[i][j].status.type == 'car':
                    print('[CC]', end=' ')
            print()
        print()
    
    def bike_in_range(self, vehicle, start_col, end_col):
        # If any 0th row cell is empty, simply assign it
        for i in range(start_col, end_col):
            if self.cells[0][i].status == None and self.cells[1][i].status == None:
                self.cells[0][i].status = vehicle
                return (0, i)
        # Create a list of all 1st row cells that are empty
        empty_cells = []
        for i in range(start_col, end_col):
            if self.cells[1][i].status == None:
                empty_cells.append((i))
        if len(empty_cells) == 0:
            return None
        out_times = []
        print(empty_cells)
        for cell in empty_cells:
            out_times.append(self.cells[1][cell].constraints[0].status.out_time)
        # Now create a dict by zipping empty cells and their respective constraint out-times. Structure of dict should be {'cell': cell, 'out_time': out_time}
        dict_cells = []
        for i in range(len(empty_cells)):
            dict_cells.append({'col': empty_cells[i], 'out_time': out_times[i]})
        # Now get the element in which the out_time is the maximum
        max_out_time = max(out_times)
        for dict_cell in dict_cells:
            if dict_cell['out_time'] == max_out_time:
                self.cells[1][dict_cell['col']].status = vehicle
                return (1, dict_cell['col'])
        return None

    def car_in_car_range(self):
        pass

    def bike_in_car_range(self, vehicle):
        # 2 columns at a time, check if any of the 4 cells is empty
        for i in range(self.separator_index, self.cols, 2):
            if self.bike_in_range(vehicle, start_col=i, end_col=i+2):
                return self.get_vehicle(vehicle.id)
        return None
        

    def car_in_bike_range(self):
        # This is the case when the car range is full, but the bike range is not full
        # We need to find 4 bike cells in the bike range that are empty and convert them into a car cell
        pass

# testing the ParkingLot Class:
parking_lot = ParkingLot(ROWS, COLS, SEP_INDEX)

offsets = [10, 99, 12, 45, 12, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 16, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
current_time = datetime.datetime.now()

parking_lot.assign_cell(Vehicle(type='car', in_time=current_time, out_time=current_time + datetime.timedelta(seconds=offsets[0]+69), id=f'{offsets[0]}Test{offsets[0]}'))



for i in offsets:
    cell = parking_lot.assign_cell(Vehicle(type='bike', in_time=current_time, out_time=current_time + datetime.timedelta(seconds=i), id=f'{i}Test{i}'))
    if not cell:
        print("Parking Lot is full, didn't assign a cell")
    else:
        print(f'Assigned cell: {cell}')
    parking_lot.display()



'''


What could be the problem here? Ans: The constraints list is empty, so it's throwing an error when I try to access the 0th element of the list. I need to check if the constraints list is empty before accessing the 0th element.
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
'''
