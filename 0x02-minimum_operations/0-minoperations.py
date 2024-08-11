#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Calculate min number of operations required to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    operation_num = 0
    done = 1
    start = 0

    while done < n:
        if start == 0:
            start = done
            done += start
            operation_num += 2
        
        elif (n - done) % done == 0:
            start = done
            done += start
            operation_num += 2

        elif start > 0:
            done += start
            operation_num += 1

    
    return operation_num
