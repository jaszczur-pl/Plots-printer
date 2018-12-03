import glob


class IOHandler:

    def get_and_sort_stats_files(self, strategy):

        dict = {}
        list_with_depth = []

        directory = ''
        if strategy == 'astr':
            param_list = ['manh', 'hamm']
        else:
            param_list = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']

        for param in param_list:
            for i in range(1, 8):
                pattern = '*_0%s_*_%s_%s_stats.txt' % (i, strategy, param)
                files = glob.glob(directory + pattern)
                list_with_depth.append(files)

                if files.__len__() >= 1:
                    dict[param+str(i)] = list_with_depth.pop()

        return dict

    def read_input_files(self, strategy_files):

        dict_values = {}

        for key, value in strategy_files.items():
            list_values = []
            for file_path in value:
                input_file = open(file_path)
                values = input_file.read().splitlines()
                values = [float(i) for i in values]
                list_values.append(values)
            dict_values[key] = list_values

        return dict_values






























































































