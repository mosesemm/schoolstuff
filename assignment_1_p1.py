
from commons import printable_items, sum_items_v, KPitem


class LinearKP:

    @staticmethod
    def getProfitableValues(candidate_values, capacity):
        candidate_values.sort()

        added_values = []
        added_weights = 0
        for item in candidate_values:
            current_weight = int(item.w)

            if added_weights + current_weight <= capacity:
                added_weights += current_weight
                added_values.append(item)

            if added_weights == capacity:
                break

        return added_values

if __name__ == "__main__":

    weights = [7, 3, 3, 5, 4, 7, 5, 4, 15, 10, 17, 3, 6, 11, 6, 14, 4, 8, 9, 10, 14, 17, 9, 24, 11, 17, 12, 14]
    values = [2, 6, 8, 7, 3, 4, 6, 5, 10, 9, 8, 11, 12, 15, 6, 8, 13, 14, 15, 16, 13, 14, 15, 26, 13, 9, 25, 26]
    candidate_values = [KPitem(item[0], item[1], i) for i, item in enumerate(zip(weights, values))]

    capacity = 30
    profitable_values = LinearKP.getProfitableValues(candidate_values, capacity)
    print("Chosen items: {}".format(printable_items(profitable_values)))
    print("Highest profit: {}".format(sum_items_v(profitable_values)))
