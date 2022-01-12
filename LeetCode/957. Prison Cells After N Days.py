class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        if n == 0:
            return cells
        # 0 1 0 1 1 0 0 1

        init = int("".join([str(i) for i in cells]), 2)  # 01011001 /89

        status = []

        while True:
            current_status = status[-1] if status else init

            next_status = (~((current_status << 1) ^ (current_status >> 1))) & (
                        (1 << (len(cells) - 1)) - 2)

            if status and next_status == status[0]:
                break

            status.append(next_status)

        k = len(status)

        idx = (n - 1) % k

        return [int(i) for i in "{0:08b}".format(status[idx])]

