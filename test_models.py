import math

import datasets
from proposed_model_train import ProposedModel

dataset = []

dataset.append(datasets.datasets("data/dataset_sf_10.csv", distance=1, hr=0.5, ht=0.5).p)
dataset.append(datasets.datasets("data/dataset_sf_6.csv", distance=88, hr=4.2, ht=4.2).p)
dataset.append(datasets.datasets("data/dataset_sf_7.csv", distance=88.2, hr=4.2, ht=7.62).p)
dataset.append(datasets.datasets("data/dataset_sf_11.csv", distance=14.6, hr=1.5, ht=1).p)
dataset.append(datasets.datasets("data/dataset_sf_13.csv", distance=120, hr=7, ht=7).p)
dataset.append(datasets.datasets("data/dataset_sf_14.csv", distance=120, hr=10, ht=7).p)
dataset.append(datasets.datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1).p)
dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62).p)



def okumura_hata(h_e, h_r, d, fc=868):
    """
    fc: carrier frequency in MHz
    h_e: height of the effective antenna in meters
    h_r: height of the receiving antenna in meters
    d: distance between antennas in kilometers
    """
    # Constants for suburban areas
    pl = 69.55 + 26.16 * math.log10(fc) - 13.8 * math.log10(h_e) - 1.1 * math.log10(fc - 0.7) * h_r - (
                1.56 * math.log10(fc) - 0.8) + (44.9 - 6.55 * math.log10(h_e)) * math.log10(d)
    return 110 - pl


def proposed_model_prediction(solution, bias=0, f=None):
    res = []
    for p in dataset:
        for k in range(len(p)):
            res.append([solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]) + bias, round(p['rssi'][k] + bias)])

    # if f != None:
    #     fi = open(f, "w")
    #     fi.writelines("Prediction,Actual,\n")
    #     for i, j in res:
    #         fi.writelines(str(i) + ',' + str(j) + ',\n')
    #
    #     fi.close()

    return res




def average_error(solution, bias=0):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]) + bias)

            # error += abs(-p['rssi'][k] + okumura_hata(p['ht'][k], p['hr'][k], p['distance'][k]))

            # error += abs(p['rssi'][k] + 43.904 + math.log10(p['distance'][k]) * 15.73)
            q += 1
    fitness = error / q
    return fitness


def rmse(solution, bias=0):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]) + bias + 5 * p['nw'][k] + 11 * p['nf'][k]) ** 2

            # error += abs(-p['rssi'][k] + okumura_hata(p['ht'][k], p['hr'][k], p['distance'][k])) ** 2

            # error += abs(p['rssi'][k] + 43.904 + math.log10(p['distance'][k]) * 15.73) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 29.05 + math.log10(p['hr'][k]) *
            #              -5.42 - 1.51 * math.log10(p['hr'][k]) * math.log10(p['distance'][k])) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 31.19 - 4.7 * math.log10(p['hr'][k])) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 28.5 + 1.41 * p['nw'][k] + 6.5 * (p[
            # 'nf'][k]) ** ((p['nf'][k] + 2) / (p['nf'][k] + 1) - 0.47)) ** 2
            q += 1
    fitness = math.sqrt(error / q)
    return fitness


def mse(solution, bias=0):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]) + bias + 5 * p['nw'][k] + 11 * p['nf'][k]) ** 2

            # error += abs(-p['rssi'][k] + okumura_hata(p['ht'][k], p['hr'][k], p['distance'][k])) ** 2
            # error += abs(p['rssi'][k] + 43.904 + math.log10(p['distance'][k]) * 15.73) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 29.05 + math.log10(p['hr'][k]) *
            #              -5.42 - 1.51 * math.log10(p['hr'][k]) * math.log10(p['distance'][k])) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 31.19 - 4.7 * math.log10(p['hr'][k])) ** 2

            # error += abs(p['rssi'][k] + 44 + math.log10(p['distance'][k]) * 28.5 + 1.41 * p['nw'][k] + 6.5 * (p['nf'][k]) ** ((p['nf'][k] + 2) / (p['nf'][k] + 1) - 0.47)) ** 2

            q += 1
    fitness = error / q
    return fitness


pro = ProposedModel(dataset)
p = pro.train()
dataset.clear()

def res_for_distance():
    dataset.append(datasets.datasets("data/dataset_sf_11.csv", distance=14.6, hr=1.5, ht=1, v=1).p)
    print(proposed_model_prediction(p, bias=0, f="output_14m.csv"))
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()

    dataset.append(datasets.datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1, v=1).p)
    print(proposed_model_prediction(p, bias=0, f="output_33m.csv"))
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()

    dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62, v=1).p)
    print(proposed_model_prediction(p, bias=0, f="output_88m.csv"))
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()


def res_for_heights():
    dataset.append(datasets.datasets("data/dataset_sf_6.csv", distance=88, hr=4.2, ht=4.2, v=1).p)
    proposed_model_prediction(p, bias=0, f="output_height_4&4m.csv")
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()

    dataset.append(datasets.datasets("data/dataset_sf_7.csv", distance=88.2, hr=4.2, ht=7.62, v=1).p)
    proposed_model_prediction(p, bias=-1.7, f="output_height_4&7m.csv")
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()

    dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62, v=1).p)
    proposed_model_prediction(p, bias=0, f="output_height_7&7m.csv")
    print("Average error :", average_error(p))
    print("Root mean square error :", rmse(p))
    print("mean square error :", mse(p))
    dataset.clear()

res_for_heights()


def additional_loss(q: list, d, hr, ht):
    # q = ['distance_from_receiver','height', 'no_walls']
    a = 0
    for i in q:
        h = (hr * i[0] + ht * (d - i[0])) / d
        if h <= i[1]:
            a += i[2] * 1.57
    return a

# dataset.append(datasets.datasets("data/dataset_sf_16.csv", distance=512, hr=14, ht=1, v=1).p)
# ad = add_loss("data2", 512, 14, 1, [125, 160, 210, 280, 320])
# print("Average error :", average_error(p, ad))
# print("Root mean square error :", rmse(p, ad))
# print("mean square error :", mse(p, ad))
# dataset.clear()
#
#
# dataset.append(datasets.datasets("data/dataset_sf_17.csv", distance=700, hr=14, ht=1, v=1).p)
# ad = add_loss("data3", 700, 14, 1, [120, 150, 180])
# print("Average error :", average_error(p, ad))
# print("Root mean square error :", rmse(p, ad))
# print("mean square error :", mse(p, ad))
# dataset.clear()
#
#
# dataset.append(datasets.datasets("data/dataset_sf_18.csv", distance=700, hr=14, ht=1, v=1).p)
# print("Average error :", average_error(p, 9))
# print("Root mean square error :", rmse(p, 9))
# print("mean square error :", mse(p, 9))
# dataset.clear()
# dataset.append(datasets.datasets("data/dataset_sf_19.csv", distance=780, hr=14, ht=4, v=1).p)
# print("Average error :", average_error(p, additional_loss([[120, 14, 3], [170, 13, 2]], 780, 14, 4)))
# print("Root mean square error :", rmse(p, additional_loss([[120, 14, 3], [170, 13, 2]], 780, 14, 4)))
# print("mean square error :", mse(p, additional_loss([[120, 14, 3], [170, 13, 2]], 780, 14, 4)))
# dataset.clear()
