from collections import deque
initial = "OXXXXXXXXXXXXXX"
goal = "XOOOOOOOOOOOOOO"


class Peg:
    def __init__(self, state, parent, path_length):
        self.state = state
        self.parent = parent
        self.path_length = path_length

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_path_length(self):
        return self.path_length


def print_puzzle(state):
    for a in range(0, len(state)):
        if a == 0 or a == 2 or a == 5 or a == 9:
            print(state[a])
        else:
            print(state[a] + " ", end="", flush=True)
    print()
    print()


def swap(s, a, b):
    n = list(s)
    temp = n[a]
    n[a] = n[b]
    n[b] = temp
    return ''.join(n)


def remove(s, a):
    n = list(s)
    n[a] = "O"
    return ''.join(n)


def get_children(state):
    children = []
    blank_index = []
    for i in range(0, len(state)):
        if state[i] == "O":
            blank_index.append(i)
    for j in blank_index:
        r = row(j)
        if r < 3:
            (a, b) = diagonal_down(r)
            (c, d) = r_diagonal_down(r)
            if state[j + a] == "X":
                if state[j + c] == "X":
                    left = swap(state, j, j + a)
                    left = remove(left, j + c)
                    children.append(left)
            if state[j + b] == "X":
                if state[j + d] == "X":
                    right = swap(state, j, j + b)
                    right = remove(right, j + d)
                    children.append(right)
            if state[j + c] == "X":
                move = swap(state, j, j + c)
                children.append(move)
            if state[j + d] == "X":
                move2 = swap(state, j, j + d)
                children.append(move2)
        if r > 1:
            if j == 3:
                if state[0] == "X" and state[1] == "X":
                    up1 = swap(state, 3, 0)
                    up1 = remove(up1, 1)
                    children.append(up1)
            if j == 6:
                if state[1] == "X" and state[3] == "X":
                    up2 = swap(state, 6, 1)
                    up2 = remove(up2, 3)
                    children.append(up2)
            if j == 10:
                if state[3] == "X" and state[6] == "X":
                    up3 = swap(state, 10, 3)
                    up3 = remove(up3, 6)
                    children.append(up3)
            if j == 7:
                if state[2] == "X" and state[4] == "X":
                    up4 = swap(state, 7, 2)
                    up4 = remove(up4, 4)
                    children.append(up4)
            if j == 11:
                if state[4] == "X" and state[7] == "X":
                    up5 = swap(state, 11, 4)
                    up5 = remove(up5, 7)
                    children.append(up5)
            if j == 12:
                if state[3] == "X" and state[7] == "X":
                    up6 = swap(state, 12, 3)
                    up6 = remove(up6, 7)
                    children.append(up6)
                if state[5] == "X" and state[8] == "X":
                    up7 = swap(state, 12, 5)
                    up7 = remove(up7, 8)
                    children.append(up7)
            if j == 8:
                if state[1] == "X" and state[4] == "X":
                    up8 = swap(state, 8, 1)
                    up8 = remove(up8, 4)
                    children.append(up8)
            if j == 13:
                if state[4] == "X" and state[8] == "X":
                    up9 = swap(state, 13, 4)
                    up9 = remove(up9, 8)
                    children.append(up9)
            if j == 5:
                if state[0] == "X" and state[2] == "X":
                    up10 = swap(state, 0, 5)
                    up10 = remove(up10, 2)
                    children.append(up10)
            if j == 9:
                if state[2] == "X" and state[5] == "X":
                    up11 = swap(state, 9, 2)
                    up11 = remove(up11, 5)
                    children.append(up11)
            if j == 14:
                if state[5] == "X" and state[9] == "X":
                    up12 = swap(state, 14, 5)
                    up12 = remove(up12, 9)
                    children.append(up12)
        if r == 2:
            if j + 2 == 5:
                if state[j + 1] == "X" and state[j + 2] == "X":
                    left1 = swap(state, j, j + 2)
                    left1 = remove(left1, j + 1)
                    children.append(left1)
            if j - 2 == 3:
                if state[j - 1] == "X" and state[j - 2] == "X":
                    right1 = swap(state, j, j - 2)
                    right1 = remove(right1, j - 1)
                    children.append(right1)
        if r == 3:
            if j + 2 == 8 or j + 2 == 9:
                if state[j + 1] == "X" and state[j + 2] == "X":
                    left2 = swap(state, j, j + 2)
                    left2 = remove(left2, j + 1)
                    children.append(left2)
            if j - 2 == 7 or j - 2 == 6:
                if state[j - 1] == "X" and state[j - 2] == "X":
                    right2 = swap(state, j, j - 2)
                    right2 = remove(right2, j - 1)
                    children.append(right2)
        if r == 4:
            if j + 2 == 12 or j + 2 == 13 or j + 2 == 14:
                if state[j + 1] == "X" and state[j + 2] == "X":
                    left3 = swap(state, j, j + 2)
                    left3 = remove(left3, j + 1)
                    children.append(left3)
            if j - 2 == 12 or j - 2 == 11 or j - 2 == 10:
                if state[j - 1] == "X" and state[j - 2] == "X":
                    right3 = swap(state, j, j - 2)
                    right3 = remove(right3, j - 1)
                    children.append(right3)
    return children


def row(index):
    if index == 0:
        return 0
    elif index < 3:
        return 1
    elif index < 6:
        return 2
    elif index < 10:
        return 3
    elif index < 15:
        return 4


def diagonal_down(row):
    if row == 0:
        return 3, 5
    if row == 1:
        return 5, 7
    if row == 2:
        return 7, 9


def r_diagonal_down(row):
    if row == 0:
        return 1, 2
    if row == 1:
        return 2, 3
    if row == 2:
        return 3, 4


def print_path():
    start = Peg(initial, None, 0)
    fringe = deque()
    fringe.appendleft(start)
    visited = set()
    visited.add(initial)
    while len(fringe) != 0:
        v = fringe.pop()
        if v.get_state() == goal:
            print(v.get_path_length())
            parents = list()
            p = v
            while p is not None:
                parents.append(p)
                p = p.get_parent()
            while parents:
                t = parents.pop()
                print_puzzle(t.get_state())
            return v.get_path_length()
        c = get_children(v.get_state())
        temp = []
        for e in c:
            add = Peg(e, v, v.get_path_length() + 1)
            temp.append(add)
        for a in temp:
            if a.get_state() not in visited:
                fringe.appendleft(a)
                visited.add(a.get_state())


print_path()
