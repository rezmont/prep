def longest_nondecreasing_subseq(nums, i):
    global mem
    global last_ptr
    if len(nums) == 0:
        return 0
    if i == 0:
        return nums[0][1]

    if i in mem:
        return mem[i]

    max_l = nums[i][1]
    for j in xrange(i-1):
        if nums[i] > nums[j]:
            l = nums[i][1] + longest_nondecreasing_subseq(nums, j)
            if l>max_l:
                max_l = l
                last_ptr[i] = j
    mem[i] = max_l
    return max_l

mem = {}
people = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95)]
last_ptr = [-1 for _ in xrange(len(people))]
l = longest_nondecreasing_subseq(sorted(people), len(people)-1)
print sorted(people)
print l
print last_ptr