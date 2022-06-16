from sys import exit

# Reading the Input file inputPS07.txt
# Populate transaction_list to create binary tree
# Populate actions_list to perform actions on the binary tree
inputFileName: str = "inputPS07.txt"

try:
    with open(inputFileName, 'r') as infile:
        lines: list = infile.readlines()
        lines: list = [line.strip() for line in lines if line.strip()]
        transactions_list: list = [i for i in lines if i.isdigit()]
        actions_list: list = [i for i in lines if not i.isdigit()]
except FileNotFoundError as e:
    print(f"Input file {inputFileName} is not present in the same directory \n{e}")
    exit(0)

print(transactions_list)
print(actions_list)

# Construct a binary tree
# Each node represents an employee
# attctr represents the number of times employee swipped a card
class EmpNode:
    def __init__(self, EmpId: int):
        self.EmpID: int = EmpId
        self.attctr: int = 1
        self.left = None
        self.right = None

def construct_tree(transactions_list):
    if not len(transactions_list):
        print("No transactions found, can't create binary tree")
        exit(0)
    
    root = EmpNode(transactions_list[0])
    head = root
    for i in transactions_list[1:]:
        while True:
            if root.left is None:
                root.left = EmpNode(i)
                break
            elif root.right is None:
                root.right = EmpNode(i)
                break
            


    



# Driver code
construct_tree(transactions_list)