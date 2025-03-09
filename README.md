This is the repository corresponding to Daiichi Sankyo's challenge for the "Data Scientist" position.

In this repository you can find 2 folders:

1) Jupyter_notebook: here I solved the proposed task in a notebook. The final "predictions.csv" file with the predictions is stored in the folder "data".

2) API_Flask: developed as an extra task. I took the resulting model from point 1 and created an API in Flask in order to simulate a "virtual production" environment. The idea is using the trained model for performing predictions programatically by means of GET calls.

3) APP_Streamlit: developed as an extra task. I created a user interface so that the bank workers could easily get a prediction about the customer subscribing or not just typing the parameters in drop down menus and input boxes. I have used the library "Streamlit" which comes in hand for creating quick using interfaces with python. The predictions are obtained by calling the API developed in the second point.


Notes about the set up: the task was developed in an Ubuntu OS using an anaconda environment. The models were trained locally using my Nvidia GEFORCE RTX GPU graphic card.