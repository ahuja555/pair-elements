# class pair_elements:
class pair_elements:

    def twosum(self,nums, target):
        # create an empty dictionery
        lookup = {}
       # iterate through the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
# take input from user
value = int(input("Enter sum from which you want to make search" ": "))
print("index1 = %d, index2 = %d" % (pair_elements().twosum((10, 20, 30, 40, 50, 60, 70), value)))  