# ZRP Case

## This repository contains the code of the exploration and prediction of the dataset described at:
https://zrp.github.io/challenges/data-science/

## The project was made using:
- PyCharm with Jupyter Notebook
- Anaconda
- Python 3.9.10
- Windows 10
- All packages used are listed in the `requirements.txt` file

## Project Overview
- Diagram:
![Diagram](https://github.com/guico3lho/zrp_case/blob/main/assets/diagram_zrp_case.png?raw=true)
- `assets` folder contains the dataframes used in the project
- `pipiline` folder contains the funnel of the project, described by the diagram above
- `prepare_data.ipynb` is the file that contains the code to prepare the data for Exploratory Analysis and Prediction.
- `eda.ipynb` contains the Exploratory Analysis of the dataset
- `methodology 1` contains code used to evaluate traditional machine learning models for the prediction of the **inference**.
- `methodology 2` contains code used to evaluate deep learning model (The recurrent neural network LSTM was used) for the prediction of the **inference**.



**Observations:**
- `prepare_data.ipynb` is the file that contains the code to prepare the data for Exploratory Analysis and Prediction.
- The resultant dataframes of this file are already stored at `assets`
- Therefore, you can skip the execution of `prepare_data.ipynb` and go directly to the Exploratory Analysis **(eda.ipynb)** and prediction files **(methodology 1 and 2)**.



## If you want to execute the project inside Google Colab, you need to:
1. Download the zip of the repository and upload it to your Google Drive
2. Extract it
3. Open any .ipynb file and click on the button "Open in Colab" at the top of the file.
4. Put the following code to mount your google drive to the Google Colab environment:

```
from google.colab import drive
drive.mount('/content/drive')
```

5.  In the cells that contains the code:

```
df_diff = pd.read_csv('../assets/df_diff.csv', index_col=0)
# or
df_diff = pd.read_csv('assets/df_start_end.csv', index_col=0)
# or
model = keras.models.load_model('../../assets/model')
```
Change the path from where you stored the extracted zip of the repository.
Here is an example:


```
df_diff = pd.read_csv('/content/drive/MyDrive/Empresas/ZRP/Desafio Técnico/zrp_case-main/assets/df_diff.csv', index_col=0)
```

You are all set to execute the project in Google Colab!

## Conclusion of the models used on project
Comparing the best traditional model (KNN) with the RNN model (LSTM), the RNN model had a better accuracy: 75.85% againist 73% of KNN.

