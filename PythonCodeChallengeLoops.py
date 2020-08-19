def divisible_by_ten(nums) : 
    count = 0
    for i in nums : 
        if i%10 == 0 : 
            count += 1

    return count

def add_greetings(names) : 
    new_list = []
    for i in names : 
        new_list.append("Hello, " + i)

    return new_list

def delete_starting_evens(lst) : 
    while (len(lst) > 0 and lst[0] % 2 == 0) : 
        lst = lst[1:]
    return lst

def odd_indices(lst) : 
    new_lst = []
    i = 0
    while i < (len(lst)): 
        if i%2 != 0 : 
            new_lst.append(lst[i])
            i += 1
        else : 
            i += 1
    return new_lst

def exponents(bases, powers) : 
    new_list = []
    for base in bases : 
        for power in powers : 
            new_list.append(base**power)
    return new_list

def larger_sum(lst1, lst2) : 
    sum1 = 0
    sum2 = 0
    for number in lst1: 
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum2 > sum1 : 
        return lst2
    else : 
        return lst1

def over_nine_thousand(lst) : 
    sum = 0 
    for i in lst:
        if sum < 9000 : 
            sum += i
        else : 
            break
    return sum

def max_num(nums) : 
    highest = nums[0]
    for i in nums : 
        if i > highest : 
            highest = i
    return highest

def same_values(num1, num2) : 
    indice_list = []
    for indice1 in range(len(num1)) : 
        if num1[indice1] == num2[indice1] :
            indice_list.append(indice1)
    return indice_list

def reversed_list(lst1, lst2) : 
    for i in range(len(lst1)) : 
        if lst1[i] != lst2[len(lst2) -1 - i] : 
            return False 
    return True