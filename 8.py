#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Programming Stack in Python
class LIFO:
    # Initializing Node/Pack structure for Stack
    def __init__(self, value):
        #self.head = Node('head')    # initializing default value
        self.data = value   # data part
        self.next = None    # next's address part
        self.len = 0        # initializing default size

    # Checks for empty Stack
    def isEmpty(self):
        return self.len == 0

    # Returns Peek(Top most) element of the Stack
    def top(self):
        # Exception handling for empty Stack
        if self.isEmpty():  
            raise Exception('Stack is Empty! :(')
        return self.next.data

    # For insertion of elements into the Stack
    def push(self, newData):
        newNode = LIFO(newData)     # inserting value to data part
        newNode.next = self.next    # inserting address of top element to address part

        # After Linking new Node, top elements and size of Stack changes
        # so updating value of top element as last inserted Node,
        self.next = newNode
        # and size of Stack is incremented.
        self.len += 1
    
    # For deletion of elements from the Stack
    def pop(self):
        # Exception handling for empty Stack
        if self.isEmpty():
            raise Exception('Stack is Empty! :(')
        # Poping begins removal of elements from Peek(Top most) element of the Stack;
        # Which ultimately states that the code maintains the Stack Protocol.
        pop = self.next

        # After Unkinking new Node, top elements and size of Stack changes
        # so updating value of top element as predecessor Node of the Deleted Node,
        self.next = self.next.next
        # and size of Stack is decremented.
        self.len -= 1
        return pop.data

    # Printing Stack as String
    def __str__(self):
        show = ''
        peek = self.next
        while peek:     # loops untill peek become None
            show += str(peek.data) + ' | '
            peek = peek.next
        return show[::-1]
    
if __name__ == "__main__":
    print('\t#STACK')
    stack = LIFO('head')
    def consoleOut():
        if f'{stack}' == '':
            print('\tStack is Empty!,\n\tTry to push element.\n')
        else:
            print(f'\tStack:{stack}')
    x = 5
    while x != 0:
        x = int(input('1) Print Stack\n2) Push Element\n3) Pop Element\n4) Print Peek\n0) Exit\t:'))
        
        if x == 1:
            consoleOut()

        if x == 2:
            ele = input('\tEnter element: ')
            stack.push(ele)
            print('\tPushed:',ele)
            
        if x == 3:
            ele = int(input('\tEnter Pop index: '))
            while ele != 0:
                print('\tPopped:',stack.pop())
                ele -= 1

        if x == 4:
            print('\tPeek:',stack.top())