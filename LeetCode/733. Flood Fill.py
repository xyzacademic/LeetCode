class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        """
        111
        110
        101
        """

        if not image:
            return image

        queue = []
        queue.append((sr, sc))
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        while queue:
            cord_x, cord_y = queue.pop(0)
            if image[cord_x][cord_y] == old_color:
                image[cord_x][cord_y] = newColor

                # add neighbor
                # check bound
                if 0 <= cord_x + 1 < len(image):
                    queue.append((cord_x + 1, cord_y))

                if 0 <= cord_x - 1 < len(image):
                    queue.append((cord_x - 1, cord_y))

                if 0 <= cord_y + 1 < len(image[0]):
                    queue.append((cord_x, cord_y + 1))

                if 0 <= cord_y - 1 < len(image[0]):
                    queue.append((cord_x, cord_y - 1))

        return image