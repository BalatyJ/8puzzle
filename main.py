from board import Board
import numpy as np
import time
from agent import *

def main():

    for m in [10, 20, 30, 40, 50]:
        print(f'Solving Problems with shuffle of: {m}')
            
        # Parameters for report:
        # % of problems solved
        # Average CPU time per problem size
        # Average solution length
        # Generated search nodes from all problems.
        
        problem_solve_percentage = 0
        average_cpu_time = 0
        average_solution_length = 0
        total_search_nodes_generated = 0
        problems_solved_count = 0
        
        for seed in range(10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)

            print(f'Board Initial State:\n{board.state}\n')
            
            print("BF Search")
            start =  time.process_time()
            solution = a_star_search(board, BF)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                print(f'Solution Time: {solution_cpu_time}\n')
            else:
                print(f'No solution found.\n')


            print("MT Search")
            start =  time.process_time()  
            solution = a_star_search(board, MT)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                print(f'Solution Time: {solution_cpu_time}\n')
            else:
                print(f'No solution found.\n')

            print("CB Search")
            start =  time.process_time()
            solution = a_star_search(board, CB)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                print(f'Solution Time: {solution_cpu_time}\n')
            else:
                print(f'No solution found.\n')

            print("NA Search")
            start =  time.process_time()
            solution = a_star_search(board, NA)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                print(f'Solution Time: {solution_cpu_time}\n')
            else:
                print(f'No solution found.\n')


        # print(f'\nReport for 10 problems with a shuffle size of {m} using BF:\n')
        # print(f'Percentage of Problems Solved: {problem_solve_percentage}%')
        # print(f'Number of search nodes generated: {total_search_nodes_generated}')
        # print(f'Average CPU time per problem: {average_cpu_time}')
        # print(f'Average Solution Length: {average_solution_length}\n')
        


    # for m in [10, 20, 30, 40, 50]:
    #     print(f'Solving Problems with shuffle of: {m}')
    #     for seed in range(10):
    #         # Sets the seed of the problem so all students solve the same problems
    #         board = Board(m, seed)

    #         # Parameters for report:
    #         # % of problems solved
    #         # Average CPU time per problem size
    #         # Average solution length

    #         problem_solve_percentage = 0

    #         print(f'Initial State (Root Node):\n{board}\n')
    #         start =  time.process_time()  
    #         solution = a_star_search(board, BF)
    #         print(f'Solution to problem using BFS: {a_star_search(board, BF)}')
    #         end =  time.process_time()
    #         solution_cpu_time = end-start
    #         print(f'Solution time:\n{solution_cpu_time}\n\n\n')





    #         # start =  time.process_time()  
    #         # print(f'Solution to problem using MT: {a_star_search(board, MT)}')
    #         # end =  time.process_time()
    #         # solution_cpu_time = end-start
    #         # print(f'Solution time:\n{solution_cpu_time}\n\n\n')
            

    #         # start =  time.process_time()  
    #         # print(f'Solution to problem using CB: {a_star_search(board, CB)}')
    #         # end =  time.process_time()
    #         # solution_cpu_time = end-start
    #         # print(f'Solution time:\n{solution_cpu_time}\n\n\n')

    # for m in [10, 20, 30, 40, 50]:
    #     print(f'Solving Problems with shuffle of: {m}')
    #     for seed in range(10):
    #         # Sets the seed of the problem so all students solve the same problems
    #         board = Board(m, seed)

    #         # Parameters for report:
    #         # % of problems solved
    #         # Average CPU time per problem size
    #         # Average solution length

    #         problem_solve_percentage = 0

    #         print(f'Initial State (Root Node):\n{board}\n')
    #         start =  time.process_time()  
    #         solution = a_star_search(board, BF)
    #         print(f'Solution to problem using BFS: {a_star_search(board, BF)}')
    #         end =  time.process_time()
    #         solution_cpu_time = end-start
    #         print(f'Solution time:\n{solution_cpu_time}\n\n\n')





    #         # start =  time.process_time()  
    #         # print(f'Solution to problem using MT: {a_star_search(board, MT)}')
    #         # end =  time.process_time()
    #         # solution_cpu_time = end-start
    #         # print(f'Solution time:\n{solution_cpu_time}\n\n\n')
            

    #         # start =  time.process_time()  
    #         # print(f'Solution to problem using CB: {a_star_search(board, CB)}')
    #         # end =  time.process_time()
    #         # solution_cpu_time = end-start
    #         # print(f'Solution time:\n{solution_cpu_time}\n\n\n')
            

if __name__ == "__main__":
    main()
