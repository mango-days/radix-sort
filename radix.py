array = [170, 45, 75, 90, 802, 24, 2, 66]

def countingSort ( array, exp ) :
    output = [0] * len(array)
    count = [0] * (10)
    
    for i in range ( 0, len(array) ) :
        index = int (array[i] / exp)
        count[ index % 10 ] += 1
        
    for i in range ( 1, 10 ) : count[i] += count[i - 1]
    
    i = len(array) - 1
    while i >= 0:
        index = int (array[i] / exp)
        output[ count[ index % 10 ] - 1] = array[i]
        count[ index % 10 ] -= 1
        i -= 1
        
    return output

max_count = max(array)
exp = 1
while (max_count / exp) > 1 :
    array = countingSort (array, exp)
    exp *= 10
    
print( array )
