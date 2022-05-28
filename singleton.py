import sys
'''length of list guaranteed to be odd (only one singleton and only one repeat of matching non-singleton values
    Given a sorted list of integers where single non-repeating element exists among other once-repeating integers,
    return this unique element
    Because we know this length of the list MUST be odd we can separate the algorithm into 3 different base cases
    and utilize a Divide and Conquer strategy using Binary Search.
    Divide the list in half and the mid point and check the length of both sides:
    Case 1: Base Case, length of list is 1 and thus unique so return element
    Case 2: The left side of the list is larger, thus the singleton element must be on the left side, repeat over and over
    until left with a single element
    Case 3: The right side of the list is larger (odd), repeat as above)'''


def singleton(sorted):
    mid = len(sorted) // 2

    if len(sorted) == 0:
        return 0

    if len(sorted) == 1:
        return sorted[0]

    elif sorted[mid] == sorted[mid + 1]:  #if midpoint has a matching value to right of it
        right = len(sorted) - mid
        if right % 2 == 0:    #if right side of list even ignore this and update list in order to decrease run time complexity
            return singleton(sorted[0: mid])

        return singleton(sorted[mid + 2:])    #if right side of list odd ignore right and slice list to decrease run time

    elif sorted[mid] == sorted[mid - 1]:  #if midpoint has matching value to left of it
        left = mid + 1
        if left % 2 == 0:  #if left side of list is even ignore and return the upper side of the (odd numbered) list
            return singleton(sorted[mid+1:])

        return singleton(sorted[0:mid-1])   # if left side of list odd, go into this one and ignore rest

    return sorted[mid]   #if midpoint value has no matching partners to left or right then you know this is the unique element (b/c sorted list); O(1) Best Case

#O(log(n)) worst case because log2(n) depth of tree and O(1) time to combine
#O(1) Space Complexity



def main(argv): 
    f = open(argv,'r') 
    read = f.readline().rstrip('\n').split(",")
    i = 0 
    while i < len(read):
        read[i] = int(read[i])
        i += 1
    print(singleton(read))

if __name__ == "__main__":
    main(sys.argv[1]) 

