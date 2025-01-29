#!/usr/bin/env python
# -*- coding: utf-8 -*
from pprint import pprint
from matplotlib import pyplot as plt



def verify(genuine_id, cells, threshold):
    match = any([v for v in cells if v >= threshold])
    decision = {
        match and genuine_id: 'AC', # aceptación correcta
        match and not genuine_id: 'FA', # falsa aceptación
        not match and genuine_id: 'FR', # falso rechazo
        not (match or genuine_id): 'RC' # rechazo correcto
    }
    return decision[True]


thresholds = [x for x in range(100,500)][::20]

similarity_matrix = [
        [[347, 301, 359], [5, 505, 334], [3, 4, 290], [2, 3, 3]],
        [[344, 274, 308], [7, 275, 334], [5, 7, 326], [3, 6, 3]],
        [[4, 9, 3], [270, 6, 3], [254, 292, 9], [268, 194, 283]],
        [[3, 8, 3], [264, 8, 3], [318, 341, 9], [325, 297, 322]]
    ]

verify_matrices = []
genuine_population = 4
impostor_population = 12
errors = []
fmrs = []
fnmrs = []

for t in thresholds:
    verify_matrix = [[],[],[],[]]
    verify_matrices.append(verify_matrix)
    error_set = {'FA': 0, 'FR': 0}
    for r_index, row in enumerate(similarity_matrix):
        for c_index, cells in enumerate(row):
            v = verify(r_index == c_index, cells, t)
            if v in error_set:
                error_set[v] += 1
            verify_matrix[r_index].append([v])

    fmr = error_set['FA'] / impostor_population
    fnmr = error_set['FR'] / genuine_population
    fmrs.append(fmr)
    fnmrs.append(fnmr)
    errors.append({
        'FMR': fmr,
        'FNMR': fnmr
    })

print(fnmrs)
print(fmrs)
fnmr_zero = min([fmr for fmr in fmrs if fmr > 0.0])
fmr_zero = min([fnmr for fnmr in fnmrs if fnmr > 0.0])
print(fnmr_zero, fmr_zero)
print(thresholds)
print(len(thresholds))
plt.plot(fnmrs)
plt.plot(fmrs)
plt.xticks(range(1,len(thresholds)), thresholds, rotation=45)
plt.xlabel('t')
plt.ylabel('Error')
plt.scatter(0.3,0.3, s=10)
plt.show()

