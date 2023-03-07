# Zrp_case

## This repository contains the code of the exploration and prediction of the dataset described at:
https://zrp.github.io/challenges/data-science/

## The project was made using:
- PyCharm with Jupyter Notebook
- Anaconda
- Python 3.9.10
- Windows 10
- All packages are listed in the requirements.txt file

**Observations:**
- `prepare_data.ipynb` is the file that contains the code to prepare the data for Exploratory Analysis and Prediction.
- The resultant dataframes of this file are already stored at `assets`
- Therefore, you can skip the execution of `prepare_data.ipynb` and go directly to the Exploratory Analysis **(eda.ipynb)** and Prediction files **(methodology 1 and 2)**.

## If you want to execute the project inside Google Colab, you need to:
1. Download the zip of the repository and upload it to your Google Drive
2. Extract it
3. Open any .ipyb file and click on the button "Open in Colab" at the top of the file.
4. Put the following code to mount your google drive to the Google Colab environment:

```
from google.colab import drive
drive.mount('/content/drive')
```

5.  In the cells that contains the code:

```
df_diff = pd.read_csv('../assets/df_diff.csv', index_col=0)
# or
df_diff = pd.read_csv('assets/df_start_end', index_col=0)
```
Change the path from where you stored the extracted zip of the repository.
Here is an example:

```
df_diff = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/zrp_case/assets/df_diff.csv', index_col=0)
```

You are all set to execute the project in Google Colab!

