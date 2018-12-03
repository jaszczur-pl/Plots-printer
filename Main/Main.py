#!/usr/bin/env python3

from IOHandler import IOHandler
from Plotter import Plotter
from DataPreparator import DataPreparator


def main():
    io_handler = IOHandler()
    plotter = Plotter()
    preparator = DataPreparator()

    bfs_files = io_handler.get_and_sort_stats_files('bfs')
    dfs_files = io_handler.get_and_sort_stats_files('dfs')
    astr_files = io_handler.get_and_sort_stats_files('astr')

    bfs_values = io_handler.read_input_files(bfs_files)
    dfs_values = io_handler.read_input_files(dfs_files)
    astr_values = io_handler.read_input_files(astr_files)

    bfs_avg_path_len = preparator.prepare_data(bfs_values, 0)
    bfs_avg_visited_states = preparator.prepare_data(bfs_values, 1)
    bfs_avg_processed_states = preparator.prepare_data(bfs_values, 2)
    bfs_avg_recursion_depth = preparator.prepare_data(bfs_values, 3)
    bfs_avg_time = preparator.prepare_data(bfs_values, 4)

    dfs_avg_path_len = preparator.prepare_data(dfs_values, 0)
    dfs_avg_visited_states = preparator.prepare_data(dfs_values, 1)
    dfs_avg_processed_states = preparator.prepare_data(dfs_values, 2)
    dfs_avg_recursion_depth = preparator.prepare_data(dfs_values, 3)
    dfs_avg_time = preparator.prepare_data(dfs_values, 4)

    astr_avg_path_len = preparator.prepare_data(astr_values, 0)
    astr_avg_visited_states = preparator.prepare_data(astr_values, 1)
    astr_avg_processed_states = preparator.prepare_data(astr_values, 2)
    astr_avg_recursion_depth = preparator.prepare_data(astr_values, 3)
    astr_avg_time = preparator.prepare_data(astr_values, 4)

    # print(bfs_files)
    # print(bfs_values)
    # print(bfs_avg_path_len)
    # print(bfs_avg_time)
    # print('---')
    # print(dfs_files)
    # print(dfs_values)
    # print('---')
    # print(astr_files)
    # print(astr_values)

    # plotter.print_plot('bfs', bfs_avg_path_len, 0)
    # plotter.print_plot('bfs', bfs_avg_visited_states, 1)
    # plotter.print_plot('bfs', bfs_avg_processed_states, 2)
    # plotter.print_plot('bfs', bfs_avg_recursion_depth, 3)
    # plotter.print_plot('bfs', bfs_avg_time, 4)
    #
    # plotter.print_plot('dfs', dfs_avg_path_len, 0)
    # plotter.print_plot('dfs', dfs_avg_visited_states, 1)
    # plotter.print_plot('dfs', dfs_avg_processed_states, 2)
    # plotter.print_plot('dfs', dfs_avg_recursion_depth, 3)
    # plotter.print_plot('dfs', dfs_avg_time, 4)
    #
    # plotter.print_plot('astr', astr_avg_path_len, 0)
    # plotter.print_plot('astr', astr_avg_visited_states, 1)
    # plotter.print_plot('astr', astr_avg_processed_states, 2)
    # plotter.print_plot('astr', astr_avg_recursion_depth, 3)
    # plotter.print_plot('astr', astr_avg_time, 4)

    plotter.print_general_plot([bfs_avg_path_len, dfs_avg_path_len, astr_avg_path_len], 0)
    plotter.print_general_plot([bfs_avg_visited_states, dfs_avg_visited_states, astr_avg_visited_states], 1)
    plotter.print_general_plot([bfs_avg_processed_states, dfs_avg_processed_states, astr_avg_processed_states], 2)
    plotter.print_general_plot([bfs_avg_recursion_depth, dfs_avg_recursion_depth, astr_avg_recursion_depth], 3)
    plotter.print_general_plot([bfs_avg_time, dfs_avg_time, astr_avg_time], 4)

if __name__ == '__main__':
    main()
