import sys

def is_win(T, m_lis): # return True if every num in m_lis is in T
    if not m_lis:
        return True
    for num in m_lis:
        if num in T:
            return True and is_win(T, m_lis[1:])
        else:
            return False

if __name__ == "__main__":
    # 读取第一行的n
    n_m = sys.stdin.readline().split()
    n = int(n_m[0])
    m = int(n_m[1])
    m_lis = []
    for i in range(1, m+1): # m_lis = [1,2,3] if m = 3
        m_lis.append(i)
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    shot_colors = list(map(int, line.split()))
    left = 0
    right = 1
    T = shot_colors[left:right+1]
    while right < len(shot_colors):
        if is_win(T, m_lis):
            print(len(T))
            break
        if shot_colors[right] == T[0]:
            left += 1
        right += 1
        T = shot_colors[left:right+1]