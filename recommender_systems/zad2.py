"""
Во речникот ratings се чуваат информации за оцени на филмови. Клуч е името на корисникот и вредност е речник чиј клуч е
филмот, а вредност е оцената која корисникот ја дал за филмот. За името на корисникот прочитано од стандарден влез да
се препорача филм на следниот начин. Прво се прави препорака според најслични корисници користејќи евклидово растојание
и пирсонов коефициент на корелација како метрика за сличност. Доколку со двете метрики за сличност се добие истиот филм,
 тогаш се печати тој филм. Во спротивно, се прави препорака според најслични филмови. Доколку препорачаниот филм според
 најслични филмови е еднаков со некој од препорачаните филмови според најслични корисници
 (препорачаниот филм со евклидово растојание и препорачаниот филм со пирсонов коефициент на корелација),
 тогаш се печати тој филм. Во спротивно се печати филмот кој има највисока вредност за препорака.
"""

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

from materials.recommender_systems import get_recommendations, sim_pearson, sim_distance, get_recommendations_item_based, transform_prefs

if __name__ == '__main__':
    user_name = input()

    euclid_recommendation = get_recommendations(ratings, user_name, sim_distance)[0]
    pearson_recommendation = get_recommendations(ratings, user_name, sim_pearson)[0]

    if euclid_recommendation[1] == pearson_recommendation[1]:
        print(euclid_recommendation[1])
    else:
        item_based = get_recommendations_item_based(transform_prefs(ratings), user_name)[0]
        if item_based[1] == euclid_recommendation[1] or item_based[1] == pearson_recommendation[1]:
            print(item_based[1])
        else:
            # first way
            tuple_list = [euclid_recommendation, pearson_recommendation, item_based]
            max_tuple = max(tuple_list, key=lambda x: x[0])
            # second way
            """
            tuple_list = [euclid_recommendation, pearson_recommendation, item_based]
            sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)
            max_tuple = sorted_list[0]
            """
            # third way
            """
            if euclid_recommendation[0] > pearson_recommendation[0] and euclid_recommendation[0] > item_based[0]:
                max_tuple = euclid_recommendation
            elif pearson_recommendation[0] > euclid_recommendation[0] and pearson_recommendation[0] > item_based[0]:
                max_tuple = pearson_recommendation
            else:
                max_tuple = item_based
            """
            print(max_tuple[1])