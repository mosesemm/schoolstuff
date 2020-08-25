import numpy as np
from alternative_assignment_1_p1 import LKPAlgorithm

def create_subsets(all_subsets, subset, current_index, k):

    if(len(subset) == current_index):
        return all_subsets

    for i in range(0, len(all_subsets)):
        if len(all_subsets[i]) < k:
            new_set = all_subsets[i].copy()
            new_set.append(subset[current_index])
            all_subsets.append(new_set)

    create_subsets(all_subsets, subset, current_index+1, k)


def create_subsets_by_size(items_indexes, subset_size, k):
    all_subsets = [[]]
    create_subsets(all_subsets, items_indexes, 0, k)
    return [curr_set for curr_set in all_subsets if len(curr_set) == subset_size]

def create_subsets_with_min_size(items_indexes, min_size, k):
    all_subsets = [[]]
    create_subsets(all_subsets, items_indexes, 0, k)
    return [curr_set for curr_set in all_subsets if len(curr_set) > min_size]

def greater_w(chosen_w, W):
    return np.sum(chosen_w) > W


class PTAS:

    @staticmethod
    def getProfitableValues(values, weights, W, min_subset_size, k):

        N = len(weights)
        all_items_index = [i for i in range(0, N)]

        S = np.array(create_subsets_by_size(all_items_index, min_subset_size, k))

        best_values = []
        best_weights = []
        highest_profit = 0
        for F in S:
            chosen_v = np.take(values, F)
            chosen_w = np.take(weights, F)

            # fill up remaining space
            if not greater_w(chosen_w, W):
                delta_v = np.take(values, list(set(all_items_index) - set(F)))
                delta_w = np.take(weights, list(set(all_items_index) - set(F)))
                sum_weights = np.sum(chosen_w)
                effective_W = W - sum_weights
                kp_index_values = LKPAlgorithm.getProfitableIndexValues(delta_v, delta_w, effective_W)
                profit_F = np.sum(chosen_v) + np.sum(delta_v[kp_index_values == 1])

                if profit_F > highest_profit:
                    highest_profit = profit_F
                    best_liner_index = np.where(kp_index_values == 1)
                    best_values = np.concatenate([np.take(values, F), np.take(delta_v, best_liner_index)[0]])
                    best_weights = np.concatenate([np.take(weights, F), np.take(delta_w, best_liner_index)[0]])

        return best_values, best_weights


print("Polynomial Time Approximation Algorithm (PTAS): ")

values = np.array([2,6,8,7,3,4,6,5,10,9,8,11,12,15,6,8,13,14,15,16,13,14,15,26,13,9,25,26])
weights = np.array([7,3,3,5,4,7,5,4,15,10,17,3,6,11,6,14,4,8,9,10,14,17,9,24,11,17,12,14])
W = 30
min_subset_size = 3
k = 10

best_values, best_weights = list(PTAS.getProfitableValues(values, weights, W, min_subset_size, k))
print("Chosen pairs: {}".format([item for item in zip(best_values, best_weights)]))
print("Resulting profit: {}".format(sum(best_values)))
print("Resulting weight: {}".format(sum(best_weights)))



