#!/usr/bin/env python
# -*- coding: utf-8 -*


def verify(genuine_id, cells, threshold):
    match = any([v for v in cells if v >= threshold])
    decision = {
        match and genuine_id: 'AC',
        match and not genuine_id: 'FA',
        not match and genuine_id: 'FR',
        not (match or genuine_id): 'RC'
    }
    return decision[True]



similarity_matrix = [
        [[347, 301, 359], [5, 505, 334], [3, 4, 290], [2, 3, 3]],
        [[344, 274, 308], [7, 275, 334], [5, 7, 326], [3, 6, 3]],
        [[4, 9, 3], [270, 6, 3], [254, 292, 9], [268, 194, 283]],
        [[3, 8, 3], [264, 8, 3], [318, 341, 9], [325, 297, 322]]
    ]

genuine_population = 4
impostor_population = 12
fmrs = []
fnmrs = []

thresholds = [x for x in range(250,355)][::5]
for t in thresholds:
    error_set = {'FA': 0, 'FR': 0}
    for r_index, row in enumerate(similarity_matrix):
        for c_index, cells in enumerate(row):
            v = verify(r_index == c_index, cells, t)
            if v in error_set:
                error_set[v] += 1

    fmr = error_set['FA'] / impostor_population
    fnmr = error_set['FR'] / genuine_population
    fmrs.append(fmr)
    fnmrs.append(fnmr)

