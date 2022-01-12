class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return False

        i = 0
        while i < len(bits) - 1:

            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == len(bits) - 1