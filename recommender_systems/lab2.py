from setuptools.command.test import test

ratings = {
    'Lisa Rose': {'Catch Me If You Can': 3.0, 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'The Night Listener': 3.0,
                     'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane': 4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck': 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5,
                         'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5,
                     'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
}

from materials.recommender_systems import get_recommendations, sim_pearson

if __name__ == '__main__':
    test_users = list(input().split(", "))

    # the dataset in recommender systems is represented as a dict
    test = {}
    train = {}

    for user in ratings.keys():
        if user in test_users:
            test[user] = ratings[user]
        else:
            train[user] = ratings[user]

    # first way
    for test_user in test.keys():
        # before we recommend items for a user, first we have to make sure that the user is present in the dataset
        # that is, present in the dataset which we send to the algorithm, in this case the 'train' dataset
        train[test_user] = test[test_user]
        recommendations = get_recommendations(train, test_user, sim_pearson)[:3]
        recommendations = [tup[1] for tup in recommendations]
        # after we're done with the test user we have to extract him from the dataset so it doesn't affect the recommendations of the other test users
        # we ignore the returned result from the '.pop()' function because we don't need it
        train.pop(test_user)

        # 'separator'.join(list/set) - joins the elements from the list/set argument in one string using 'separator'
        # ex: '-'.join([2, 3, 5]) -> "2-3-5"
        print(f"{test_user}: {'; '.join(recommendations)}")

    # second way
    """
    for test_tup in test.items():
        train[test_tup[0]] = test_tup[1]
        recommendations = get_recommendations(train, test_tup[0], sim_pearson)[:3]
        recommendations = [tup[1] for tup in recommendations]
        train.pop(test_tup[0])

        print(f"{test_tup[0]}: {'; '.join(recommendations)}")
    """

    # third way
    """
    for (test_user, reviews) in test.items():
        train[test_user] = reviews
        recommendations = get_recommendations(train, test_user, sim_pearson)[:3]
        recommendations = [tup[1] for tup in recommendations]
        train.pop(test_user)

        print(f"{test_user}: {'; '.join(recommendations)}")
    """