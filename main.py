from board import Board
import numpy as np
import time
from agent import *

def main():

    for m in [10, 20, 30, 40, 50]:
        print(f'Solving Problems with shuffle of: {m}')

        TOTAL_SEEDS = 10

        # BF_Report(m, TOTAL_SEEDS)
        MT_Report(m, TOTAL_SEEDS)
        CB_Report(m, TOTAL_SEEDS)
        NA_Report(m, TOTAL_SEEDS)
        


def NA_Report(m, total_problems):
        # Parameters for NA heuristic report:
        # % of problems solved
        # Average CPU time per problem size
        # Average solution length
        # Generated search nodes from all problems.
        
        problem_solve_percentage = 0
        average_cpu_time = 0
        average_solution_length = 0
        total_search_nodes_generated = 0
        problems_solved_count = 0
        
        
        print("NA Search")
        for seed in range(10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)

            # print(f'Board Initial State:\n{board.state}\n')
            

            start =  time.process_time()
            solution, search_nodes_generated = a_star_search(board, NA)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                # print(f'Solution Generated: {solution}')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated
                problems_solved_count += 1
                average_solution_length += len(solution)
            else:
                # print(f'No solution found.')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated


        problem_solve_percentage = (int) (problems_solved_count/total_problems * 100)
        average_cpu_time /= total_problems
        if (problems_solved_count > 0):
            average_solution_length /= problems_solved_count

        print(f'\nReport for {total_problems} problems with a shuffle size of {m} using NA:\n')
        print(f'Percentage of Problems Solved: {problem_solve_percentage}%')
        print(f'Number of search nodes generated: {total_search_nodes_generated}')
        print(f'Average CPU time per problem: {average_cpu_time} seconds')
        print(f'Average Solution Length: {average_solution_length}\n')

def CB_Report(m, total_problems):
        # Parameters for CB heuristic report:
        # % of problems solved
        # Average CPU time per problem size
        # Average solution length
        # Generated search nodes from all problems.
        
        problem_solve_percentage = 0
        average_cpu_time = 0
        average_solution_length = 0
        total_search_nodes_generated = 0
        problems_solved_count = 0
        
        
        print("CB Search")
        for seed in range(10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)

            # print(f'Board Initial State:\n{board.state}\n')
            

            start =  time.process_time()
            solution, search_nodes_generated = a_star_search(board, CB)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                # print(f'Solution Generated: {solution}')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated
                problems_solved_count += 1
                average_solution_length += len(solution)
            else:
                # print(f'No solution found.')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated


        problem_solve_percentage = (int) (problems_solved_count/total_problems * 100)
        average_cpu_time /= total_problems
        if (problems_solved_count > 0):
            average_solution_length /= problems_solved_count

        print(f'\nReport for {total_problems} problems with a shuffle size of {m} using CB:\n')
        print(f'Percentage of Problems Solved: {problem_solve_percentage}%')
        print(f'Number of search nodes generated: {total_search_nodes_generated}')
        print(f'Average CPU time per problem: {average_cpu_time} seconds')
        print(f'Average Solution Length: {average_solution_length}\n')

def MT_Report(m, total_problems):
        # Parameters for MT heuristic report:
        # % of problems solved
        # Average CPU time per problem size
        # Average solution length
        # Generated search nodes from all problems.
        
        problem_solve_percentage = 0
        average_cpu_time = 0
        average_solution_length = 0
        total_search_nodes_generated = 0
        problems_solved_count = 0
        
        
        print("MT Search")
        for seed in range(10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)

            # print(f'Board Initial State:\n{board.state}\n')
            

            start =  time.process_time()
            solution, search_nodes_generated = a_star_search(board, MT)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                # print(f'Solution Generated: {solution}')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated
                problems_solved_count += 1
                average_solution_length += len(solution)
            else:
                # print(f'No solution found.')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated


        problem_solve_percentage = (int) (problems_solved_count/total_problems * 100)
        average_cpu_time /= total_problems
        if (problems_solved_count > 0):
            average_solution_length /= problems_solved_count

        print(f'\nReport for {total_problems} problems with a shuffle size of {m} using MT:\n')
        print(f'Percentage of Problems Solved: {problem_solve_percentage}%')
        print(f'Number of search nodes generated: {total_search_nodes_generated}')
        print(f'Average CPU time per problem: {average_cpu_time} seconds')
        print(f'Average Solution Length: {average_solution_length}\n')

def BF_Report(m, total_problems):
        # Parameters for BF report:
        # % of problems solved
        # Average CPU time per problem size
        # Average solution length
        # Generated search nodes from all problems.
        
        
        problem_solve_percentage = 0
        average_cpu_time = 0
        average_solution_length = 0
        total_search_nodes_generated = 0
        problems_solved_count = 0
        
        
        print("BF Search")
        for seed in range(10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)

            # print(f'Board Initial State:\n{board.state}\n')
            

            start =  time.process_time()
            solution, search_nodes_generated = a_star_search(board, BF)
            end =  time.process_time()
            solution_cpu_time = end-start
            if (board.check_solution(solution)):
                # print(f'Solution Generated: {solution}')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated
                problems_solved_count += 1
                average_solution_length += len(solution)
            else:
                # print(f'No solution found.')
                average_cpu_time += solution_cpu_time
                total_search_nodes_generated += search_nodes_generated


        problem_solve_percentage = (int) (problems_solved_count/total_problems * 100)
        average_cpu_time /= total_problems
        if (problems_solved_count > 0):
            average_solution_length /= problems_solved_count

        print(f'\nReport for {total_problems} problems with a shuffle size of {m} using BFS:\n')
        print(f'Percentage of Problems Solved: {problem_solve_percentage}%')
        print(f'Number of search nodes generated: {total_search_nodes_generated}')
        print(f'Average CPU time per problem: {average_cpu_time} seconds')
        print(f'Average Solution Length: {average_solution_length}\n')

if __name__ == "__main__":
    main()
