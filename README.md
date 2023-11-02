# ReadingLargeShapeFile
Reading Large File

I have been using geopandas, and enjoying the package to working on the shape file, however, lately I was working with some large shape file (over 1Gb for the dbf file), and when I open the file using geopandas, and found it took over 22 minutes just to read the file into the memory. Obviously, this is too long. I did some googling, and find the informaiton in the following link: https://dev.to/spara_50/speeding-up-geo-data-processing-ig7. It suggested to use pyogrio instead of geopandas. I took the fragement code, and I found the reading time has been greated reduced using pyogrio, it took less than 2 minutes to read the file.

In Sophia Parafina's article reffered above, she said she experimented to stream the data using pickle package, and compress the data to stream, and read and write, and the speed of reading and writting even fast. A third version of the code was added to check how well the pickle package in dealing with the large size data. 

The file codes are included in here: 
  readingUsingGeopanda.py
  
  readingUsingPygiro.py
  
  readingUsingPygrioPickle.py
  
  readingPickleFile.py
  
  ReadAndZipPickleFile.py
  
  ReadGZipFile.py


