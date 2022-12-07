## PrepareCases per Date in Germany as Diagrams
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
#from IPython.display import set_matplotlib_formats
#set_matplotlib_formats('retina')
%config InlineBackend.figure_format = 'retina'

## We create an array for every possible value of Rt
# Why R ? Unter dem "R‑Wert" wird die "Reproduktionszahl R" verstanden. 
# Die Reproduktionszahl beschreibt, wie viele Menschen eine infizierte Person im Mittel ansteckt, und wird regelmäßig durch das RKI mithilfe eines "Nowcastings" geschätzt und veröffentlicht.
R_T_MAX = 12
r_t_range = np.linspace(0, R_T_MAX, R_T_MAX*100+1)

# Gamma is 1/serial interval
GAMMA = 1/4

# Skip last 5 days since the THL data is incomplete for the last few days
# https://wwwnc.cdc.gov/eid/article/26/6/20-0357_article
SKIP_N_LAST_DAYS_IN_DATA = 5
# How many days of history used as posterior
DAYS_USED_IN_POSTERIOR = 7

## Interval for density
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

## Infection und new infections an Date table
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

## Infection , new infections, Date, Id, Deaths and newdeaths as table
def get_all_data_from_RKI():
    url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
    germany = pd.read_csv(url)
    germany['date'] = germany['date'].apply(pd.to_datetime).dt.date
    germany = germany.groupby('date').sum()
    return germany

germany = get_all_data_from_RKI()

## Zusatz mit Bundesländern und Region # Last Call 7199 Datensätze 2021-06-13
url = 'https://covid19publicdata.blob.core.windows.net/rki/covid19-germany-federalstates.csv'
germany = pd.read_csv(url)
germany

## Diagram for Germany new cases per Day
state_name = 'Germany'

    # Note that in the origanal data, the cases were cumulative
    # The RKI data is per day, so there is no need to take diff
def prepare_cases(new_cases):

    # Why Smoothing -> https://en.wikipedia.org/wiki/Smoothing
    smoothed = new_cases.rolling(7,
        win_type='gaussian',
        min_periods=1,
        center=True).mean(std=2).round()
    
    zeros = smoothed.index[smoothed.eq(0)]
    print(zeros)
    if len(zeros) == 0:
        idx_start = 0
    else:
        last_zero = zeros.max()
        idx_start = smoothed.index.get_loc(last_zero) + 1
    smoothed = smoothed.iloc[idx_start:]
    original = new_cases.loc[smoothed.index]
    
    return original, smoothed

cases = germany['newinfections'].rename(f"{state_name} cases")

original, smoothed = prepare_cases(cases)

original.plot(title=f"{state_name} New Cases per Day",
               c='k',
               linestyle=':',
               alpha=.5,
               label='Actual',
               legend=True,
             figsize=(600/72, 400/72))

ax = smoothed.plot(label='Smoothed',
                   legend=True)
ax.get_figure().set_facecolor('w')

## Data for the Realtime Rt
# Why R ? Unter dem "R‑Wert" wird die "Reproduktionszahl R" verstanden. 
# Die Reproduktionszahl beschreibt, wie viele Menschen eine infizierte Person im Mittel ansteckt, und wird regelmäßig durch das RKI mithilfe eines "Nowcastings" geschätzt und veröffentlicht.
# https://www.corona-in-zahlen.de/r-wert/
# https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0250110
def get_posteriors(sr, min_periods=1):
    window=DAYS_USED_IN_POSTERIOR
    lam = sr[:-1].values * np.exp(GAMMA * (r_t_range[:, None] - 1))

    # Note: if you want to have a Uniform prior you can use the following line instead.
    # I chose the gamma distribution because of our prior knowledge of the likely value
    # of R_t.
    
    # prior0 = np.full(len(r_t_range), np.log(1/len(r_t_range)))
    
    prior0 = np.log(sps.gamma(a=3).pdf(r_t_range) + 1e-14)

    likelihoods = pd.DataFrame(
        # Short-hand way of concatenating the prior and likelihoods
        data = np.c_[prior0, sps.poisson.logpmf(sr[1:].values, lam)],
        index = r_t_range,
        columns = sr.index)

    # Perform a rolling sum of log likelihoods. This is the equivalent
    # of multiplying the original distributions. Exponentiate to move
    # out of log.
    posteriors = likelihoods.rolling(window,
                                     axis=1,
                                     min_periods=min_periods).sum()
    posteriors = np.exp(posteriors)

    # Normalize to 1.0
    posteriors = posteriors.div(posteriors.sum(axis=0), axis=1)
    
    return posteriors

posteriors = get_posteriors(smoothed)

## Format Diagram
ax = posteriors.plot(title=f'{state_name} - Daily Posterior for $R_t$',
           legend=False, 
           lw=1,
           c='k',
           alpha=.3,
           xlim=(0.4,4))

ax.set_xlabel('$R_t$');