from pyogrio import read_dataframe, write_dataframe
import geopandas as gpd
from datetime import datetime
import pickle
import time

import gzip
import shutil


if __name__ == '__main__':

    
    #this program does the following:
     # - read a gzipped pickle file, 
     # - load it as pickle object
     # - write the data as shape file using pyogrio package.

    f=gzip.open('fw_ptl.gz','rb')
    file_content=pickle.load(f)
    print(len(file_content))
    print((file_content.columns))
    startime=time.process_time()
    #file_content.to_file('test.shp', index=False)
    #file_content.set_crs('EPSG:26917', inplace=True, allow_override=True)
    write_dataframe(file_content,'test.shp', spatial_index=True)
    endtime=time.process_time()
    print("Totoal time writting the file to a shape file is {:5.2f} minutes.".format((endtime-startime)/60))
    f.close()

    