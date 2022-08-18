import linked_list
from linked_list import *
import random_number_generator
from random_number_generator import *

linkedlist=create_list()
linkedlist.headval=node(33)
e2=node(100)
linkedlist.headval.nextval=e2
e3=node(50)
e2.nextval=e3
linkedlist.insert_head(30)
linkedlist.insert_tail(54)
linkedlist.print_val()


