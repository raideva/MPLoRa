import pandas
import matplotlib.pyplot as plt


def plot_mse():
    p = pandas.read_csv("data/report.csv")[0:3]
    plt.ylabel("Mean Square Error (dBM)")
    plt.xlabel("Distance (m)")

    plt.plot(p.distance, p.proposed_model_mse, label="Mean Square error for proposed model")
    plt.plot(p.distance, p.okumara_mse, label="Mean Square error for okumara hata model")
    plt.plot(p.distance, p.log_distance_mse, label="Mean Square error for log distance model")
    plt.plot(p.distance, p.lebanon_rural_mse, label="Mean Square error for lebanon rural model")
    plt.plot(p.distance, p.lebanon_campus_mse, label="Mean Square error for lebanon campus model")
    plt.legend()
    plt.show()

def plot_rmse():
    p = pandas.read_csv("data/report.csv")[0:3]
    plt.ylabel("Root mean Square Error (dBM)")
    plt.xlabel("Distance (m)")
    plt.plot(p.distance, p.proposed_model_rmse, label="Root mean Square error for proposed model")
    plt.plot(p.distance, p.okumara_rmse, label="Root mean Square error for okumara hata model")
    plt.plot(p.distance, p.log_distance_rmse, label="Root mean Square error for log distance model")
    plt.plot(p.distance, p.lebanon_rural_rmse, label="Root mean Square error for lebanon rural model")
    plt.plot(p.distance, p.lebanon_campus_rmse, label="Root mean Square error for lebanon campus model")
    plt.legend()
    plt.show()

plot_rmse()