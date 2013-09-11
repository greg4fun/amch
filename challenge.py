from itertools import combinations


def calculate_combinations(elements, target_sum):
    sumcombinations = 0
    tempsum = 0
    maxquantityofelements = 0
    elements.sort()
    try:
        while (tempsum < target_sum):
            tempsum = tempsum + elements[maxquantityofelements]
            maxquantityofelements += 1
        for z in range(1, maxquantityofelements + 1):
            for comb in combinations(elements, z):
                tempsum = 0
                for el in comb:
                    tempsum += el
                if(tempsum == target_sum):
                    sumcombinations += 1
        return sumcombinations
    except Exception as e:
        print e
#arr1 = [5, 10, 15, 5]
#tsum = 15
#print calculate_combinations(arr1, tsum)
