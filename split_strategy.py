def split(list_i, current_sum, target_sum, depth, res_list):
    depth += 1
    if (current_sum == target_sum) or depth > 20:
        return res_list
    for i in range(1, target_sum):
        if i == 1 or i ==3 :
            list_i.append(i)
            if current_sum + i != target_sum:
                split(list_i, current_sum + i, target_sum, depth, res_list)
            if current_sum + i == target_sum:
                res_list.append(list_i[:])  # 添加 list_i 的副本
            list_i.pop()
    return res_list

if __name__ == '__main__':
    print(split([], 0, 4, 0, []))
