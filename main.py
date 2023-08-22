from board import Board
import time
from agent import *
import matplotlib.pyplot as plt


def main():

    TOTAL_SEEDS = 10

    for m in [10, 20, 30, 40, 50]:
        print('BF Search: Shuffle Size {m}')
        report(m, BF)
        print('MT Search: Shuffle Size {m}')
        report(m, MT)
        print('CB Search: Shuffle Size {m}')
        report(m, CB)
        print('NA Search: Shuffle Size {m}')
        report(m, NA)


def report(m, heuristic):
    for seed in range(10):
        # Sets the seed of the problem so all students solve the same problems
        board = Board(m, seed)

        start = time.process_time()
        solution = a_star_search(board, heuristic)
        end = time.process_time()
        solution_cpu_time = end-start

        if (board.check_solution(solution)):
            print(f'Solution Generated: {solution}')
        else:
            print(f'A* timed out (max nodes reached).')

        print(f'CPU Time: {solution_cpu_time}\n')


if __name__ == "__main__":
    main()
