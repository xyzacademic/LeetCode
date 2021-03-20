class Solution:
    def __init__(self, heights, plate=None):
        self.heights = heights
        self.plate = plate

    def solve(self,):

        self.moveTower(self.heights, self.plate[0], self.plate[2], self.plate[1])


    def moveTower(self, height, fromPlate, toPlate, withPlate):
        if height > 0:
            self.moveTower(height - 1, fromPlate, withPlate, toPlate)
            self.move(fromPlate, toPlate)
            self.moveTower(height - 1, withPlate, toPlate, fromPlate)

        return

    def move(self, fromPlate, toPlate):
        print("Moving from {fromPlate} to {toPlate}".format(fromPlate=fromPlate, toPlate=toPlate))
        return


if __name__ == '__main__':

    plate = ["A", "B", "C"]
    height = 3

    solution = Solution(height, plate)

