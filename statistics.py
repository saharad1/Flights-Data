def sum_list(values):
    final_sum = 0
    for x in values:
        final_sum += x
    return final_sum


def mean(values):
    final_mean = float(sum_list(values)) / len(values)
    return final_mean


def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)

    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        result = sorted_list[center_index]
    return result
