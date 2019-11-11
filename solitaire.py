from pprint import pprint

stacks = [[9, 8, 7, 12, 11, 8, 12],
          [9, 11, 7, 6, 12, 7],
          [10, 13, 9, 14, 13, 10],
          [9, 6, 8, 13, 6, 11],
          [12, 10, 11, 14, 6, 14],
          [10, 13, 7, 7, 8, 14]]

def convert(x):
    try:
        return int(x)
    except:
        if x == 'v':
            return 11
        elif x == 'd':
            return 12
        elif x == 'k':
            return 13
        else:
            raise ValueError(x)

def get_stack_end(stack):
    # Return (moveable, rest)
    if len(stack) == 1:
        return stack, []
    i = 0
    while i < len(stack) - 1:
        bottom      = stack[-1 - i]
        predecessor = stack[-1 - i -1]
        if predecessor != bottom + 1:
            break
        i += 1
    return stack[len(stack) - 1 - i:len(stack)], stack[:len(stack) - 1 - i]

def get_moves(stacks):
    moves = []
    for i, stack in enumerate(stacks):
        moveable, base = get_stack_end(stack)
        if len(moveable) > 0:
            head = moveable[0]
            for j, other_stack in enumerate(stacks):
                if i != j and (len(other_stack) == 0 or other_stack[-1] == head + 1):
                    moves.append((i, moveable, j))
    return moves

def show(stacks):
    for stack in stacks:
        print(' | '.join(str(item).ljust(2, ' ') for item in stack))

def apply_move(stacks, move):
    from_i, section, to_i = move
    stacks[to_i].extend(stacks[from_i][-len(section):])
    stacks[from_i] = stacks[from_i][:-len(section)]
    return stacks

def is_win(stacks):
    for move in get_moves(stacks):
        if len(move[1]) != 0:
            return False
    return True

def test_get_stack_end():
    #print(get_stack_end([9, 8]))
    #print(get_stack_end([10, 8]))
    #pprint(get_moves(stacks))
    for move in get_moves(stacks):
        #show(apply_move(stacks, move))
        #print('-' * 80)
        pass
    active = [stacks]
    while True:
        possible = []
        for state in active:
            for move in get_moves(state):
                next_state = apply_move(state, move)
                if is_win(next_state):
                    show(next_state)
                    return True
                possible.append(next_state)
        active = possible


test_get_stack_end()
