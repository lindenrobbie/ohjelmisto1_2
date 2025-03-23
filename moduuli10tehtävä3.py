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

    def firealarm(self):
        building.move(0, 0)
        building.move(1, 0)
        print('Ring ring ring... Palohälytys')
        print(f'Hissit ovat nyt 0 kerroksessa.')


building = Building(0, 10, 2)

building.move(0, 5)
building.move(1, 8)
building.move(0, 10)

building.firealarm()