import sys

def _max_subseq(nums):
    part_sum = [-1 for _ in xrange(len(nums))]
    part_sum[0] = nums[0]
    for i in xrange(1,len(nums)):
        part_sum[i] = part_sum[i-1] + nums[i]

    end = 1
    min_sum = part_sum[end]
    max_sum = part_sum[end]
    ret_val = 0
    # while end < len(nums):
    #     if part_sum[end] < min_sum
    #         ret_val = max_sum - min_sum
    #         min_sum = part_sum[end]
    #     if part_sum[end] > max_sum
    #         max_sum = part_sum[end]
    #     if  <= 0 and nums[end]>0:
    #         beg = end
    #     s += nums[end]
    #     if s > max_s:
    #         max_s = s
    #         pos = [beg, end]
    #     elif s < 0:
    #         s = 0
    #     end += 1
    # print pos
    # print max_s


def max_subseq(nums):
    if len(nums) == 0:
        return None
    beg = 0
    end = 0
    cur_sum = nums[end] if nums[end] > 0 else 0
    max_sum = nums[end] if nums[end] > 0 else 0
    end += 1    
    while end < len(nums):
        cur_sum += nums[end]
        if cur_sum > max_sum:
            max_sum = cur_sum
            pos = [beg, end]
        elif cur_sum < 0:
            cur_sum = 0
            beg = end+1
        end += 1
    # print pos
    print max_sum



if __name__ == '__main__':
    # nums = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    nums = [-1, 2]
    print nums
    max_subseq(nums)
