import matplotlib.pyplot as plt

floor2_snr = [[6.60304054054054, 1.0356520721616314],
              [7.648333333333333, 0.7932510461526177],
              [8.04026845637584, 0.894177246448042],
              [7.9783333333333335, 0.6582404997837459],
              [7.226666666666667, 0.7859954763794057],
              [6.305743243243243, 1.1077205052989458]]

floor2_rssi = [[-98.62162162162163, 1.3823472273020998],
               [-97.30666666666667, 0.7388880534665286],
               [-97.79865771812081, 0.7770177523976538],
               [-97.75333333333333, 0.8321591728082369],
               [-99.34666666666666, 1.0582165289874383],
               [-99.72297297297297, 1.4085690743117205]]

floor1_snr = [[9.632075471698114, 0.5592358617086389],
              [11.7675, 0.5865737379051332],
              [11.62, 1.2631706139710503],
              [12.5175, 1.019960170790997],
              [10.5525, 0.8248446823493499],
              [9.466494845360824, 0.852247533420222]]

floor1_rssi = [[-74.39622641509433, 3.1283223706000287],
               [-73.77, 1.5482570845954489],
               [-73.97, 1.053138167573467],
               [-73.27, 1.0663489110042734],
               [-74.72, 2.0788458336298055],
               [-74.43298969072166, 1.9259873167348782]]

wall1_snr = [[9.607894736842105, 0.5008579896155922],
             [11.675, 0.5018714974971183],
             [12.1075, 1.4253311018847514],
             [11.440104166666666, 1.208555003912788],
             [10.65, 1.1118677978968543],
             [9.9425, 1.5070065527395693]]

wall1_rssi = [[-69.54736842105264, 1.9236392103599753],
              [-70.67, 3.8860133813459785],
              [-70.04, 2.806848766855813],
              [-70.23958333333333, 1.3975036647735688],
              [-72.31, 2.5206943487856672],
              [-71.89, 2.6754251998514182]]

wall2_snr = [[9.669191919191919, 0.552574647395989],
             [11.97, 0.41725292090050137],
             [13.315, 0.38829756630707846],
             [11.93, 1.2354553816305953],
             [11.00765306122449, 0.5421683619455405],
             [9.36111111111111, 0.6800013203921953]]

wall2_rssi = [[-73.17171717171718, 1.2230150196093181],
              [-72.75, 0.7664854858377946],
              [-73.08, 0.7304792947099868],
              [-74.42, 1.1762652762026087],
              [-75.11224489795919, 0.9988018644930462],
              [-74.83838383838383, 1.079721912449521]]


def reshape(x, y):
    v = []
    for i in x:
        v.append(i[y])
    return v


p = [7, 8, 9, 10, 11, 12]
plt.ylabel("mean rssi")
plt.xlabel("spreading factor")
plt.plot(p, reshape(floor2_rssi, 0), label="Mean rssi value for 2 floors")
plt.plot(p, reshape(floor1_rssi, 0), label="Mean rssi value for 1 floor")
plt.plot(p, reshape(wall2_rssi, 0), label="Mean rssi value for 2 walls")
plt.plot(p, reshape(wall1_rssi, 0), label="Mean rssi value for 1 wall")
plt.legend()
plt.show()

plt.ylabel("standard deviation of rssi")
plt.xlabel("spreading factor")
plt.plot(p, reshape(floor2_rssi, 1), label="Standard deviation of rssi value for 2 floors")
plt.plot(p, reshape(floor1_rssi, 1), label="Standard deviation of rssi value for 1 floor")
plt.plot(p, reshape(wall2_rssi, 1), label="Standard deviation of rssi value for 2 walls")
plt.plot(p, reshape(wall1_rssi, 1), label="Standard deviation of rssi value for 1 wall")
plt.legend()
plt.show()

plt.ylabel("mean snr")
plt.xlabel("spreading factor")
plt.plot(p, reshape(floor2_snr, 0), label="Mean snr value for 2 floors")
plt.plot(p, reshape(floor1_snr, 0), label="Mean snr value for 1 floor")
plt.plot(p, reshape(wall2_snr, 0), label="Mean snr value for 2 walls")
plt.plot(p, reshape(wall1_snr, 0), label="Mean snr value for 1 wall")
plt.legend()
plt.show()

plt.ylabel("standard deviation of snr")
plt.xlabel("spreading factor")
plt.plot(p, reshape(floor2_snr, 1), label="Standard deviation of snr value for 2 floors")
plt.plot(p, reshape(floor1_snr, 1), label="Standard deviation of snr value for 1 floor")
plt.plot(p, reshape(wall2_snr, 1), label="Standard deviation of snr value for 2 walls")
plt.plot(p, reshape(wall1_snr, 1), label="Standard deviation of snr value for 1 wall")
plt.legend()
plt.show()


# proposed_model = [[1.3463746033142634, 1.9123884187160847, 3.6572294640394065],
#                   [3.7150527134664753, 3.9638460571993783, 27.20209021858142],
#                   [1.8943608708101987, 1.9874848514746741, 3.9500960348413074],
#                   [ 1.674767200390397, 1.7792736055083138, 3.165814563258555],
#                   [1.912227517850709, 1.9733900782696578, 3.8942684010131265],
#                   [0.8345261012508101, 1.0795946602102673, 1.1655246303545224]]
#
# okumara_model = [[31.706376771273955, 31.762005878169727, 1008.8250174048884],
#                  [1.2022917171451373, 1.559798219909264, 2.4329704868321085],
#                  [1.7328897444554265, 1.834230027129474, 3.364399792423391],
#                  [8.063250730142366, 8.08560336183369, 65.3769817248963],
#                  [8.24579041268204, 8.260188487611309, 68.2307138508664],
#                  [7.840997049948576, 7.891599753113609, 62.277346663342776]]
#
# log_distance_model = [[1.349637318897582, 1.9018329435943417, 3.6169685453407183],
#                       [1.487860317585179, 3.124346101236997, 3.389692412801804],
#                       [20.78229232214044, 20.79098764101595, 432.2651670888779],
#                       [18.414036402004236, 18.42383526853446, 339.43770600209433],
#                       [18.231496719464644, 18.23801324028571, 332.6251269528368],
#                       [15.975791378263695, 16.000688175445323, 256.02202208783575]]
#
# plt.ylabel("Root Mean Square Error (dBM)")
# plt.xlabel("Datasets")
# q = [1, 2, 3, 4, 5, 6]
# plt.plot(q, reshape(proposed_model, 1), label="Root Mean Square error for proposed model")
# plt.plot(q, reshape(okumara_model, 1), label="Root Mean Square error for okumara hata model")
# plt.plot(q, reshape(log_distance_model, 1), label="Root Mean Square error for log distance model")
# plt.legend()
# plt.show()
