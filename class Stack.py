

class Stack:
    def __init__(self, string):
        self.string = list(string)

    def isEmpty(self):
        if len(self.string) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.string.append(element)

    def pop(self):
        if len(self.string) == 0:
            return None
        element = self.string[-1]
        self.string.pop()
        return element

    def peek(self):
        if len(self.string) == 0:
            return None
        element = self.string[-1]
        return element

    def size(self):
        return len(self.string)

def match(open, close):
    openers = "([{"
    closers = ")]}"
    if open in openers:
        op_index = openers.index(open)
    else:
        return None
    status = op_index == closers.index(close)
    return status

def is_balanced(string):
    test_stack = Stack(string)
    index = 0
    balanced = True

    while index < len(string) and balanced:
        element = string[index]
        if element in "([{":
            test_stack.push(element)
        else:
            if test_stack.isEmpty():
                balanced = False
            else:
                last_element = test_stack.pop()
                if not match(last_element, element):
                    balanced = False
        index += 1

    if balanced :
        return "Сбалансировано"
    else:
        return "Несбалансировано"


if __name__ == "__main__":
    '''Пример
    сбалансированных
    последовательностей
    скобок:'''
    test_1 = "(((([{}]))))"
    test_2 = "[([])((([[[]]])))]{()}"
    test_3 = "{{[()]}}"
    '''Несбалансированные
    последовательности:'''

    test_4 = "}{}"
    test_5 = "{{[(])]}}"
    test_6 = "[[{())}]"

    print(is_balanced(test_1))
    print(is_balanced(test_2))
    print(is_balanced(test_3))

    print(is_balanced(test_4))
    print(is_balanced(test_5))
    print(is_balanced(test_6))

