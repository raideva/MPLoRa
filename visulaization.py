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
# plt.plot(p, reshape(floor2_rssi, 0), label="Mean rssi value for 2 floors")
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
