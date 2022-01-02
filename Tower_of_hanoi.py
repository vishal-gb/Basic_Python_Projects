DISKS = int(input("Enter number of disks:"))
bars = ( [], [], [] )
moves = 0

def show():
    for i in range(len(bars)):
        print(bars[i])
    print("moves %d" % moves)
    print("------------")
    time.sleep(0.1)
    print()

def step_move(_from, _to):
    global moves
    moves += 1
    bars[_to].append(bars[_from].pop())
    show()


def move_disks(_from, _to, _num):

    if _num == 0:
        return

    tmp = 3 - _from - _to # temporary storage bar
    move_disks(_from, tmp, _num - 1)
    step_move(_from, _to)
    move_disks(tmp, _to, _num - 1)


if __name__ == '__main__':
    bars[0].extend(list(range(DISKS))[::-1])
    show()

    move_disks(0, 2, DISKS)
