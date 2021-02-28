# This is a test program. This program outputs a list of triangular numbers.
# n is the largest traingular number


# The perfect square formala follows: x = (n(n+1))/2

def traingularnumbers(n):
    list = []               # Creating a blank list
    for i in range(n):
        #list = list + (i*(i+1))/2
        list.append((i*(i+1))/2)
    return list

print(traingularnumbers(20))