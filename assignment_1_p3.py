
import numpy as np
from fake_assignment import linearKnapSack


def findSubsets(allSubsets, subset, currentIndex, k):
    if (len(subset) == currentIndex):
        return allSubsets

    newSet = []
    for i in range(0, len(allSubsets)):
        if (len(allSubsets[i]) < k):
            newSet = allSubsets[i].copy()
            newSet.append(subset[currentIndex])
            allSubsets.append(newSet)

    findSubsets(allSubsets, subset, currentIndex + 1, k)


# Find all subsets of a specific size
def findAllSubsetsSpecificSize(array, subsetSize, k):
    allSubsets = [[]]
    findSubsets(allSubsets, array, 0, k)
    returnSet = []
    for sets in allSubsets:
        if (len(sets) == subsetSize):
            returnSet.append(sets)
    return returnSet


def sampleKfromN(selectedNumbers, k, N):

    delta_selectedNumbers = np.delete(range(N), selectedNumbers)
    nextRandomNumbers = len(delta_selectedNumbers) if len(delta_selectedNumbers) < k else k
    return np.random.choice(delta_selectedNumbers, nextRandomNumbers, replace=False)


def index_by_efficiency_function(list_pairs, p, w):
    efficiency_criteria = np.array([])
    for pair in list_pairs:
        p_ij = p[pair[0]][pair[1]]
        w_i = w[pair[0]]
        w_j = w[pair[1]]
        efficiency = p_ij/(w_i + w_j)
        efficiency_criteria = np.append(efficiency_criteria, efficiency)
    return np.argsort(-efficiency_criteria)

def alreadySelected(candidate_pair, already_chosen_pairs):
    return candidate_pair[0] in already_chosen_pairs or candidate_pair[1] in already_chosen_pairs


def greater_w(chosen_w, W):
    return np.sum(chosen_w) > W


def QKPAlgorithm(k, N, rand_seed, v, w, W, p):
    np.random.seed(rand_seed)
    chosen_i =[]
    sum_weight = 0
    sum_value = 0
    index_set = [i for i in range(0,15)]

    max_iterations = 1000
    count_iterations = 0

    while count_iterations < max_iterations :
        count_iterations += 1
        random_index = sampleKfromN(chosen_i, k, N)

        candidate_pair = findAllSubsetsSpecificSize(random_index, 2, k)
        efficiency_i = index_by_efficiency_function(candidate_pair, p, w)

        current_largest_pair = candidate_pair[efficiency_i[0]]
        pairs_i_1 = current_largest_pair[0]
        pairs_i_2 = current_largest_pair[1]
        w_i = w[pairs_i_1]
        w_j = w[pairs_i_2]

        if sum_weight + w_i + w_j <= W:
            if alreadySelected(candidate_pair, chosen_i):
                continue
            else:
                chosen_i.append(pairs_i_1)
                chosen_i.append(pairs_i_2)
                delta_v = np.copy(v)
                delta_w = np.copy(w)
                np.put(delta_v, current_largest_pair, 0)
                sum_weight += w_i + w_j
                sum_value += v[pairs_i_1]+v[pairs_i_2]
                W = W - sum_weight

    selectedV = np.take(v, chosen_i)
    selectedW = np.take(w, chosen_i)

    print("Selected w: ", selectedW)



    kp_items_indexes = linearKnapSack(delta_v, delta_w, len(delta_v), W)

    chosen_kp_indexes = np.where(kp_items_indexes == 1)[0]
    all_indexes = np.concatenate((chosen_kp_indexes, chosen_i))

    all_pairs = findAllSubsetsSpecificSize(all_indexes, 2, N)

    single_item_profit = np.sum(np.concatenate([np.take(v, chosen_i), delta_v[kp_items_indexes == 1]]))
    total_profit = single_item_profit

    for i in range(len(all_pairs)):
        current_pair = all_pairs[i]
        total_profit += p[current_pair[0]][current_pair[1]]

    print("Chosen values:", np.concatenate([np.take(v, chosen_i), delta_v[kp_items_indexes == 1]]))

    print("Chosen weights: ", np.concatenate([np.take(w, chosen_i),delta_w[kp_items_indexes == 1]]))
    print("Total Weight: ", np.sum(np.concatenate([np.take(w, chosen_i),delta_w[kp_items_indexes == 1]])))
    print("Total Profit - Single Values:", single_item_profit)
    print("Total Profit - (Including P_ij):", total_profit)


v = np.array([7, 6, 13,16, 5, 10, 9, 23, 18, 12, 9, 22, 17, 32, 8])
w = np.array([13, 14, 14, 15, 15, 9, 26, 24, 13, 11, 9, 12, 25, 12, 26])
W = 50
p = np.array([7	,12	,7	,6	,13	,8	,11	,7	,15	,23	,14	,15	,17	,9	,15, 12	,6	,15	,13	,10	,15	,9	,10	,8	,17	,11	,13	,12	,16	,15, 7,15,
              13	,11	,16	,6	,8	,14	,13	,4	,14	,8	,15	,9	,16,6	,13	,11	,16	,10	,13	,14	,14	,17	,15	,14	,6	,24	,13	, 4,13	,10	,16
                 ,10	,5	,9	,7	,25	,12	,6	,6	,16	,10	,15	,14,8	,15	,6	,13	,9	,10	,2	,13	,12	,16	,9	,11	,23	,10	,21,11	,9	,8
                 ,14	,7	,2	,9	,8	,18	,4	,13	,14	,14	,17	,15,7	,10	,14	,14	,25	,13	,8	,23	,9	,16	,12	,3	,14	,14	,27,15	,8	,13	,
              17	,12	,12	,18	,9	,18	,15	,16	,13	,14	,7	,17,23	,17	,4	,15	,6	,16	,4	,16	,15	,12	,28	,5	,19	,6	,18,14	,11	,14	,14	,
              6	,9	,13	,12	,16	,28	,9	,13	,4	,13	,16,15	,13	,8	,6	,16	,11	,14	,3	,13	,5	,13	,22	,11	,19	,13,17	,12	,15	,24	,10	,23	,
              14	,14	,14	,19	,4	,11	,17	,15	,12,9	,16	,9	,13	,15	,10	,17	,14	,7	,6	,13	,19	,15	,32	,16,15	,15	,16	,4	,14	,21	,15	,
              27	,17	,18	,16	,13	,12	,16	, 8])
p = p.reshape(15,15)
k = 7
N = 15
randomSeed = 7

print("Problem 2 - Quadratic Knapsack Problem ")
QKPAlgorithm(k,N,randomSeed,v,w,W,p)







