import numpy as np

def Print_ID(StudentID):
    print(f'student ID = {StudentID}')

def calculate_sum(array):
    return array.sum()

if __name__ == '__main__':
    Print_ID("3456")
    calculate_sum(np.array([1,2,3]))

