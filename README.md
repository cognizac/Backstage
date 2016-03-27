# Backstage
Take home test for backstage

## Data Installation

### PostgreSQL Server
Here I am assuming that there is a PostgreSQL server running on the local machine at port 5432.
If not, it can be installed by downloading and installing the latest version from this page: <http://www.enterprisedb.com/products-services-training/pgdownload>

If installing on Windows, the path to the bin folder of the PostgreSQL folder (e.g. C:\Program Files\PostgreSQL\9.5\bin) must be added to the system path so that the Chinook scripts below will work.

You must edit the file settings.cfg to use the correct user, password, and database starting from line 5.

### Chinook Database
The Chinook Database data was added to Postgres by downloading the recommended version "ChinookDatabase1.4_CompleteVersion.zip"  
from <https://chinookdatabase.codeplex.com/releases/view/55681>

Upon completion of the download, the contents should be unzipped. Open a command prompt navigate to the directory where the Chinook files were unzipped.  
Run the batch file CreatePostgreSql.bat to create the Chinook DB in Postgres.

## Python Environment
to install the required packages you can simply run:  
```pip install -r requirements.txt```  
using the requirements.txt file in the root directory

Alternatively, you can install the individual packages using Anaconda2 Python Distribution and running the following in your virtual environment:  
```conda install numpy scipy matplotlib pandas seaborn```  
```pip install ipython[all] psycopg2```

If trying to install on windows you may need to download the appropriate wheel file for psycopg2 here:  
http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg  
then use  
```pip install <the wheel file you download based on your version>```

## Running the script
You can run the script to download the data and produce correlational plots with  
```python data_supplementation.py```

if you would like to download the data from the web, edit line 2 of the settings.cfg to read:  
```use_API = true```  
Otherwise, the script will load a pickle file containing the data. Keep in mind this is using a free trial for the weather API so it's best to use the included file.
