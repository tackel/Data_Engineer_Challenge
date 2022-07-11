import zipfile


def extrac_data():
    """
    Function for extract all folder and files from the .zip file to use in the tasks 
    """
    with zipfile.ZipFile('Data+Engineer+Programming+Exercise.zip', 'r') as zip_ref:
        zip_ref.extractall('data_exercise')
