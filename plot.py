import pylab
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num

datafile = cbook.get_sample_data("/home/eels/code/temp-plotter/tempData.dat", asfileobj=False)
print("loading", datafile)

#datefunc = lambda  x:mdates.date2num(datetime.strptime(x,'%Y-%m-%d'))

dates, temps = np.loadtxt(datafile, delimiter=',', dtype=float,
                           converters={1: bytespdate2num('%I:%M %p %Y-%m-%d')},
                            usecols=(1,0), unpack=True)
fig = plt.figure()
#1x1 grid
ax = fig.add_subplot(111)
ax.set_xticks(dates)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
ax.set_title('Temperature in Porvoo')
ax.set_ylabel('Temp')
ax.set_xlabel('Date')
ax.plot_date(dates,temps,'-', marker='o')
ax.grid(True)
fig.autofmt_xdate(rotation=45)
plt.show()
