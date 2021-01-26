def match_parentheses(i):

    matches = {('(', ')'), ('{', '}'), ('[', ']')}

    i_len = len(i)

    index = 0
    i_stk = []
    is_balanced = False

    while index < i_len:

        c = i[index]

        if c in '({[':

            is_balanced = False

            i_stk.append(c)

        else:

            if len(i_stk) == 0:
                return False

            top = i_stk.pop()

            if (top, c) not in matches:
                is_balanced = False
            else:
                is_balanced = True

        index += 1

    return is_balanced
