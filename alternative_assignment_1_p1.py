import numpy as np


def sort_by_efficiency_function(values, weights):
    score = np.array([values[i]/weights[i] for i in range(len(weights))])
    return np.argsort(-score)

def selected_items(items, indexes):
    return items[indexes == 1]

class LKPAlgorithm:

    @staticmethod
    def getProfitableIndexValues(values, weights, W):
        N = len(weights)
        sorted_indexes = sort_by_efficiency_function(values, weights)
        added_items_index = np.zeros(N).astype(int)

        sum_items_w = 0
        for i in range(N):
            best_value_i = sorted_indexes[i]
            if sum_items_w + weights[best_value_i] <= W:
                added_items_index[best_value_i] = 1
                sum_items_w += weights[best_value_i]

        return added_items_index


print("Problem 1: Greedy Algorithm")

values = np.array([2,6,8,7,3,4,6,5,10,9,8,11,12,15,6,8,13,14,15,16,13,14,15,26,13,9,25,26])
weights = np.array([7,3,3,5,4,7,5,4,15,10,17,3,6,11,6,14,4,8,9,10,14,17,9,24,11,17,12,14])
W = 30

print("Linear Knapsack: ")
kp_items_indexes = LKPAlgorithm.getProfitableIndexValues(values, weights, W)
print("Chosen pairs: {}".format([item for item in zip(selected_items(values, kp_items_indexes), selected_items(weights, kp_items_indexes))]))
print("Resulting profit: {}".format(np.sum(selected_items(values, kp_items_indexes))))
print("Resulting weight: {}".format(np.sum(selected_items(weights, kp_items_indexes))))


