

def func_b1(nums, target):
    """
二分查找的最基础和最基本的形式。
查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）。
不需要后处理，因为每一步中，你都在检查是否找到了元素。如果到达末尾，则知道未找到该元素。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xe5fpe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def func_b2(nums, target):
    """
    一种实现二分查找的高级方法。
查找条件需要访问元素的直接右邻居。
使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
保证查找空间在每一步中至少有 2 个元素。
需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xerqxt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    :param nums:
    :param target:
    :return:
    """

    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left != len(nums) and nums[left] == target:
        return left

    return -1