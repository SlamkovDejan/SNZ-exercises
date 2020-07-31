"""
Во науката за анализа на податоци откако ќе биде истрениран модел врз податочно множество базирано на неколку
карактеристики, често се прави експеримент кој се нарекува аблација (отстранување). Целта на овој експеримент
е да се одреди која од карактеристиките има најмногу влијание врз точноста на моделот, а со тоа и која е најклучна
карактеристика - од која најмногу зависи класната припадност на примероците.

За оваа задача во променливата dataset ви е дадено податочно множество кое се однесува на цвеќиња наречени Iris.
Секој ред од множеството се однесува на едно од трите класи на цвеќиња означени со 0, 1 и 2. За секое цвеќе има четири
карактеристики кои се однесуваат на должината и ширината на неговите листови. Ова податочно множество го делите на два
дела: тренирачко множество со првите 80% од редиците и тестирачко множество со останатите 20% од податоците.

Од стандарден влез се чита индексот на една колона од податочното множество во променливата column_ind.
Ваша задача е да направите две дрва на одлука, така што првото дрво на одлука ќе ги користи сите карактеристики од
податочното множество, додека второто дрво на одлука ќе го користи множеството каде што е отстранета колоната со индекс
column_ind. Пресметајте точност со двете дрва и на стандарден излез испечатете ја точноста на двете дрва.
"""

from materials.decision_tree_learning import build_tree, classify, max_classification

dataset = [
    [6.3, 2.9, 5.6, 1.8, 0],
    [6.5, 3.0, 5.8, 2.2, 0],
    [7.6, 3.0, 6.6, 2.1, 0],
    [4.9, 2.5, 4.5, 1.7, 0],
    [7.3, 2.9, 6.3, 1.8, 0],
    [6.7, 2.5, 5.8, 1.8, 0],
    [7.2, 3.6, 6.1, 2.5, 0],
    [6.5, 3.2, 5.1, 2.0, 0],
    [6.4, 2.7, 5.3, 1.9, 0],
    [6.8, 3.0, 5.5, 2.1, 0],
    [5.7, 2.5, 5.0, 2.0, 0],
    [5.8, 2.8, 5.1, 2.4, 0],
    [6.4, 3.2, 5.3, 2.3, 0],
    [6.5, 3.0, 5.5, 1.8, 0],
    [7.7, 3.8, 6.7, 2.2, 0],
    [7.7, 2.6, 6.9, 2.3, 0],
    [6.0, 2.2, 5.0, 1.5, 0],
    [6.9, 3.2, 5.7, 2.3, 0],
    [5.6, 2.8, 4.9, 2.0, 0],
    [7.7, 2.8, 6.7, 2.0, 0],
    [6.3, 2.7, 4.9, 1.8, 0],
    [6.7, 3.3, 5.7, 2.1, 0],
    [7.2, 3.2, 6.0, 1.8, 0],
    [6.2, 2.8, 4.8, 1.8, 0],
    [6.1, 3.0, 4.9, 1.8, 0],
    [6.4, 2.8, 5.6, 2.1, 0],
    [7.2, 3.0, 5.8, 1.6, 0],
    [7.4, 2.8, 6.1, 1.9, 0],
    [7.9, 3.8, 6.4, 2.0, 0],
    [6.4, 2.8, 5.6, 2.2, 0],
    [6.3, 2.8, 5.1, 1.5, 0],
    [6.1, 2.6, 5.6, 1.4, 0],
    [7.7, 3.0, 6.1, 2.3, 0],
    [6.3, 3.4, 5.6, 2.4, 0],
    [5.1, 3.5, 1.4, 0.2, 1],
    [4.9, 3.0, 1.4, 0.2, 1],
    [4.7, 3.2, 1.3, 0.2, 1],
    [4.6, 3.1, 1.5, 0.2, 1],
    [5.0, 3.6, 1.4, 0.2, 1],
    [5.4, 3.9, 1.7, 0.4, 1],
    [4.6, 3.4, 1.4, 0.3, 1],
    [5.0, 3.4, 1.5, 0.2, 1],
    [4.4, 2.9, 1.4, 0.2, 1],
    [4.9, 3.1, 1.5, 0.1, 1],
    [5.4, 3.7, 1.5, 0.2, 1],
    [4.8, 3.4, 1.6, 0.2, 1],
    [4.8, 3.0, 1.4, 0.1, 1],
    [4.3, 3.0, 1.1, 0.1, 1],
    [5.8, 4.0, 1.2, 0.2, 1],
    [5.7, 4.4, 1.5, 0.4, 1],
    [5.4, 3.9, 1.3, 0.4, 1],
    [5.1, 3.5, 1.4, 0.3, 1],
    [5.7, 3.8, 1.7, 0.3, 1],
    [5.1, 3.8, 1.5, 0.3, 1],
    [5.4, 3.4, 1.7, 0.2, 1],
    [5.1, 3.7, 1.5, 0.4, 1],
    [4.6, 3.6, 1.0, 0.2, 1],
    [5.1, 3.3, 1.7, 0.5, 1],
    [4.8, 3.4, 1.9, 0.2, 1],
    [5.0, 3.0, 1.6, 0.2, 1],
    [5.0, 3.4, 1.6, 0.4, 1],
    [5.2, 3.5, 1.5, 0.2, 1],
    [5.2, 3.4, 1.4, 0.2, 1],
    [5.5, 2.3, 4.0, 1.3, 2],
    [6.5, 2.8, 4.6, 1.5, 2],
    [5.7, 2.8, 4.5, 1.3, 2],
    [6.3, 3.3, 4.7, 1.6, 2],
    [4.9, 2.4, 3.3, 1.0, 2],
    [6.6, 2.9, 4.6, 1.3, 2],
    [5.2, 2.7, 3.9, 1.4, 2],
    [5.0, 2.0, 3.5, 1.0, 2],
    [5.9, 3.0, 4.2, 1.5, 2],
    [6.0, 2.2, 4.0, 1.0, 2],
    [6.1, 2.9, 4.7, 1.4, 2],
    [5.6, 2.9, 3.6, 1.3, 2],
    [6.7, 3.1, 4.4, 1.4, 2],
    [5.6, 3.0, 4.5, 1.5, 2],
    [5.8, 2.7, 4.1, 1.0, 2],
    [6.2, 2.2, 4.5, 1.5, 2],
    [5.6, 2.5, 3.9, 1.1, 2],
    [5.9, 3.2, 4.8, 1.8, 2],
    [6.1, 2.8, 4.0, 1.3, 2],
    [6.3, 2.5, 4.9, 1.5, 2],
    [6.1, 2.8, 4.7, 1.2, 2],
    [6.4, 2.9, 4.3, 1.3, 2],
    [6.6, 3.0, 4.4, 1.4, 2],
    [6.8, 2.8, 4.8, 1.4, 2],
    [6.7, 3.0, 5.0, 1.7, 2],
    [6.0, 2.9, 4.5, 1.5, 2],
    [5.7, 2.6, 3.5, 1.0, 2],
    [5.5, 2.4, 3.8, 1.1, 2],
    [5.4, 3.0, 4.5, 1.5, 2],
    [6.0, 3.4, 4.5, 1.6, 2],
    [6.7, 3.1, 4.7, 1.5, 2],
    [6.3, 2.3, 4.4, 1.3, 2],
    [5.6, 3.0, 4.1, 1.3, 2],
    [5.5, 2.5, 4.0, 1.3, 2],
    [5.5, 2.6, 4.4, 1.2, 2],
    [6.1, 3.0, 4.6, 1.4, 2],
    [5.8, 2.6, 4.0, 1.2, 2],
    [5.0, 2.3, 3.3, 1.0, 2],
    [5.6, 2.7, 4.2, 1.3, 2],
    [5.7, 3.0, 4.2, 1.2, 2],
    [5.7, 2.9, 4.2, 1.3, 2],
    [6.2, 2.9, 4.3, 1.3, 2],
    [5.1, 2.5, 3.0, 1.1, 2],
    [5.7, 2.8, 4.1, 1.3, 2],
    [6.4, 3.1, 5.5, 1.8, 0],
    [6.0, 3.0, 4.8, 1.8, 0],
    [6.9, 3.1, 5.4, 2.1, 0],
    [6.8, 3.2, 5.9, 2.3, 0],
    [6.7, 3.3, 5.7, 2.5, 0],
    [6.7, 3.0, 5.2, 2.3, 0],
    [6.3, 2.5, 5.0, 1.9, 0],
    [6.5, 3.0, 5.2, 2.0, 0],
    [6.2, 3.4, 5.4, 2.3, 0],
    [4.7, 3.2, 1.6, 0.2, 1],
    [4.8, 3.1, 1.6, 0.2, 1],
    [5.4, 3.4, 1.5, 0.4, 1],
    [5.2, 4.1, 1.5, 0.1, 1],
    [5.5, 4.2, 1.4, 0.2, 1],
    [4.9, 3.1, 1.5, 0.2, 1],
    [5.0, 3.2, 1.2, 0.2, 1],
    [5.5, 3.5, 1.3, 0.2, 1],
    [4.9, 3.6, 1.4, 0.1, 1],
    [4.4, 3.0, 1.3, 0.2, 1],
    [5.1, 3.4, 1.5, 0.2, 1],
    [5.0, 3.5, 1.3, 0.3, 1],
    [4.5, 2.3, 1.3, 0.3, 1],
    [4.4, 3.2, 1.3, 0.2, 1],
    [5.0, 3.5, 1.6, 0.6, 1],
    [5.9, 3.0, 5.1, 1.8, 0],
    [5.1, 3.8, 1.9, 0.4, 1],
    [4.8, 3.0, 1.4, 0.3, 1],
    [5.1, 3.8, 1.6, 0.2, 1],
    [5.5, 2.4, 3.7, 1.0, 2],
    [5.8, 2.7, 3.9, 1.2, 2],
    [6.0, 2.7, 5.1, 1.6, 2],
    [6.7, 3.1, 5.6, 2.4, 0], # column_ind = 0; new_row = [3.1, 5.6, 2.4, 0]
    [6.9, 3.1, 5.1, 2.3, 0],
    [5.8, 2.7, 5.1, 1.9, 0],
]

if __name__ == "__main__":
    column_ind = int(input())

    # casting
    # int(value-to-cast); float(value-to-cast); str(value-to-cast)
    # we use casting here because slicing requires int indices, but multiplication with 0.8 gives us a decimal number
    eighty = int(len(dataset) * 0.8)

    train = dataset[:eighty]
    test = dataset[eighty:]

    # one way (no list comprehension)
    new_train = []
    for row in train:
        new_row = []
        for col_index in range(len(row)):
            if col_index != column_ind:
                new_row.append(row[col_index])
        new_train.append(new_row)

    # second way (one loop, one list comprehension)
    """new_train = []
    for row in train:
        new_row = [row[col_index] for col_index in range(len(row)) if col_index != column_ind]
        new_train.append(new_row)"""

    # third way (two nested list comprehensions)
    """new_train = [[row[col_index] for col_index in range(len(row)) if col_index != column_ind] for row in train]"""

    # one way (no list comprehension)
    new_test = []
    for row in test:
        new_row = []
        for col_index in range(len(row)):
            if col_index != column_ind:
                new_row.append(row[col_index])
        new_test.append(new_row)

    # second way (one loop, one list comprehension)
    """new_test = []
    for row in test:
        new_row = [row[col_index] for col_index in range(len(row)) if col_index != column_ind]
        new_test.append(new_row)"""

    # third way (two nested list comprehensions)
    """new_test = [[row[col_index] for col_index in range(len(row)) if col_index != column_ind] for row in test]"""

    tree1 = build_tree(train)
    tree2 = build_tree(new_train)

    num_correct_1 = 0
    num_correct_2 = 0

    # one way (with two separate loops)
    for row in test:
        tree_1_pred = max_classification(classify(row, tree1))

        correct_class = row[-1]

        if tree_1_pred == correct_class:
            num_correct_1 = num_correct_1 + 1

    for row in new_test:
        tree_2_pred = max_classification(classify(row, tree2))

        correct_class = row[-1]

        if tree_2_pred == correct_class:
            num_correct_2 = num_correct_2 + 1

    # second way (with one loop, using the zip() function)
    # zip(list1, list2) -> allows for iteration with one loop of two lists with equal lengths
    # ex: for el-in-list1, el-in-list2 in zip(list1, list2)

    """num_correct_1 = 0
    num_correct_2 = 0

    for row, new_row in zip(test, new_test):
        # 'row'' is an element of 'test' list
        # 'new_row' is an element of 'new_test' list
        tree_1_pred = max_classification(classify(row, tree1))
        tree_2_pred = max_classification(classify(new_row, tree2))

        correct_class = row[-1] # it's the same class for the two rows, 'row' and 'new_row'

        if tree_1_pred == correct_class:
            num_correct_1 = num_correct_1 + 1
        if tree_2_pred == correct_class:
            num_correct_2 = num_correct_2 + 1"""

    # 'test' and 'new_test' are the same length, so it doesn't matter which length we take for the division
    total = len(test)

    correctness1 = num_correct_1 / total
    correctness2 = num_correct_2 / total

    print(f'Tochnost so prvoto drvo na odluka: {correctness1}')
    print(f'Tochnost so vtoroto drvo na odluka: {correctness2}')