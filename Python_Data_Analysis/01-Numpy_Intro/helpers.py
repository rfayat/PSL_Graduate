"Helper functions for December 7th,  2020 Python Session"
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')  # figure styling
RANDOM_STATE = 42  # random state for all random functions


def print_hello():
    "Simply print 'hello'"
    print("hello")


def plot_linear_regression(x, y, slope=1., intercept=0.):
    """Plot the result of a linear regression

    Parameters
    ----------
    x, y: arrays, shape=(n,)
        InpThe input data ofut data

    slope: float, default=1.
        Slope of the regression

    intercept: float, default=0.
        Intercept of the regression

    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # plot the initial data
    ax.scatter(x, y, label="data")

    # plot the output of the linear regression
    x_minmax = np.array([x.min(), x.max()])
    y_predicted_minmax = slope * x_minmax + intercept
    ax.plot(x_minmax, y_predicted_minmax, "--k", label="prediction")

    # Cosmetic stuff
    ax.set_ylabel("salary")
    ax.set_xlabel("years of experience")
    ax.legend(loc="lower right")
    return fig, ax


# Data for simple linear regressions
# from: https://www.kaggle.com/karthickveerakumar/salary-data-simple-linear-regression  # noqa E501
data_linear_regression = np.array([
    [1.1, 39343.],
    [1.3, 46205.],
    [1.5, 37731.],
    [2.0, 43525.],
    [2.2, 39891.],
    [2.9, 56642.],
    [3.0, 60150.],
    [3.2, 54445.],
    [3.2, 64445.],
    [3.7, 57189.],
    [3.9, 63218.],
    [4.0, 55794.],
    [4.0, 56957.],
    [4.1, 57081.],
    [4.5, 61111.],
    [4.9, 67938.],
    [5.1, 66029.],
    [5.3, 83088.],
    [5.9, 81363.],
    [6.0, 93940.],
    [6.8, 91738.],
    [7.1, 98273.],
    [7.9, 101302.],
    [8.2, 113812.],
    [8.7, 109431.],
    [9.0, 105582.],
    [9.5, 116969.],
    [9.6, 112635.],
    [10.3, 122391.],
    [10.5, 121872.]])
