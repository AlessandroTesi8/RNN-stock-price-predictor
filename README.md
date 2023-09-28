# RNN stock prices
Project Description:
This project consists of a recurrent neural network (RNN) trained on historical stock data of major tech giants over the past 10 years. It is important to note that this RNN is not intended for actual trading purposes as it lacks the accuracy required for real-world financial decisions.

Project Components:

    main.py: This is the main application that takes the stock symbol as input, extracts the stock's values for the last 500 days, and attempts to predict the value for the day following the current day.

    graph.py: This file contains functions that enable the creation of a candlestick chart representing the stock's performance over the last 30 days.

    datascraper.py: This script is responsible for downloading historical stock values for the past 500 days from a data source.

    RNN_train.py: This script was used in the training process of the neural network. However, it is no longer necessary for the project's current functionality.

    dataprocesser.py: This file contains functions that take the dataset acquired by the datascraper and preprocess it, making it suitable for input into the neural network.

    savedRNN.keras: This file represents the trained neural network model that has been saved for use in the project.

    datasets folder: This folder, which is not included in the upload, used to contain the training datasets that were utilized during the training process.

License: Please note that this project is not covered by any specific license. It is provided for educational and experimental purposes only, and its predictions should not be used for actual trading decisions due to its limited accuracy.