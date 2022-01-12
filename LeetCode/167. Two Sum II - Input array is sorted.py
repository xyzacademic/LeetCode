class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers or len(numbers) == 0 or \
                numbers[-2] + numbers[-1] < target or numbers[0] + numbers[1] > target:
            return []

        i = 0
        j = len(numbers) - 1

        while i < j:
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            temp_sum = numbers[i] + numbers[j]
            if temp_sum == target:
                return [i + 1, j + 1]
            elif temp_sum < target:
                i += 1
                while i < j and numbers[i] == numbers[i - 1]:
                    i += 1
            else:
                j -= 1
                while i < j and numbers[j] == numbers[j + 1]:
                    j -= 1
