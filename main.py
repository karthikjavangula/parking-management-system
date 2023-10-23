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
        self.car_cell_groups2 = [[(0, i), (0, i + 1), (1, i), (1, i + 1)] for i in range(int(separator_index-1))]
    
    def assign_cell(self, vehicle):
        if self.get_vehicle(vehicle.id) is not None:
            print('Vehicle already exists in the parking lot')
            return 0
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
            if self.car_in_car_range(vehicle):
                return self.get_vehicle(vehicle.id)
            elif self.car_in_bike_range(vehicle):
                return self.get_vehicle(vehicle.id) 
        else:
            return None
    

    def remove_vehicle(self, vehicle):
        if vehicle.type == 'car':
            group = self.get_vehicle(vehicle.id)
            if group:
                for i, j in group:
                    self.cells[i][j].status = None
                return group
            else:
                return None
        elif vehicle.type == 'bike':
            cell = self.get_vehicle(vehicle.id)
            if cell:
                self.cells[cell[0]][cell[1]].status = None
                return cell
            else:
                return None
    

    def get_vehicle(self, vehicle_id):
        for cellrows in self.cells:
            for cell in cellrows:
                if cell.status is not None:
                    if cell.status.id == vehicle_id:
                        if cell.status.type == 'bike':
                            return (cell.x, cell.y)
                        elif cell.status.type == 'car':
                            for group in self.car_cell_groups:
                                if (cell.x, cell.y) in group:
                                    return group
        return None
            
    
    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].status is None:
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
            if self.cells[0][i].status is None and self.cells[1][i].status is None:
                self.cells[0][i].status = vehicle
                return (0, i)
        # Create a list of all 1st row cells that are empty
        empty_cells = [i for i in range(start_col, end_col) if self.cells[1][i].status is None]
        if len(empty_cells) == 0:
            return None
        out_times = [self.cells[1][cell].constraints[0].status.out_time for cell in empty_cells]
        # Now create a dict by zipping empty cells and their respective constraint out-times. Structure of dict should be {'cell': cell, 'out_time': out_time}
        dict_cells = [{'col': empty_cells[i], 'out_time': out_times[i]} for i in range(len(empty_cells))]
        # Now get the element in which the out_time is the maximum
        max_out_time = max(out_times)
        for dict_cell in dict_cells:
            if dict_cell['out_time'] == max_out_time:
                self.cells[1][dict_cell['col']].status = vehicle
                return (1, dict_cell['col'])
        return None

    def bike_in_car_range(self, vehicle):
        # 2 columns at a time, check if any of the 4 cells is empty
        for i in range(self.separator_index, self.cols, 2):
            if self.bike_in_range(vehicle, start_col=i, end_col=i+2):
                return self.get_vehicle(vehicle.id)
        return None
    

    def car_in_car_range(self, vehicle):
        for group in self.car_cell_groups:
            if all(self.cells[i][j].status is None for i, j in group):
                for i, j in group:
                    self.cells[i][j].status = vehicle
                return group
        return None
    

    def car_in_bike_range(self, vehicle):
        for group in self.car_cell_groups2:
            if all(self.cells[i][j].status is None for i, j in group):
                for i, j in group:
                    self.cells[i][j].status = vehicle
                return group
        return None




'''
Space for Code Description
'''
