class node:
    """ a new node which has a link to the next value in memory and carries a data value,
        the data is hererogeneous(can be ,int ,bool ,str ,char,etc) since it is stored in a python array .
    """
    def __init__ (self,data,nextval=None):
        self.data=data
        self.nextval=nextval

class create_list:
    # this is a singly linked list with CRUD methods. forgive the massive docstrings, i wanted them to be detailed for easy learning

    def __init__(self, headval=None):
        """
            this method will always store the value of the headval since it will be initialized when the
            list is created
        """
        self.headval=headval

    def insert_head(self,value):
        """
            we create a new node and tell the new node to point to the current head node as the next value,
            then we make the new node the new head value.
            --runs in O(n)constant time--
        """
        new_node=node(value)
        if self.headval is None:
            self.headval=new_node
            return
        new_node.nextval = self.headval
        self.headval=new_node
        print('inserted head',value)

    def insert_tail(self,value):
        """
            here we have to find the next value after the headval until we find the last element which lacks,
            a nextval. when we get to the end we point the last node to our new node.
            --runs in O(n) linear time--.

        """
        new_node=node(value)
        if self.headval is None:
            self.headval=new_node
            return
        last = self.headval
        while last.nextval is not None:
            last = last.nextval
        last.nextval = new_node
        print('inserted tail',value)

    def delete_elem(self,key):
        """
            to delete an element this method takes in self(the list instance) & the element as the key, we loop through the whole array,
            to find the key but if the key is the headval.data(first node) get the next value after it and make it headval,
            then disconnect the old headval by pointing its nextval to None.
            if its not the headval loop through but when you find the key, get the previous node to point--> to the
            key`s next value then disconect the key/node by poinitng it to None.
            --runs in linear time when looping but constant time when deleting--
        """
        index = self.headval
        while index.nextval :
            if self.headval is None:
                return
            prev = index
            index = prev.nextval
            last = index.nextval
            if prev.data == key:
                print('\n removed value :',prev.data)
                former_head = prev
                self.headval = former_head.nextval
                former_head.nextval=None
            elif index.data == key:
                print('\n removed value :',index.data)
                prev.nextval = last
                index.nextval = None

    def search_elem(self,key):
        """
            this search method was implemented a little late in the program,so to find an element in the linked list
            we get the key(the element) from input and start from the head to tail while keeping count of the index if the key is found
            Ding ! Ding ! Ding! we return the index else none.
        """
        index = 0
        current = self.headval
        while current.nextval :
            if current.data == key :
                print(f'\n********key value \"{key}\" found at  index :{index}********')
                return current.data
            else:
                current = current.nextval
                index+=1
                if current.nextval == None and current.data != key:
                    print(f'\n*********key value \"{key}\" not found in list**********')
                    return False
        return index

    def insert_at_index(self,data,key):
        """
           we will traverse the list keeping track of our index position if the next position matches the key(index) we will
           do  an insert at that position. remember its easy, we jus need to change the pointers.
        """
        index = 0
        current = self.headval
        new_node=node(data)
        while current.nextval :
            if current == self.headval and index == key :
                self.insert_head(data)
            if current.nextval == None and index == key :
                self.insert_tail(data)
            if index+1 == key :
                nextval = current.nextval
                current.nextval=new_node
                new_node.nextval=nextval
                print(f'\n************Inserted {data} at index {key}*******')
                return True
            else:
                current = current.nextval
                index+=1
        return False

    def delete_at_index(self,key):
        """
           we will traverse the list keeping track of our index position if the next position matches the key we will
           do  a deletion at that position.
        """
        index = 0
        current = self.headval
        while current.nextval :
            if current == self.headval and index == key :
                self.delete_elem(data)

            if index+1 == key :
                midval = current.nextval
                nextval = midval.nextval
                current.nextval = nextval
                midval.nextval = None
                print(f'\n************deleted {midval.data} at index {key}*******')
                return True
            else:
                current = current.nextval
                index+=1


        return False



    def print_val(self):
        current_node=self.headval
        while current_node is not None:
            print(current_node.data,end="->")
            current_node=current_node.nextval
        print('\n')


"""
    this is for easy reffereal when importing since the code is long you can use this info when calling the class methods
                from linked_list import create_list()
                linkedlist=create_list()
                linkedlist.insert_head(data)
                linkedlist.insert_tail(data)
                linkedlist.search_elem(data)
                linkedlist.delete_elem(data)
                linkedlist.insert_at_index(data,index)
                linkedlist.delete_at_index(index)
                linkedlist.print_val()

"""





if __name__ == '__main__' :

    linkedlist=create_list()
    linkedlist.headval=node(33)
    e2=node(100)
    linkedlist.headval.nextval=e2
    e3=node(50)
    e2.nextval=e3
    linkedlist.print_val()
    linkedlist.delete_elem(100)
    linkedlist.print_val()
    print('..............................')
    linkedlist.insert_tail(200)
    linkedlist.print_val()
    print('..............................')
    linkedlist.insert_head(170)
    linkedlist.print_val()
    print('..............................')
    linkedlist.insert_head(70)
    linkedlist.print_val()
    print('..............................')
    linkedlist.insert_tail(300)
    linkedlist.print_val()
    print('..............................')
    linkedlist.search_elem(50)
    linkedlist.print_val()
    print('..............................')
    linkedlist.insert_at_index(155,4)
    linkedlist.print_val()
    print('..............................')
    linkedlist.delete_at_index(3)
    linkedlist.print_val()
    print('..............................')
    linkedlist.delete_elem(33)
    linkedlist.print_val()
    print('..............................')
