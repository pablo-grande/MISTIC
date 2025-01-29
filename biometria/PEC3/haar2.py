#!/usr/bin/env python
# -*- coding: utf-8 -*
from numpy import mean, std, sqrt, prod, pi, e
from pprint import pprint


def get_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f.readlines():
            row = line.strip().split("\t")
            matrix.append([int(r) for r in row])
    return matrix


class Haar:
    window = []

    def __init__(self, matrix, x, y, h, w):
        self.window = [row[x:w] for row in matrix[y:h]]

    def filter_1(self):
        split = int(len(self.window) / 2)
        white, black = 0, 0

        for row in self.window[:split]:
            white += sum(row)
        for row in self.window[split:]:
            black += sum(row)

        return white - black

    def filter_2(self):
        split = int(len(self.window) / 2)
        white, black = 0, 0

        for row in self.window:
            white += sum(row[:split])
            black += sum(row[split:])

        return white - black

    def filter_3(self):
        split = int(len(self.window) / 3)
        white, black = 0, 0

        for row in self.window:
            white += sum(row[:split])
            remain = row[split:]
            black += sum(remain[:split])
            white += sum(remain[split:])

        return white - black

    def filter_4(self):
        split = int(len(self.window) / 2)
        white, black = 0, 0

        for row in self.window[:split]:
            black += sum(row[:split])
            white += sum(row[split:])

        for row in self.window[split:]:
            white += sum(row[:split])
            black += sum(row[split:])

        return white - black


def get_haar_values(obj_list, window):
    """Modified function in order to return only Haar1"""
    haar_values = [[]]
    for f in obj_list:
        matrix = get_matrix(path + f + ".txt")
        haar = Haar(matrix, **window)
        haar_values[0].append(haar.filter_1())

    return haar_values


def a_priori(mean, std, x):
    exp = (-((x - mean) ** 2)) / (2 * std ** 2)
    return (1 / (std * sqrt(2 * pi))) * e ** exp


def p_face(priori_face, priori_no_face):
    return priori_face / (priori_face + priori_no_face)


def p_no_face(priori_face, priori_no_face):
    return priori_no_face / (priori_face + priori_no_face)


if __name__ == "__main__":

    path = "PEC3_ficheros/"

    window = {"x": 0, "y": 0, "w": 6, "h": 6}
    faces = ["f" + str(i) for i in range(1, 11)]
    no_faces = ["n" + str(i) for i in range(1, 11)]

    vector_faces = get_haar_values(faces, window)
    faces_mean_stds = [(mean(h), std(h)) for h in vector_faces]
    vector_no_faces = get_haar_values(no_faces, window)
    no_faces_mean_stds = [(mean(h), std(h)) for h in vector_no_faces]

    cnn = ["c" + str(i) for i in range(1, 7)]
    vector_cnn = get_haar_values(cnn, window)
    results = [{} for _ in range(len(cnn))]

    for haar_index, value in enumerate(vector_cnn):
        for image_index, x_i in enumerate(value):
            faces_mean, faces_std = faces_mean_stds[haar_index]
            priori_face = a_priori(faces_mean, faces_std, x_i)
            no_faces_mean, no_faces_std = no_faces_mean_stds[haar_index]
            priori_no_face = a_priori(no_faces_mean, no_faces_std, x_i)

            img = results[image_index]
            img[f"Pc{haar_index+1}"] = p_face(priori_face, priori_no_face)
            img[f"Pnc{haar_index+1}"] = p_no_face(priori_face, priori_no_face)

            img["Prod(Pc)"] = prod([v for k, v in img.items() if k.startswith("Pc")])
            img["Prod(Pnc)"] = prod([v for k, v in img.items() if k.startswith("Pnc")])

            img["class"] = "Face" if img["Prod(Pc)"] > img["Prod(Pnc)"] else "No face"

    pprint(results)
