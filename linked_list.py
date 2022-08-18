class node:
    def __init__ (self,data,nextval=None):
        self.data=data
        self.nextval=nextval

class create_list:
    
    def __init__(self, headval=None):
        self.headval=headval

    def insert_head(self,value):
        new_node=node(value)
        if self.headval is None:
            self.headval=new_node
            return
        current_node = self.headval
        current_node = current_node.nextval
        current_node.nextval = new_node
        
    def insert_tail(self,value):
        new_node=node(value)
        if self.headval is None:
            self.headval=new_node
            return
        last = self.headval
        while last.nextval is not None:
            last = last.nextval
        last.nextval = new_node
        
    def delete_elem(self,key):
        while self.headval.nextval :
            if self.headval is None:
                return
            if self.headval.data == key :
                current=self.headval
                self.headval=current.next
                current.next=None
            if self.headval is not None:
                self.headval.next = current.next
                
    def print_val(self):
        current_node=self.headval
        while current_node is not None:
            print(current_node.data,"->",end="")
            current_node=current_node.nextval

if __name__ == '__main__' :

    linkedlist=create_list()
    linkedlist.headval=node(33)
    e2=node(100)
    linkedlist.headval.nextval=e2
    e3=node(50)
    e2.nextval=e3
    linkedlist.delete_elem(50)
    linkedlist.insert_tail(200)
    linkedlist.print_val()






            
