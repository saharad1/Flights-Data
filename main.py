import sys
from data import Data
from statistics import mean, median
from flights import Flights


def main(argv):
    """
    This program answers hw2 as required.
    prints the final output.
    :param argv:
    :return:
    """

    # Objects and variables
    new_data = Data(argv[1])
    statistics_functions = [mean, median]
    letters = {'D', 'A', 'T', 'S', 'C', 'I', 'E', 'N'}
    new_data.select_features(argv[2])
    flight = Flights(new_data.data)
    flight.filter_by_airport_names('Origin_airport', letters)
    features2 = ['Distance', 'Flights', 'Passengers', 'Seats']

    # Print Question 1
    print("Question 1:")
    flight.print_details(features2, statistics_functions)
    flight.compute_empty_seats()
    print()

    # Print Question 2
    print("Question 2:")
    unwanted_flights = flight.count_bad_flights(3000)
    print("Number of unwanted flights: " + str(unwanted_flights))
    if unwanted_flights > 3120:
        separate = "Yes"
    else:
        separate = "No"
    print("Will Mr & Mrs Smith be separated? " + separate)


if __name__ == "__main__":
    main(sys.argv)
