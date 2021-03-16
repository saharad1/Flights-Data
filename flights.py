from statistics import mean


class Flights:
    def __init__(self, data):
        self.data = data

    def filter_by_airport_names(self, airports, letters):
        """
        This function gets a specific feature and a set of letters and accordingly deletes the airport names that
        begin with any of the letters in the input set, and the fitting values for the specific index.
        :param airports: Is a string for a key in the dictionary(The data set)
        :param letters: is a set of letters that the names of the airport shouldn't begin with.
        :return:
        """
        airport_list = [i for i in self.data[airports]]
        delete = {i for i in self.data[airports] if not i.startswith(tuple(letters))}
        not_relevant_index = []
        for index, value in enumerate(airport_list):
            if value in delete:
                not_relevant_index.append(index)
        for i in reversed(range(len(airport_list))):
            if i in not_relevant_index:
                for keys in self.data.keys():
                    del self.data[keys][i]

    def print_details(self, features, statistic_functions):
        """
        Prints the required details.
        :param features: the features that we would like to print.
        :param statistic_functions: a list of functions for statistical analysis.
        :return:
        """
        for key in features:
            print(key + ": " + str(statistic_functions[0](self.data[key])) + ", " + str(statistic_functions[1](
                self.data[key])))

    def compute_empty_seats(self, ):
        """
        This function adds a new key to the dictionary, and by a formula given -
        (number of seats available minus - passengers)
        calculates the values of the list.
        :return:
        """
        empty_seats = []
        self.data.update({'Empty_seats': empty_seats})
        for seats, passengers in zip(self.data['Seats'], self.data['Passengers']):
            empty_s = seats - passengers
            self.data['Empty_seats'].append(empty_s)

    def count_bad_flights(self, num):
        """
        A bad flight is defined as a flight of the mean of the empty seats minus the empty seats per flight.
        And then the function counts how may bad flights are there in the data set.
        :param num: Is the minimum number for a bad flight.
        :return:
        """
        u = mean(self.data['Empty_seats'])
        bad_flights = 0
        for empty_s in self.data['Empty_seats']:
            check = u - empty_s
            if check < 0:
                check = -1 * check
            if check > num:
                bad_flights += 1
        return bad_flights
