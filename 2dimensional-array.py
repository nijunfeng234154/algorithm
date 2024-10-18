def find_num_in_2darray(arr,target):
    rows = len(arr)
    columns = len(arr[0])
    row = 0
    column = columns-1
    while row < rows and column >=0 :
        if arr[row][column] == target:
            return True
        elif arr[row][column] > target:
            column -= 1
        else:
            row += 1
    return False

def main():
    arr = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 16
    print(find_num_in_2darray(arr,target))

if __name__ == '__main__':
    main()
