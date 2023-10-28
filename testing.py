import datetime
from parking import ParkingLot, Vehicle
import time

ROWS = 2
COLS = 2
SEP_INDEX = 2

DELAY = 0.25
SHORT_DELAY = 0.1

import tkinter as tk

class ParkingLotGUI:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.update_display()

    def add_gap(self, j):
        if j >= self.parking_lot.separator_index:
            return 20
        else:
            return 0

    def update_display(self):
        self.canvas.delete("all")
        cell_width = 45
        cell_height = 75
        gap = 0
        left_margin = 20
        top_margin = 20

        for i in range(self.parking_lot.rows):
            for j in range(self.parking_lot.cols):
                x0 = j * (cell_width + gap) + left_margin + self.add_gap(j)
                y0 = i * (cell_height + gap) + top_margin
                x1 = x0 + cell_width
                y1 = y0 + cell_height

                if self.parking_lot.cells[i][j].status is None:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="darkgrey")
                else:
                    if self.parking_lot.cells[i][j].status.type == 'bike':
                        self.canvas.create_rectangle(x0, y0, x1, y1, fill="orange")
                        vehicle_id = self.parking_lot.cells[i][j].status.id
                        self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=vehicle_id)
                    elif self.parking_lot.cells[i][j].status.type == 'car':
                        self.canvas.create_rectangle(x0, y0, x1, y1, fill="cyan")
                        vehicle_id = self.parking_lot.cells[i][j].status.id
                        self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=vehicle_id)

        self.root.update()

# Now, you can use this ParkingLotGUI class in your code:

# Initialize your parking_lot
parking_lot = ParkingLot(ROWS, COLS, SEP_INDEX)

# Create an instance of the GUI
gui = ParkingLotGUI(parking_lot)

# Whenever you call gui.update_display(), it will update the visual representation of the parking lot.




# testing the ParkingLot Class:
# parking_lot = ParkingLot(ROWS, COLS, SEP_INDEX)

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

gui.update_display()

# #delay 1s
# time.sleep(1)

# # Add 4 cars to the parking lot:
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car1'))
# gui.update_display()
# parking_lot.display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car2'))
# gui.update_display()
# parking_lot.display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car3'))
# gui.update_display()
# parking_lot.display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car4'))
# gui.update_display()
# parking_lot.display()
# time.sleep(1)
# gui.update_display()
# parking_lot.display()

# #delay 1s
# time.sleep(1)

# # Add 1 bike to the parking lot:
# parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike1'))
# parking_lot.display()
# gui.update_display()

# time.sleep(1)

# # Add 1 car to the parking lot:
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car5'))
# parking_lot.display()
# gui.update_display()

# time.sleep(1)

# # Try to add another car to the parking lot:
# parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car6'))
# parking_lot.display()
# gui.update_display()

# time.sleep(1)

# # Remove a car from the parking lot:
# parking_lot.remove_vehicle(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='car1'))
# parking_lot.display()
# gui.update_display()

# time.sleep(1)

# # Add 4 bikes to the parking lot:
# parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike2'))
# gui.update_display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike3'))
# gui.update_display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike4'))
# gui.update_display()
# time.sleep(1)
# parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id='bike5'))
# gui.update_display()
# time.sleep(1)
# parking_lot.display()
# time.sleep(1)


# Actual Test Code:
# Test for:
# 1. Filling the entire parking lot with cars and bikes
# 2. Removing all the cars and bikes from the parking lot (in reverse order of their entrances to the parking lot)
# 3. Filling the entire parking lot with only cars
# 4. Removing all the cars from the parking lot
# 5. Filling the entire parking lot with only bikes
# 6. Removing all the bikes from the parking lot
# 7. Partially fill the parking lot with cars, and then fill all remaining spots with bikes
# 8. Partially fill the parking lot with bikes, and then fill all remaining spots with cars
# 9. Remove all vehicles from the parking lot

# The gui has to update for every step, along with a half-second delay. Use loops to do this.
# Do note though that the maximum number of cars = (ROWS * COLS)/4, and the maximum number of bikes = (ROWS * COLS)

# 1. Filling the entire parking lot with cars and bikes
for i in range(ROWS * int((COLS - SEP_INDEX) / 4)):
    parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    gui.update_display()
    time.sleep(DELAY)
for i in range(ROWS * SEP_INDEX):
    parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    gui.update_display()
    time.sleep(DELAY)

# 2. Removing all the cars and bikes (in reverse order to their addition):
for i in range(ROWS * SEP_INDEX - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    gui.update_display()
    time.sleep(DELAY)
for i in range(ROWS * int((COLS - SEP_INDEX) / 4) - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    gui.update_display()
    time.sleep(DELAY)

# 3. Filling the entire parking lot with only cars
for i in range(int(ROWS * COLS / 4)):
    parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    print(f'car{i} added')
    gui.update_display()
    time.sleep(DELAY)

# 4. Removing all the cars from the parking lot
for i in range(int(ROWS * COLS / 4) - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    print(f'car{i} removed')
    gui.update_display()
    time.sleep(DELAY)

# 5. Filling the entire parking lot with only bikes
for i in range(ROWS * COLS):
    parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    print(f'bike{i} added')
    gui.update_display()
    time.sleep(SHORT_DELAY)

# 6. Removing all the bikes from the parking lot
for i in range(ROWS * COLS - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    print(f'bike{i} removed')
    gui.update_display()
    time.sleep(SHORT_DELAY)

# 7. Partially fill the parking lot with cars, and then fill all remaining spots with bikes
for i in range(int(ROWS * COLS / 4)):
    parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    print(f'car{i} added')
    gui.update_display()
    time.sleep(SHORT_DELAY)

for i in range(int(ROWS * COLS / 4), ROWS * COLS):
    parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    print(f'bike{i} added')
    gui.update_display()
    time.sleep(SHORT_DELAY)

# 8. Partially fill the parking lot with bikes, and then fill all remaining spots with cars
for i in range(ROWS * COLS):
    parking_lot.assign_cell(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    print(f'bike{i} added')
    gui.update_display()
    time.sleep(SHORT_DELAY)

for i in range(ROWS * COLS):
    parking_lot.assign_cell(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    print(f'car{i} added')
    gui.update_display()
    time.sleep(SHORT_DELAY)

# 9. Remove all vehicles from the parking lot
for i in range(ROWS * COLS - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='car', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'car{i}'))
    print(f'car{i} removed')
    gui.update_display()
    time.sleep(SHORT_DELAY)

for i in range(ROWS * COLS - 1, -1, -1):
    parking_lot.remove_vehicle(Vehicle(type='bike', in_time=datetime.datetime.now(), out_time=datetime.datetime.now() + datetime.timedelta(seconds=100), id=f'bike{i}'))
    print(f'bike{i} removed')
    gui.update_display()
    time.sleep(SHORT_DELAY)

