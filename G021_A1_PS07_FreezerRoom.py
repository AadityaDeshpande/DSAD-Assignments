from sys import exit
import cProfile
""" 
Reading the Input file inputPS07.txt
Populate transaction_list to create binary tree
Populate actions_list to perform actions on the binary tree
"""
inputFileName: str = "inputPS07.txt"
outputFileName: str = "outputPS07.txt"

# Redirect the print outputs to the file
class FileWriter:
    """ A File writer class """
    file = open(outputFileName, 'a')
    def __init__(self):
        self.file = open(outputFileName, 'a')
    
    def __del__(self):
        self.file.close()

    @classmethod
    def write_in_file(cls, content):
        cls.file.write(content + "\n")

# Reading the Input and process it

try:
    with open(inputFileName, 'r') as infile:
        lines: list = infile.readlines()
        lines: list = [line.strip() for line in lines if line.strip()]
        Employee_transactions_list: list = [int(i) for i in lines if i.isdigit()]
        actions_list: list = [i for i in lines if not i.isdigit()]
except FileNotFoundError as e:
    FileWriter.write_in_file(f"Input file {inputFileName} is not present in the same directory \n{e}")
    exit(0)

# validation for no employees
if not len(Employee_transactions_list):
    FileWriter.write_in_file("Can't create a binary tree without any elements")
    exit(0)

# Construct a binary tree
""" 
Each node represents an employee
attctr represents the number of times employee swipped a card
"""
class EmpNode:
    def __init__(self, EmpId: int):
        """ Parameterised constructor """
        self.EmpID: int = EmpId
        self.attctr: int = 1
        self.left = None
        self.right = None

    def insert(self, EmpId: int):
        """ Insert the element in binary tree """
        if EmpId == self.EmpID:
            # same swipe so increment counter
            self.attctr += 1
        elif EmpId < self.EmpID:
            # insert to the left of tree
            if self.left is None:
                self.left = EmpNode(EmpId)
            else:
                self.left.insert(EmpId)
        elif EmpId > self.EmpID:
            # insert to the right of tree
            if self.right is None:
                self.right = EmpNode(EmpId)
            else:
                self.right.insert(EmpId)

    def get_status(self, Employee_dict: dict = {}, print_tree: bool = True):
        """ Print the elements in tree recrsively and update the list of employees """
        if self.left:
            self.left.get_status(Employee_dict, print_tree)
        if print_tree:
            print("Employee ID:",self.EmpID, ", and attctr value :",self.attctr)
        Employee_dict.update({self.EmpID:self.attctr})
        if self.right:
            self.right.get_status(Employee_dict, print_tree)

def searchEmployee(root: EmpNode, EmpID):
    """ Helper function that will be used for recursive  """
    if root is None:
        FileWriter.write_in_file(f"Employee id {EmpID} did not swipe today.")
        return root
    if root.EmpID == EmpID:
        FileWriter.write_in_file(f"Employee id {root.EmpID} swiped {root.attctr} times today and is currently {'outside' if root.attctr % 2 == 0 else 'inside'} freezer room")
        return root
    if root.EmpID < EmpID:
        return searchEmployee(root.right, EmpID)
    if root.EmpID > EmpID:
        return searchEmployee(root.left, EmpID)

def inFreezer(root: EmpNode):
    # logic to get employees in the freezer
    Employee_status = {}
    root.get_status(Employee_status, False)
    inside_freezer = 0
    for k, v in Employee_status.items():
        if v % 2 != 0:
            inside_freezer += 1
    FileWriter.write_in_file(f"Total number of employees recorded today: {len(Employee_status.keys())} {inside_freezer} employee(s) still inside freezer room")

def checkEmp(root: EmpNode, action: str):
    emp_to_search = action.split(':')[1].strip()
    if emp_to_search.isdigit():
        emp_to_search = int(emp_to_search)
    searchEmployee(root, emp_to_search)

def freqVisit(root: EmpNode, action: str):
    frequency = action.split(':')[1].strip()
    # logic to get employees frequency status
    Employee_status = {}
    root.get_status(Employee_status, False)
    for k, v in Employee_status.items():
        if int(frequency) <= v:
            FileWriter.write_in_file(f"{k}, {v}")

def rangeEmp(root: EmpNode, action: str):
    lower_range = action.split(':')[1].strip()
    upper_range = action.split(':')[2].strip()
    # FileWriter.write_in_file(f"{lower_range}, {upper_range}")
    FileWriter.write_in_file(f"Range: {lower_range} to {upper_range} Employee swipe:")
    # logic to get employees frequency status
    Employee_status = {}
    root.get_status(Employee_status, False)

    for k,v in Employee_status.items():
        if k <= int(upper_range) and k >= int(lower_range):
            FileWriter.write_in_file(f"{k}, {v}, {'out' if v % 2 == 0 else 'in'}")

# Driver code / Main Code
"""
Construct a Tree
create a root node with first value
"""
root = EmpNode(Employee_transactions_list[0])

# Create a binary tree
for EmpID in Employee_transactions_list[1:]:
    root.insert(EmpID)

root.get_status({}, False)

# Finite states to drive the code
for action in actions_list:
    if 'inFreezer' in action:
        inFreezer(root)
    
    if 'checkEmp' in action:
        checkEmp(root, action)
    
    if 'freqVisit' in action:
        freqVisit(root, action)
    
    if 'range' in action:
        rangeEmp(root, action)

# cProfile.run('inFreezer(root)')
# cProfile.run('checkEmp(root, action)')
# cProfile.run('freqVisit(root, action)')
# cProfile.run('rangeEmp(root, action)')