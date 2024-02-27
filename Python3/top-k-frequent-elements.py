def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency_list = {}
    result = []
    for i in nums:
        if i in frequency_list:
            frequency_list[i] += 1
        else:
            frequency_list[i] = 1
    print(frequency_list)
    while k > 0:
        result.append(max(frequency_list, key=frequency_list.get))
        frequency_list.pop(max(frequency_list, key=frequency_list.get))
        k -= 1
    print(result)
    return result

testList = [1,1,1,2,2,3]
#testList = [-1,-1]
result = topKFrequent(testList, 2)
print(result)


