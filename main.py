from linked_list import LinkedList

sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("Thy Sushi Prep Steps:")
sushi_preparation.print_list()

sushi_preparation.insert_after_value("prepare", "serve")
print('\nAdded "serve" after prepare:')
sushi_preparation.print_list()

sushi_preparation.remove_value("roll")
print('\nremoved "roll":')
sushi_preparation.print_list()

sushi_preparation.remove_value("assemble")
print('\nremoved beginning step:')
sushi_preparation.print_list()

