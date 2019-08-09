def douyin():
    # 1. 给你一个很大的文件，文件里有很多行数据，每一行数据是一个用户的uid，
    # 表示这个用户点开过抖音，请你找出打开抖音次数最频繁的前10个用户。
    import sys
    lines = sys.stdin.readlines()

    new_lis = [line.strip() for line in lines]

    import collections
    cnt = collections.Counter(new_lis).most_common(10)

    res = []
    for v, f in cnt:
        res.append(v)

    return res


def max_length(s):
    # 2. 给定一个字符串，请找出其中无重复字符的最长子字符串的长度
    # 思路：先求出这个字符串的所有子字符串；
    # 然后再求其中没有重复字符的子字符串；
    # 最后求这些子字符串中长度最长的那一个。
    res = []
    for i in range(len(s)):
        if s[i] not in res:
            res.append(s[i])
        for j in range(i + 1, len(s)):
            tmp = [v for v in s[i: j + 1]]
            if s[i:j + 1] not in res and len(list(set(tmp))) == len(tmp):
                res.append(s[i:j + 1])
    res_len = list(map(len, res))

    return max(res_len)


# s = 'abcabcbb'
# s = 'bbbbb'
# print(max_length(s))


def num_depart(grid):
    # 3. 给定一个M*M的二维数组，每个值为1的元素代表一个团队。如果两个团队在上下或左右两个方向上相邻，
    # 说明两个团队有紧密合作关系。将有紧密合作关系的两个团队合并。判断给定输入合并之后有几个部门

    # 思路：使用dfs统计矩阵中有多少个连通区域，这里的连通定义为上下左右相邻。
    # 遍历矩阵的每一个元素，如果当前元素是1，部门数 + 1，同时从当前位置开始进行深搜（dfs），碰到0回退，碰到1则翻成0，这样便把与该位置1相连的所有1都变成了0；
    # 如果当前元素是0，则跳过。
    # 遍历结束后便可以统计出连通区域有多少个，即部门数。
    m = len(grid)

    if m == 0:
        return 0

    n = len(grid[0])

    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j]:
            grid[i][j] = False
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                count += 1
                dfs(grid, i, j)

    return count


# grid = [[1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
# grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
# res = num_depart(grid)
# print(res)


def debug_ip(s):
    # 4. 工程师小张的代码出了bug。再上报用户IP的时候，漏掉了‘.’符号。例如10.0.0.1，变成了10001.
    # 请你帮小张处理这些异常情况，还原出所有可能的异常IP, 输出可能的原始IP的数量。
    res = []

    length = len(s)

    if length > 12 or length < 4:
        return 0

    for i in range(1, 4):
        if i < length - 2:
            for j in range(i + 1, i + 4):
                if j < length - 1:
                    for k in range(j + 1, j + 4):
                        if k < length:
                            if length - k >= 4:
                                continue
                            if s[:i][0] == '0':
                                continue
                            elif s[i:j][0] == '0' and len(s[i:j]) > 1:
                                continue
                            elif s[j:k][0] == '0' and len(s[j:k]) > 1:
                                continue
                            elif s[k:][0] == '0' and len(s[k:]) > 1:
                                continue
                            a = int(s[:i])
                            b = int(s[i:j])
                            c = int(s[j:k])
                            d = int(s[k:])

                            if (a >= 1 and a <= 255) or (b >= 0 and b <= 255) or (c >= 0 and c <= 255) or (d >= 0 and d <= 255):
                                res.append(str(s) + '.' + str(b) + '.' + str(c) + '.' + str(d))

    return len(res)


# s = '10001'
# s = '8888'
# print(debug_ip(s))


def if_utf8(lis):
    # 5. 给定一个整数数组表示的数据，判断其是否为有效的utf-8编码。
    def int2bin(num):
        s = ''
        while num > 0:
            s = str(num % 2) + s
            num //= 2
        if len(s) < 8:
            s = '0' * (8 - len(s)) + s
        return s

    new_lis = list(map(int2bin, lis))

    im = new_lis[0]

    num_byte = 0
    for i in im:
        if i == '1':
            num_byte += 1
        if i == '0':
            break
    for j in range(1, num_byte):
        if new_lis[j][:2] != '10':
            return False
    return True

# class Solution(object):
#     def validUtf8(self, data):
#         """
#         :type data: List[int]
#         :rtype: bool
#         """
#         masks = [0x0, 0x80, 0xE0, 0xF0, 0xF8]
#         bits = [0x0, 0x0, 0xC0, 0xE0, 0xF0]
#         while data:
#             for x in (4, 3, 2, 1, 0):
#                 if data[0] & masks[x] == bits[x]:
#                     break
#             if x == 0 or len(data) < x:
#                 return False
#             for y in range(1, x):
#                 if data[y] & 0xC0 != 0x80:
#                     return False
#             data = data[x:]
#         return True
# print(if_utf8([197, 130, 1]))


def famousPlayer(num, gx_list):
    # 抖音工程师想要找到抖音中的红人，假设用户数为N,有M个关注关系对(A, B), 表示A关注了B.
    # 关注关系具有传递性，A->B, B->C则可推出A->C。如果一个用户被所有N个用户直接或间接关注，
    # 那么我们认为这个用户就是抖音红人，求抖音红人的总数
    import collections
    gx_dict = collections.defaultdict(set)  # key表示用户，value为list，表示谁关注了他
    for i, x in enumerate(gx_list):
        if i % 2 != 0:  # 奇数表示拿到的是关注的对象 奇数前面的偶数表示关注此对象的人
            gx_dict[x].add(x)
            gx_dict[x].add(gx_list[i - 1])  # key是被关注的，value是玩家

    for i in range(int(num)):  # 遍历所有的用户。需要多次检测，因为有间接的关注关系
        for star, user in gx_dict.items():  # star 表示被关注的人， user表示关注者
            add_people = set()
            for x in user:
                if x in gx_dict:
                    add_people |= gx_dict[x]  # 取并集
            gx_dict[star] |= add_people

    star_num = 0
    for star, user in gx_dict.items():
        if len(user) == int(num):
            star_num += 1
    return star_num

print(famousPlayer(3, [1, 2, 2, 1, 2, 3]))