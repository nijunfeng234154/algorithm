
def longest_common_substring1(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    return str1[end_index - max_length:end_index]

def longest_common_substring2(str1, str2):
    max_length = 0
    end_index = 0
    len1, len2 = len(str1), len(str2)

    for i in range(len1):
        for j in range(len2):
            length = 0
            while (i + length < len1) and (j + length < len2) and (str1[i + length] == str2[j + length]):
                length += 1
            if length > max_length:
                max_length = length
                end_index = i + length

    return str1[end_index - max_length:end_index]

# 示例用法
str1 = "abcdefg"
str2 = "xyzabcde"
print("最长公共子串是:", longest_common_substring1(str1, str2))