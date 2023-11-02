from pyogrio import read_dataframe, write_dataframe
import geopandas as gpd
from datetime import datetime
import pickle
import time

import gzip
import shutil


if __name__ == '__main__':

    #test to read the pickled file
    #read the pickle file, and check the dataframe.
    picklefile = open('fw_ptl.pkl', 'rb')

    #unpickle the dataframe
    pickle_read_start = time.process_time()
    df = pickle.load(picklefile)
    pickle_read_end = time.process_time()

    #check the pickle file
    print(len(df))
    print(df.columns)

    #close file
    picklefile.close()

    pickle_read = (pickle_read_end - pickle_read_start)/60
    print(str(pickle_read)+" minutes")






