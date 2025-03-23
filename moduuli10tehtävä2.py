class Elevator:
    def __init__(self, lfloor, hfloor):
        self.lfloor = lfloor
        self.hfloor = hfloor
        self.current_floor = lfloor

    def go_up(self):
        if self.current_floor < self.hfloor:
            self.current_floor += 1
            print(f"{self.current_floor}")

    def go_down(self):
        if self.current_floor > self.lfloor:
            self.current_floor -= 1
            print(f"{self.current_floor}")

    def move_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.go_up()
        while self.current_floor > target_floor:
            self.go_down()


class Building:
    def __init__(self, lfloor, hfloor, number_of_elevators):
        self.elevators = [Elevator(lfloor, hfloor) for i in range(number_of_elevators)]

    def move(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Hissi {elevator_number} siirtyy kerrokseen {target_floor}")
            self.elevators[elevator_number].move_to_floor(target_floor)


building = Building(0, 10, 2)

while True:
    print(f'\nKumman hissin haluat siirtää? (0/1)')
    elevator_choice = input()

    if elevator_choice == '':
        break
    else:
        elevator_choice = int(elevator_choice)

    print(f'Mihin kerrokseen haluat hissi {elevator_choice} siirtyy? 0 / 10')
    target_floor = input()

    if target_floor == '':
        break
    else:
        target_floor = int(target_floor)

    building.move(elevator_choice, target_floor)