import pandas as pd

data_f = pd.read_csv("C:\\Users\\Riya\\Downloads\\archive\\groceries - groceries.csv")

print(data_f.head(2))
data_f.shape

list_of_transactions = []

for i in range(0, 50):
    list_of_transactions.append([str(data_f.values[i, j]) for j in range(0, 20)])

list_of_transactions[0]

from apyori import apriori

rules = apriori(list_of_transactions, min_support=0.003, min_confidence=0.3, min_lift=3, min_length=2)


results = list(rules)


print(results[0])


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))


resultsinDataFrame = pd.DataFrame(inspect(results),
                                  columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
print(resultsinDataFrame.head(2))
print(resultsinDataFrame.nlargest(n=3, columns='Lift'))
