import geopandas as gpd
import time
import pickle

if __name__ == '__main__':

    time1= datetime.now()
    print(time1)

    ptl_gpd=gpd.read_file('fw_ptl.shp', crs='EPSG:26917')
    Particle_IDs=ptl_gpd['ID'].unique()
    
    time2= datetime.now()
    print(time2)
    timeDif=time2-time1

    print("Opening the forward particle tracking shape file took about {:5.2f} seconds".format(timeDif.total_seconds()))    

