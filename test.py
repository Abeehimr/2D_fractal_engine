def main(nums):
    out = 0
    l , r = 0 , 0
    while l < len(nums):
        if nums[l] == nums[r]:
            out += 1
            if r != len(nums)-1:r += 1
            else:
                l += 1
                r = l
        elif nums[l] > nums[r]:       
            if r != len(nums)-1:r += 1
            else:
                l += 1
                r = l
        else:
            out += r - l - 1
            l = r
            
    # for l in range(len(nums)):
    #     for r in range(l,len(nums)):
    #         if nums[l] == nums[r]:
    #             out += 1
    #         elif nums[l] < nums[r]:
    #             break
    return out


if __name__ == "__main__":
    print(main([145,147,147,147,149,147,150,149,148,149]))