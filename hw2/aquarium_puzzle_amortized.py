from constraint import *
import numpy as np

def check_gravity(a,b) :
    return b >= a 

# assume max block size is string
def get_equal_blocks(row,max_block_size,max_block_size_digit) : 
    equal_block_variables = []
    curr = row[0]
    temp = [curr]
    
    curr_len = len(curr)
    
    for i in range(1,len(row)):
    
        temp_element = row[i]
        temp_element_len = len(temp_element)
        take_last_cur =int('-' + str(curr_len-2))
        take_last_temp = int('-' + str(temp_element_len-2))
        
        if curr[take_last_cur:] == temp_element[take_last_temp:]:
            temp.append(temp_element)
        else :
            if len(temp) > 1 :
                equal_block_variables.append(temp)
            curr = temp_element
            temp = [curr]


    if len(temp) > 1 : 
        equal_block_variables.append(temp)
    #print("same adjacent elements: ", equal_block_variables)
    return equal_block_variables

        

def solve_using_CSP(puzzle,row_values,column_values,max_block_size,max_block_size_digit):

    problem = Problem() # import it from constraint
    x_range = len(puzzle)
    y_range = len(puzzle[0])
    domain = [0,1]


    # add variable --- variable,domain
    # variables contain ((i,j),puzzle[i,j])

    variables = []
    variable_2D = []
    for i in range(x_range):
        temp = []
        for j in range(y_range):
            variables.append(str(i)+str(j)+str(puzzle[i][j]))
            temp.append(str(i)+str(j)+str(puzzle[i][j]))
        variable_2D.append(temp)
    
    
    
    for var in variables:
        problem.addVariable(var,domain)

    # add constraints


    # first constraint -> The water level of a block should be the same across its full width
    
    
    



    for i in range(len(row_values)):
        problem.addConstraint(ExactSumConstraint(row_values[i]),variable_2D[i])
    
    '''
        # Get Kth Column of Matrix 
        # using list comprehension 
        res = [sub[K] for sub in test_list] 
    '''


    column_list = []
    for i in range(len(variable_2D[0])) :
        column_list.append([sub[i] for sub in variable_2D])


    
    for column in column_list :
        equal_adjacent = get_equal_blocks(column,max_block_size,max_block_size_digit)
        for block in equal_adjacent:
            curr = block[0]
            for i in range(1,len(block)):
                problem.addConstraint(FunctionConstraint(check_gravity), [curr, block[i]])
                curr = block[i]
    
                
    for i in range(len(column_values)) : 
        problem.addConstraint(ExactSumConstraint(column_values[i]),[sub[i] for sub in variable_2D])


    
    for row in variable_2D :
        equal_adjacent = get_equal_blocks(row,max_block_size,max_block_size_digit)
        if len(equal_adjacent) != 0 :
            for i in range(len(equal_adjacent)):
                problem.addConstraint(AllEqualConstraint(),variables = equal_adjacent[i])
    
    
    print(problem.getSolution())
    
def main():
    
    aquarium_puzzle =  [[ '1' , '3' , '5' , '5' , '5' , '5' ],
                        [ '1' , '3' , '1' , '1' , '1' , '5' ],
                        [ '1' , '1' , '1' , '6' , '6' , '5' ],
                        [ '1' , '1' , '1' , '6' , '5' , '5' ],
                        [ '2' , '1' , '4' , '6' , '5' , '5' ],
                        [ '2' , '1' , '4' , '6' , '5' , '5' ]]
    row_values = [1,1,2,4,5,5]
    column_values = [3,5,1,4,3,2]



    aquarium_puzzle_10 = [
    ['1','1','1','1','1','2','2','2','2','5'],
    ['3','3','4','1','1','1','1','6','6','5'],
    ['3','3','4','4','4','4','6','6','6','5'],
    ['7','3','3','9','4','4','6','5','5','5'],
    ['7','7','3','9','9','6','6','5','5','5'],
    ['7','7','9','9','9','6','5','5','5','13'],
    ['7','9','9','10','10','6','6','13','13','13'],
    ['7','7','8','8','10','14','13','13','11','11'],
    ['7','7','8','10','10','14','13','13','11','12'],
    ['8','8','8','8','10','10','10','10','11','12']
    ]

    row_values_10 = [4,4,4,4,4,4,4,3,6,6]
    column_values_10 = [3,5,5,3,3,8,5,4,4,3]
    
    
    np_puzzle =  np.array(aquarium_puzzle).astype(np.int)
    max_block_size = str(np.max(np_puzzle))
    #print(max_block_size)
    max_block_size_digit = str(len(max_block_size))
    #print(max_block_size_digit)

    solve_using_CSP(aquarium_puzzle,row_values,column_values,max_block_size,max_block_size_digit)



if __name__ == '__main__' : 
    main()