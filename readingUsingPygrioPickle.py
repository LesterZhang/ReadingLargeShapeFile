from pyogrio import read_dataframe, write_dataframe
import geopandas as gpd
from datetime import datetime
import pickle
import time



if __name__ == '__main__':
    
    #this program does the following:
     # - read a the shape file using pyogrio package, the shape file has a size of over 1GB, and about 12 million data entries. 
     # - write the data to a new shape file, and check the time require writing the file
     # - pickle the data using the data package, and write as a pick file, and check the time required to do the writing.
     # - 


    #Read the shape file using pygiro 

    time1= datetime.now()
    print(time1)

    ptl_gpd=read_dataframe('fw_ptl.shp')
    Particle_IDs=ptl_gpd['ID'].unique()
    
    time2= datetime.now()
    print(time2)
    timeDif=time2-time1

    print("It took about {:5.2f} minutes to read the shape file.".format(timeDif.total_seconds()/60))    

    #write the shape file using pygiro
    write_dataframe(ptl_gpd, 'fw_ptl_1.shp', spatial_index=True)

    time3= datetime.now()
    print(time3)
    timeDif=time3-time2
    print("It took about {:5.2f} minutes to write the shape file.".format(timeDif.total_seconds()/60))    


    #pickle the data
    picklefile = open('fw_ptl.pkl', 'wb')

    #pickle the dataframe
    pickle_write_start = time.process_time()
    pickle.dump(ptl_gpd, picklefile)
    pickle_write_end = time.process_time()

    #close file
    picklefile.close()

    pickle_write = (pickle_write_end - pickle_write_start)#/60
    print("Writting the pickled file took {:5.2f} seconds.".format(pickle_write))









