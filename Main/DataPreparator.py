class DataPreparator:

    def prepare_data(self, dict_values, value_no):

        averages_dictionary = {}

        for key, values in dict_values.items():
            cnt = 0
            sum = 0
            for value in values:
                if value[0] == -1:
                    continue
                else:
                    sum += value[value_no]
                    cnt += 1
            averages_dictionary[key] = float(sum/cnt)

        return averages_dictionary
