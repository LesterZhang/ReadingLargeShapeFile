from pyogrio import read_dataframe, write_dataframe
import geopandas as gpd
from datetime import datetime
import pickle
import time

import gzip
import shutil


if __name__ == '__main__':
    
    #This file did the following: 
    # - read the pickled file 'ft_ptl.pkl', and zipped using gzip to a zip file, and check the processing time, it took 1.41 minues on my machine.

    pickle_write_zipstart = time.process_time()

    #read and zip pickle file
    with open('fw_ptl.pkl', 'rb') as f_in:
        with gzip.open('fw_ptl.gz', 'wb', compresslevel = 4) as f_out:    #by default, the compression level is 9, which is highest, but not necessarily the best.
            shutil.copyfileobj(f_in, f_out)

    pickle_write_zipend= time.process_time()

    pickle_zip = (pickle_write_zipend - pickle_write_zipstart)/60.0
    print("It took about {:5.2f} minutes to read the pickle file and zip it to a zip file.".format(pickle_zip))





