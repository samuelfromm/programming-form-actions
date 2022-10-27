from data_structures import Stack


def test_stack():

    stack = Stack()
    teachers = ("Matias", "Björn", "Lars", "Jon", "Marcus", "Per")

    for teacher in teachers:

        stack.push(teacher)

    assert stack.pop() == "Per"
