## Bubble sort function
def bubblesort(elements):
    size=len(elements)

    ## size-1 no of iterations
    for i in range(size-1):
        ##Swapped flag
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                #Swapping code
                tmp = elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=tmp
                swapped=True

        if not swapped:
            break

# elements = [5,9,2,1,67,34,88,34]
# # elements = [1,2,3,4,2]
elements = ["mona", "jubal", "aamir", "aryan", "chang"]

bubblesort(elements)
print(elements)       
