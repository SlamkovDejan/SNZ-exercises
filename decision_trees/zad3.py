"""
Изградете 2 дрва на одлука. Едното дрво на одлука ќе ја користи првата половина од податочното множество, а другото дрво,
втората половина. Притоа, од првичното податочно множество за тренирање отстранете ги редиците чии што индекси
ги содржи листата test_indices и од тие податочни редици креирајте го тестирачкото множество.
Потоа, пресметајте ја точноста на двете дрва на одлука со користење на тестирачкото множество.
Доколку двете дрва имаат иста точност да се испринта "Drvata imaat ista tochnost",
а во спротивно потребно да е да се испринта "Drvoto i e podobro od drvoto j".

Точност на класификатор се пресметува како:

точност = број на точно предвидени примероци / вкупен број на примероци
"""

from materials.decision_tree_learning import build_tree, classify, max_classification

data = [
    [6.3, 2.9, 5.6, 1.8, 'I. virginica'],
    [6.5, 3.0, 5.8, 2.2, 'I. virginica'],
    [7.6, 3.0, 6.6, 2.1, 'I. virginica'],
    [4.9, 2.5, 4.5, 1.7, 'I. virginica'],
    [7.3, 2.9, 6.3, 1.8, 'I. virginica'],
    [6.7, 2.5, 5.8, 1.8, 'I. virginica'],
    [7.2, 3.6, 6.1, 2.5, 'I. virginica'],
    [6.5, 3.2, 5.1, 2.0, 'I. virginica'],
    [6.4, 2.7, 5.3, 1.9, 'I. virginica'],
    [6.8, 3.0, 5.5, 2.1, 'I. virginica'],
    [5.7, 2.5, 5.0, 2.0, 'I. virginica'],
    [5.8, 2.8, 5.1, 2.4, 'I. virginica'],
    [6.4, 3.2, 5.3, 2.3, 'I. virginica'],
    [6.5, 3.0, 5.5, 1.8, 'I. virginica'],
    [7.7, 3.8, 6.7, 2.2, 'I. virginica'],
    [7.7, 2.8, 6.7, 2.0, 'I. virginica'],
    [6.3, 2.7, 4.9, 1.8, 'I. virginica'],
    [6.7, 3.3, 5.7, 2.1, 'I. virginica'],
    [7.2, 3.2, 6.0, 1.8, 'I. virginica'],
    [6.2, 2.8, 4.8, 1.8, 'I. virginica'],
    [6.1, 3.0, 4.9, 1.8, 'I. virginica'],
    [6.4, 2.8, 5.6, 2.1, 'I. virginica'],
    [7.2, 3.0, 5.8, 1.6, 'I. virginica'],
    [7.4, 2.8, 6.1, 1.9, 'I. virginica'],
    [7.9, 3.8, 6.4, 2.0, 'I. virginica'],
    [6.4, 2.8, 5.6, 2.2, 'I. virginica'],
    [6.3, 2.8, 5.1, 1.5, 'I. virginica'],
    [6.1, 2.6, 5.6, 1.4, 'I. virginica'],
    [7.7, 3.0, 6.1, 2.3, 'I. virginica'],
    [6.3, 3.4, 5.6, 2.4, 'I. virginica'],
    [5.1, 3.5, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.0, 1.4, 0.2, 'I. setosa'],
    [4.7, 3.2, 1.3, 0.2, 'I. setosa'],
    [4.6, 3.1, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.6, 1.4, 0.2, 'I. setosa'],
    [5.4, 3.9, 1.7, 0.4, 'I. setosa'],
    [4.6, 3.4, 1.4, 0.3, 'I. setosa'],
    [5.0, 3.4, 1.5, 0.2, 'I. setosa'],
    [4.4, 2.9, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.1, 1.5, 0.1, 'I. setosa'],
    [5.4, 3.7, 1.5, 0.2, 'I. setosa'],
    [4.8, 3.4, 1.6, 0.2, 'I. setosa'],
    [4.8, 3.0, 1.4, 0.1, 'I. setosa'],
    [4.3, 3.0, 1.1, 0.1, 'I. setosa'],
    [5.8, 4.0, 1.2, 0.2, 'I. setosa'],
    [5.1, 3.8, 1.5, 0.3, 'I. setosa'],
    [5.4, 3.4, 1.7, 0.2, 'I. setosa'],
    [5.1, 3.7, 1.5, 0.4, 'I. setosa'],
    [4.6, 3.6, 1.0, 0.2, 'I. setosa'],
    [5.1, 3.3, 1.7, 0.5, 'I. setosa'],
    [4.8, 3.4, 1.9, 0.2, 'I. setosa'],
    [5.0, 3.0, 1.6, 0.2, 'I. setosa'],
    [5.0, 3.4, 1.6, 0.4, 'I. setosa'],
    [5.2, 3.5, 1.5, 0.2, 'I. setosa'],
    [5.2, 3.4, 1.4, 0.2, 'I. setosa'],
    [5.5, 2.3, 4.0, 1.3, 'I. versicolor'],
    [6.5, 2.8, 4.6, 1.5, 'I. versicolor'],
    [5.7, 2.8, 4.5, 1.3, 'I. versicolor'],
    [6.3, 3.3, 4.7, 1.6, 'I. versicolor'],
    [4.9, 2.4, 3.3, 1.0, 'I. versicolor'],
    [6.6, 2.9, 4.6, 1.3, 'I. versicolor'],
    [5.2, 2.7, 3.9, 1.4, 'I. versicolor'],
    [5.0, 2.0, 3.5, 1.0, 'I. versicolor'],
    [5.9, 3.0, 4.2, 1.5, 'I. versicolor'],
    [6.0, 2.2, 4.0, 1.0, 'I. versicolor'],
    [6.1, 2.9, 4.7, 1.4, 'I. versicolor'],
    [5.6, 2.9, 3.6, 1.3, 'I. versicolor'],
    [6.7, 3.1, 4.4, 1.4, 'I. versicolor'],
    [6.6, 3.0, 4.4, 1.4, 'I. versicolor'],
    [6.8, 2.8, 4.8, 1.4, 'I. versicolor'],
    [6.7, 3.0, 5.0, 1.7, 'I. versicolor'],
    [6.0, 2.9, 4.5, 1.5, 'I. versicolor'],
    [5.7, 2.6, 3.5, 1.0, 'I. versicolor'],
    [5.5, 2.4, 3.8, 1.1, 'I. versicolor'],
    [5.5, 2.4, 3.7, 1.0, 'I. versicolor'],
    [5.8, 2.7, 3.9, 1.2, 'I. versicolor'],
    [6.0, 2.7, 5.1, 1.6, 'I. versicolor'],
    [5.4, 3.0, 4.5, 1.5, 'I. versicolor'],
    [6.0, 3.4, 4.5, 1.6, 'I. versicolor'],
    [6.7, 3.1, 4.7, 1.5, 'I. versicolor'],
    [6.3, 2.3, 4.4, 1.3, 'I. versicolor'],
    [5.6, 3.0, 4.1, 1.3, 'I. versicolor'],
    [5.5, 2.5, 4.0, 1.3, 'I. versicolor'],
    [5.5, 2.6, 4.4, 1.2, 'I. versicolor'],
    [6.1, 3.0, 4.6, 1.4, 'I. versicolor'],
    [5.8, 2.6, 4.0, 1.2, 'I. versicolor'],
    [5.0, 2.3, 3.3, 1.0, 'I. versicolor'],
    [5.6, 2.7, 4.2, 1.3, 'I. versicolor'],
    [5.7, 3.0, 4.2, 1.2, 'I. versicolor'],
    [5.7, 2.9, 4.2, 1.3, 'I. versicolor'],
    [6.2, 2.9, 4.3, 1.3, 'I. versicolor'],
    [5.1, 2.5, 3.0, 1.1, 'I. versicolor'],
    [5.7, 2.8, 4.1, 1.3, 'I. versicolor'],
    [6.4, 3.1, 5.5, 1.8, 'I. virginica'],
    [6.0, 3.0, 4.8, 1.8, 'I. virginica'],
    [6.9, 3.1, 5.4, 2.1, 'I. virginica'],
    [6.7, 3.1, 5.6, 2.4, 'I. virginica'],
    [6.9, 3.1, 5.1, 2.3, 'I. virginica'],
    [5.8, 2.7, 5.1, 1.9, 'I. virginica'],
    [6.8, 3.2, 5.9, 2.3, 'I. virginica'],
    [6.7, 3.3, 5.7, 2.5, 'I. virginica'],
    [6.7, 3.0, 5.2, 2.3, 'I. virginica'],
    [6.3, 2.5, 5.0, 1.9, 'I. virginica'],
    [6.5, 3.0, 5.2, 2.0, 'I. virginica'],
    [6.2, 3.4, 5.4, 2.3, 'I. virginica'],
    [4.7, 3.2, 1.6, 0.2, 'I. setosa'],
    [4.8, 3.1, 1.6, 0.2, 'I. setosa'],
    [5.4, 3.4, 1.5, 0.4, 'I. setosa'],
    [5.2, 4.1, 1.5, 0.1, 'I. setosa'],
    [5.5, 4.2, 1.4, 0.2, 'I. setosa'],
    [4.9, 3.1, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.2, 1.2, 0.2, 'I. setosa'],
    [5.5, 3.5, 1.3, 0.2, 'I. setosa'],
    [4.9, 3.6, 1.4, 0.1, 'I. setosa'],
    [4.4, 3.0, 1.3, 0.2, 'I. setosa'],
    [5.1, 3.4, 1.5, 0.2, 'I. setosa'],
    [5.0, 3.5, 1.3, 0.3, 'I. setosa'],
    [4.5, 2.3, 1.3, 0.3, 'I. setosa'],
    [4.4, 3.2, 1.3, 0.2, 'I. setosa'],
    [5.0, 3.5, 1.6, 0.6, 'I. setosa'],
    [5.1, 3.8, 1.9, 0.4, 'I. setosa'],
    [4.8, 3.0, 1.4, 0.3, 'I. setosa'],
    [5.1, 3.8, 1.6, 0.2, 'I. setosa'],
    [5.9, 3.0, 5.1, 1.8, 'I. virginica'],
    [7.7, 2.6, 6.9, 2.3, 'I. virginica'],
    [6.0, 2.2, 5.0, 1.5, 'I. virginica'],
    [6.9, 3.2, 5.7, 2.3, 'I. virginica'],
    [5.6, 2.8, 4.9, 2.0, 'I. virginica'],
    [5.7, 4.4, 1.5, 0.4, 'I. setosa'],
    [5.4, 3.9, 1.3, 0.4, 'I. setosa'],
    [5.1, 3.5, 1.4, 0.3, 'I. setosa'],
    [5.7, 3.8, 1.7, 0.3, 'I. setosa'],
    [5.6, 3.0, 4.5, 1.5, 'I. versicolor'],
    [5.8, 2.7, 4.1, 1.0, 'I. versicolor'],
    [6.2, 2.2, 4.5, 1.5, 'I. versicolor'],
    [5.6, 2.5, 3.9, 1.1, 'I. versicolor'],
    [5.9, 3.2, 4.8, 1.8, 'I. versicolor'],
    [6.1, 2.8, 4.0, 1.3, 'I. versicolor'],
    [6.3, 2.5, 4.9, 1.5, 'I. versicolor'],
    [6.1, 2.8, 4.7, 1.2, 'I. versicolor'],
    [6.4, 2.9, 4.3, 1.3, 'I. versicolor']]

if __name__ == "__main__":
    test_indices = list(map(int, input().split(', ')))

    # more efficient way -> only one iteration
    test_data = []
    train_data = []
    # we use a for loop for iteration of lists/sets in Python
    # the regular for loop in python lets us iterate the elements of the list, one by one:
    # for item in list -> element by element
    # in this case, we want to iterate the indices of the list, that is indices from 0 to len(list) - 1
    # for those purposes, in Python we use the range() function
    # range(startInclusive, endExclusive) -> returns a "list" of numbers from startInclusive to endExclusive - 1
    # ex: range(0, 5) -> [0, 1, 2, 3, 4]
    # later we use that "list" and iterate it's elements in a regular for loop
    # if we don't specify startInclusive, Python sets startInclusive to 0
    # so this: range(len(train_data)) is equivalent to this: range(0, len(train_data))
    for i in range(len(data)):
        # operator 'in' -> checks if a list contains a certain element
        if i in test_indices:
            test_data.append(data[i])
        else:
            train_data.append(data[i])

    # in Java: for(int i=0; i<list.length; i++) list[i]

    # less efficient (two iterations), but more fancier :) (with list comprehension)
    # test_data = [data[index] for index in range(len(data)) if index in test_indices]
    # train_data = [data[index] for index in range(len(data)) if index not in test_indices]

    half = len(train_data) // 2

    tr_data_1 = train_data[:half]
    tr_data_2 = train_data[half:]

    tree1 = build_tree(tr_data_1)
    tree2 = build_tree(tr_data_2)

    num_correct_1 = 0
    num_correct_2 = 0

    for row in test_data:
        tree_1_pred = max_classification(classify(row, tree1))
        tree_2_pred = max_classification(classify(row, tree2))

        correct_class = row[-1]

        if tree_1_pred == correct_class:
            num_correct_1 = num_correct_1 + 1

        if tree_2_pred == correct_class:
            num_correct_2 = num_correct_2 + 1

    total = len(test_data)

    correctness1 = num_correct_1 / total
    correctness2 = num_correct_2 / total

    print(f'Tochnost na drvoto 1: {correctness1}')
    print(f'Tochnost na drvoto 2: {correctness2}')

    if correctness1 == correctness2:
        print('Drvata imaat ista tochnost')
    elif correctness1 > correctness2:
        print('Drvoto 1 e podobro od drvoto 2')
    else:
        print('Drvoto 2 e podobro od drvoto 1')
