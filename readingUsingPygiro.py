from pyogrio import read_dataframe, write_dataframe
import geopandas as gpd
from datetime import datetime
import pickle


if __name__ == '__main__':

    #This file did the following: 

    # - read the shape file 'ft_ptl.shp', the file size is over 1Gb (nearly 12 Million data entries). It took about 2 minutes to read the data using pyogrio package
    # - write the data to a new shape file using the pyogrio package,  it took about 4.15 minutes to write the data using pyogrio package

    time1= datetime.now()
    print(time1)

    ptl_gpd=read_dataframe('fw_ptl.shp')
    Particle_IDs=ptl_gpd['ID'].unique()
    
    time2= datetime.now()
    print(time2)
    timeDif=time2-time1

    print("It took about {:5.2f} minutes to read the shape file.".format(timeDif.total_seconds()/60))    

    write_dataframe(ptl_gpd, 'fw_ptl_1.shp', spatial_index=True)

    time3= datetime.now()
    print(time2)
    timeDif=time2-time1
    print("It took about {:5.2f} minutes to write the shape file.".format(timeDif.total_seconds()/60))    


