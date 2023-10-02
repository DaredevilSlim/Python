#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Your function should return a multiline string of unique lowercase letters in alphabetical order. The characters
# should be placed in a form of hollow rhombus (diamond), along its edges, starting from the top vertex.
# For this purpose you are given three values (for their constraints see Preconditions):
# side - number of letters in each side of the rhombus;
# length - total number of letters you should use;
# cw - clockwise flag, which shows in what direction the letters must go (if True - letters should be placed in
# clockwise direction).
# If it's not enough length to complete the form, complement it with "*". The rhombus should not have white spaces at
# the right. Here is an example with arguments and expected result:
# Input: Three arguments: side as integer (int), length as integer (int) and clockwise flag as logic (bool).
# Output: Multiline string (str).
# Preconditions:
# 26 >= length >= 0;
# side > 1;
# (side-1)*4 >= length.
def hollow_diamond(side: int, length: int, cw: bool) -> str:
    li = [''] * (side * 2 - 1)
    a = 1
    size = side * 2 + (side - 2) * 2
    b = 'abcdefghijklmnopqrstuvwxyz'[:length]
    b = b + '*' * (size - length) if length < size else b
    c, d = (size - 1, 0) if cw else (0, size - 1)
    e = 1
    for i in range(len(li)):
        f = ' ' * (side - a)
        g = b[c] + ' ' * e + b[d] + '\n'
        if i < side - 1:
            li[i] = f + (b[d if cw else c] + '\n' if i == 0 else g)
        else:
            li[i] = f + (b[side * 2 - 2] if i == (side * 2 - 2) else g)
        a = a + 1 if i < side - 1 else a - 1
        e = e + 0 if i == 0 else e + 2 if i < side - 1 else e - 2
        c, d = (c - 1 if i != 0 else c, d + 1) if cw else (c + 1, d - 1 if i != 0 else d)
    return ''.join(li)


print(hollow_diamond(4, 1, False))  # '   a\n  * *\n *   *\n*     *\n *   *\n  * *\n   *'
print(hollow_diamond(3, 8, True))  # "  a\n h b\ng   c\n f d\n  e"
print(hollow_diamond(3, 6, False))  # "  a\n b *\nc   *\n d f\n  e"
print((
    hollow_diamond(4, 10, False))  # "   a\n  b *\n c   *\nd     j\n e   i\n  f h\n   g"
)
print((
    hollow_diamond(5, 16, True)
   )  # "    a\n   p b\n  o   c\n n     d\nm       e\n l     f\n  k   g\n   j h\n    i"
)
print((
    hollow_diamond(5, 14, False)
   )  # "    a\n   b *\n  c   *\n d     n\ne       m\n f     l\n  g   k\n   h j\n    i"
)
