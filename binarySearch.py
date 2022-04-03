from tracemalloc import stop
import datalist as d

def searchNumber(b,var,high,low):
    if high >= low:
        mid = (high + low) // 2
        if var < b[mid]:                            #checks whether search variable is bigger than midpoint
            return searchNumber(b,var,mid - 1,low)        #runs function with new high index (mid)
        elif var > b[mid]:                          #checks whether search variable is bigger than midpoint
            return searchNumber(b,var,high,mid + 1)       #runs function with new low index (mid)
        elif var == b[mid]:
            print("Found at index:",mid,"\nNumber found is", var)    #result
    else:
        print("not found")

b = d.data.copy() #copies data to b

def main():
    try:
        searchVar = int(input("Please enter a number to search for:\n")) #get userinput to search in b
        searchNumber(b,searchVar,len(b)-1,0) #inputs arr, search variable, highest index, lowest index
    except:
        print("Invalid input detected\n\n")
        main()

main() #run main

