import datetime
from parking import ParkingLot, Vehicle

ROWS = 2
COLS = 12
SEP_INDEX = 4

# testing the ParkingLot Class:
parking_lot = ParkingLot(ROWS, COLS, SEP_INDEX)

# offsets = [10, 99, 12, 45, 12, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 16, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# current_time = datetime.datetime.now()

# parking_lot.assign_cell(Vehicle(type='car', in_time=current_time, out_time=current_time + datetime.timedelta(seconds=offsets[0]+69), id=f'{offsets[0]}Test{offsets[0]}'))



# for i in offsets:
#     cell = parking_lot.assign_cell(Vehicle(type='bike', in_time=current_time, out_time=current_time + datetime.timedelta(seconds=i), id=f'{i}Test{i}'))
#     if not cell:
#         print("Parking Lot is full, didn't assign a cell")
#     else:
#         print(f'Assigned cell: {cell}')
#     parking_lot.display()

# Add 4 cars to the parking lot:
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car1'))
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car2'))
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car3'))
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car4'))
parking_lot.display()

# Add 1 bike to the parking lot:
parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike1'))
parking_lot.display()

# Add 1 car to the parking lot:
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car5'))
parking_lot.display()

# Try to add another car to the parking lot:
parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car6'))
parking_lot.display()

# Remove a car from the parking lot:
parking_lot.remove_vehicle(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car1'))
parking_lot.display()
