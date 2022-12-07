#PrepareCases per Date in Deutschland als Diagramm
import pandas as pd
import numpy as np

from datetime import datetime as dt
from datetime import timedelta

from matplotlib import pyplot as plt
from matplotlib.dates import date2num, num2date
from matplotlib import dates as mdates
from matplotlib import ticker
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

from scipy import stats as sps
from scipy.interpolate import interp1d

from IPython.display import clear_output

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

#%config InlineBackend.figure_format = 'retina'

# We create an array for every possible value of Rt
R_T_MAX = 12
r_t_range = np.linspace(0, R_T_MAX, R_T_MAX*100+1)

# Gamma is 1/serial interval
# https://wwwnc.cdc.gov/eid/article/26/6/20-0357_article
GAMMA = 1/4

# Skip last 5 days since the THL data is incomplete for the last few days
SKIP_N_LAST_DAYS_IN_DATA = 5
# How many days of history used as posterior
DAYS_USED_IN_POSTERIOR = 7

def highest_density_interval(pmf, p=.95):
    
    # If we pass a DataFrame, just call this recursively on the columns
    if(isinstance(pmf, pd.DataFrame)):
        return pd.DataFrame([highest_density_interval(pmf[col]) for col in pmf],
                            index=pmf.columns)
    
    cumsum = np.cumsum(pmf.values)
    best = None
    for i, value in enumerate(cumsum):
        for j, high_value in enumerate(cumsum[i+1:]):
            if (high_value-value > p) and (not best or j<best[1]-best[0]):
                best = (i, i+j+1)
                break
            
    low = pmf.index[best[0]]
    high = pmf.index[best[1]]
    return pd.Series([low, high], index=['Low', 'High'])
# Infection und new infections an Date Tabelle
def get_data_from_RKI():
    url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
    germany = pd.read_csv(url)
    germany['date'] = germany['date'].apply(pd.to_datetime).dt.date
    germany.set_index(germany['date'], inplace=True)
    germany = germany[['federalstate', 'infections', 'newinfections']]
    germany = germany.groupby('date').sum()
    return germany

germany = get_data_from_RKI()
germany
# Infection , new infections, Date, Id, Deaths und newdeaths als Tabelle
def get_all_data_from_RKI():
    url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
    germany = pd.read_csv(url)
    germany['date'] = germany['date'].apply(pd.to_datetime).dt.date
    germany = germany.groupby('date').sum()
    return germany

germany = get_all_data_from_RKI()

url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
germany = pd.read_csv(url)
germany

# Zusatz mit Bundesländern und Region # Last Call 7199 Datensätze 2021-05-22
url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
germany = pd.read_csv(url)
germany
