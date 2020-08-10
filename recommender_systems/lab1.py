movie_reviews = {
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

from materials.recommender_systems import sim_pearson, sim_distance, transform_prefs

def tabela_na_slichni_korisnici(reviews: dict):
    slicnosti = {}

    for user in reviews.keys():
        # we first must initialize an empty dict at 'slicnosti[user]'. If we don't initialize an empty dict
        # later at 'slicnosti[user][other]' will throw an exception because it will not know what 'slicnosti[user]' is
        slicnosti[user] = {}
        for other in reviews.keys():
            if user == other: continue
            sim_euc = sim_distance(reviews, user, other)
            sim_pear = sim_pearson(reviews, user, other)

            # first way
            inv = transform_prefs(reviews)
            common_movies = [movie for movie in inv.keys() if user in inv[movie].keys() and other in inv[movie].keys()]
            num_common_movies = len(common_movies)
            # second way
            """
            inv = transform_prefs(reviews)
            num_common_movies = 0
            for movie in inv.keys():
                if user in inv[movie].keys() and other in inv[movie].keys():
                    num_common_movies = num_common_movies + 1
            """
            # third way
            """
            num_common_movies = 0
            for movie in reviews[user].keys():
                if movie in reviews[other].keys():
                    num_common_movies = num_common_movies + 1
            """
            tup = (round(sim_euc, 3), round(sim_pear, 3), num_common_movies)
            slicnosti[user][other] = tup

    return slicnosti


if __name__ == "__main__":
    korisnik1 = input()
    korisnik2 = input()

    tabela = tabela_na_slichni_korisnici(movie_reviews)
    print(tabela[korisnik1][korisnik2])