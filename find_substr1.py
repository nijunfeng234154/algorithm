

def find_substr(s1,s2):
    max_length = 0
    end_index = len(s1)
    for i in range(len(s1)):
        length = 0
        for j in range(len(s2)):
            while i+length<len(s1) and j+length<len(s2) and s1[i+length]==s2[j+length]:
                length+=1
            if length>max_length:
                max_length = length
                end_index = i+length

    return s1[end_index-max_length:end_index]


if __name__ == '__main__':
    print(find_substr('abcdesf','acdessa'))