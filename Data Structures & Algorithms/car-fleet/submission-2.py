class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # postition
        # speed
        # target 

        # .   ..    .   . |
        #   .  ..      .  | .
        #       ...       .| 

        # we enumerate them like this:
        # starting with 1/0 with the max position.
        # first is 3->4 (does it reach 4 before 4 reaches end)
        # if yes, then does 2->4
        # else does 2->3
        # so we repeatedly scan the same condition. and don't need to do it n**2 times but only n times roughly

        cars = sorted(zip(position, speed), key=lambda car: car[0], reverse=True)
        total = len(cars)
        fleet_count = total
        ahead_pointer = 0
        behind_pointer = 1
        while behind_pointer<total:
            if self.reaches(cars[behind_pointer], cars[ahead_pointer], target):
                fleet_count -= 1
            else:
                ahead_pointer = behind_pointer
            behind_pointer +=1
        return fleet_count
                

    def reaches(self, car1, car2, target):
        """car1 behind car2"""
        x1 = car1[0]
        v1 = car1[1]
        x2 = car2[0]
        v2 = car2[1]

        d1 = target - x1
        d2 = target - x2
        t1 = d1/v1
        t2 = d2/v2
        return t1<=t2




