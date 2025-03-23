class Elevator:
    def __init__(self, hfloor, lfloor, floor = 0):
        self.hfloor = hfloor
        self.lfloor = lfloor
        self.floor = floor

    def move(self, target_floor):
        print(self.floor)
        if target_floor > self.hfloor:
            target_floor = self.hfloor
        elif target_floor < self.lfloor:
            target_floor = self.lfloor

        while self.floor < target_floor:
            self.floor += 1
            print(f'{self.floor}')

        while self.floor > target_floor:
            self.floor -= 1
            print(f'{self.floor}')


elevator1 = Elevator(10,0,0)

while True:
    print(f'\nOlet nyt kerroksessa {elevator1.floor}')
    print(f'Mihin kerrokseen haluat siirtyä? {elevator1.lfloor}/{elevator1.hfloor}\n')
    move = input()

    if move == '':
        break
    else:
        move = int(move)
        elevator1.move(move)




