def sum_euler(sum, st_num, en_num):
    for num in range(st_num, en_num):
        if ((num%3) * (num%5) == 0): #  if (( num % 3 ) == 0) or ((num % 5) == 0):
            sum += num

       # else:
           # pass 

    return sum

print(sum_euler( 0, 0, 1000))
