#!/usr/python
""" How to add two numbers """
import re


class Tree:
    """A tree with a root value and a list of branches"""

    def __init__(self, question):
        self.data = "<q>" + question + "</q>"
        self.step_idx = 1

    def add(self, data):
        """Add a branch to the tree"""
        self.data += f"<{self.step_idx}>" + data + f"</{self.step_idx}>"
        self.step_idx += 1

    def answer(self, data):
        """Add an answer to the tree"""
        self.data += "<a>" + data + "</a>"

    def __repr__(self):
        return self.data


def solve_addition(question: str) -> str:
    """
    Solve an addition problem.
    """
    a, b = re.findall(r"\d+", question)

    # zero pad the numbers
    a = a.zfill(len(b))
    b = b.zfill(len(a))

    # apply the addition algorithm
    result = [str(int(a[i]) + int(b[i])).zfill(2) for i in range(len(a))]
    result_1 = result.copy()

    # convert the intermediate result to final result
    for i in range(len(result) - 1, 0, -1):
        n = result[i]
        m = result[i - 1]

        m = int(m) + int(n[0])
        m = str(m).zfill(2)
        n = n[1].zfill(2)

        result[i] = n
        result[i - 1] = m

    # combine the result into single number
    answer = "".join([str(int(x)) for x in result])

    # convert the result to a tree structure
    result_tree = Tree(question)
    result_tree.add(",".join(result_1))
    result_tree.add(",".join(result))
    result_tree.add(answer)
    result_tree.answer(answer)
    return str(result_tree)


if __name__ == "__main__":
    # <q>1239 + 4569 = </q><1>05,07,09,18</1><2>05,08,00,08</2><3>5808</3><a>5808</a>
    print(solve_addition("1239 + 4569 = "))
