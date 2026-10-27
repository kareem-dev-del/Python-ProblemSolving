#solve 1
# O(n²)

def Two_sum(nums,target):
    
    for i in range(len(nums)):
        for j in range(i + 1 ,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(Two_sum([1,2,3,4,5,6],6))


#solve 2
# o(n)

def Two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i

print(Two_sum([1, 2, 3, 4, 5, 6], 6))