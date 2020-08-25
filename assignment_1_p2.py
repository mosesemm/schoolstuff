
from commons import printable_items, sum_items_v, sum_items_w, KPitem
from assignment_1_p1 import LinearKP



def createF(remainingItems, k, W, minSubsetCount, S = []):
        F = []
        w_F = 0

        if len(remainingItems) > 0:
            for item in remainingItems:
                if item.w + w_F <= W and len(F) <= k:
                    F.append(item)
                    w_F += item.w
                    remainingItems.remove(item)

            if len(F) > minSubsetCount:
                S.append(F)

            createF(remainingItems, k, W, minSubsetCount, S)

        return S

def pack_each_F_into_sack(S, items, W):

    updated_S = []

    for F in S:

        if sum_items_w(F) < W:
            delta_items = [item for item in items if item not in F]
            w_F = sum_items_w(F)
            delta_w = W - w_F
            best_delta_items = LinearKP.getProfitableValues(delta_items, delta_w)
            updated_S.append(F+best_delta_items)
        else:
            updated_S.append(F)


    return updated_S

def highest_valued_set(S):

    best_value = 0
    best_set = []
    for F in S:
        v_F = sum_items_v(F)
        if v_F > best_value:
            best_value = v_F
            best_set = F

    return best_set

class PTAS:

    @staticmethod
    def getProfitableValues(items, k, W, minSubsetCount):
        S = createF(items.copy(), k, W, minSubsetCount, [])
        updated_S = pack_each_F_into_sack(S, items.copy(), W)
        F = highest_valued_set(updated_S)
        return F




if __name__ == "__main__":

    weights = [7, 3, 3, 5, 4, 7, 5, 4, 15, 10, 17, 3, 6, 11, 6, 14, 4, 8, 9, 10, 14, 17, 9, 24, 11, 17, 12, 14]
    values = [2, 6, 8, 7, 3, 4, 6, 5, 10, 9, 8, 11, 12, 15, 6, 8, 13, 14, 15, 16, 13, 14, 15, 26, 13, 9, 25, 26]

    items = [KPitem(item[0], item[1], i) for i, item in enumerate(zip(weights, values))]

    minSubsetCount = 3
    k = 10
    W = 30
    F = PTAS.getProfitableValues(items, k, W, minSubsetCount)

    print("Chosen set: {}".format(printable_items(F)))
    print("Chosen set weight: {}".format(sum_items_w(F)))
    print("Highest profit: {}".format(sum_items_v(F)))

