def judge(list):
    for i in range(len(list)):
        if list[0:i] == sorted(list[0:i]) and list[i:] == sorted(list[i:], reverse=True):
            return True
    return False

def main():
    list = [1, 2, 3, 4, 5, 4, 3, 5]
    print(judge(list))

if __name__ == '__main__':
    main()