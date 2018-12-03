import matplotlib.pyplot as plt
import numpy as np


class Plotter:

    def print_plot(self, algortihm, data_dictionary, param_no):

        if algortihm == 'astr':
            plt.title("A* algorithm")
        elif algortihm == 'bfs':
            plt.title("BFS algorithm")
        elif algortihm == 'dfs':
            plt.title("DFS algorithm")

        width = 0.1
        averages_dictionary = self.get_average_values_for_parameter(data_dictionary)
        ind = np.arange(1, 8, 1)

        i = 0
        for key, values in averages_dictionary.items():
            plt.bar(ind + i * width, values, width, label=key)
            i += 1

        plt.xlabel('solution length')
        plt.ylabel(self.ylabel_switch(param_no))
        plt.legend(loc='best')
        plt.show()

    def print_general_plot(self, all_data_list, param_no):
        labels = ['bfs', 'dfs', 'astr']
        plt.title("All algorithms")

        width = 0.1
        ind = np.arange(1, 8, 1)
        j = 0

        for algorithm in all_data_list:
            algorithm_values = self.get_average_values_for_depth(algorithm)
            plt.bar(ind + j * width, algorithm_values, width, label=labels[j])
            for i in range(1, 8):
                plt.text(x=i, y=algorithm_values[i-1], s=ind, size=5)
            j += 1

        plt.xlabel('solution length')
        plt.ylabel(self.ylabel_switch(param_no))
        plt.legend(loc='best')
        plt.show()

    @staticmethod
    def ylabel_switch(x):
        return {
            0: "average path length",
            1: "average number of visited states",
            2: "average number of processed states",
            3: "average recursion depth",
            4: "average processing time"
        }.get(x, "")

    def get_average_values_for_parameter(self, data_dictionary):
        values_dictionary = {}
        old_key = ''
        for key, value in data_dictionary.items():
            new_key = key[0:4]
            if old_key != new_key:
                values_dictionary[new_key] = [value]
            else:
                values_dictionary[new_key].append(value)
            old_key = new_key

        return values_dictionary

    def get_average_values_for_depth(self, data_dictionary):
        values_dictionary = {}
        values_list = []
        old_key = ''
        i = 0

        for key, values in data_dictionary.items():
            new_key = key[0:4]
            if old_key != new_key:
                i += 1
            old_key = new_key

        for key, value in data_dictionary.items():
            new_key = key[-1:]
            if values_dictionary.keys().__contains__(new_key):
                values_dictionary[new_key] += value
            else:
                values_dictionary[new_key] = value

        for key, value in values_dictionary.items():
            values_dictionary[key] = value / i
            values_list.append(values_dictionary[key])

        return values_list
