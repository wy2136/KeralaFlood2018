#!/usr/bin/env python
import numpy as np
import xarray as xr
import os

ifiles = '/tigress/wenchang/data/gpcc/precip.mon.total.v7.nc'
data_name = "precip"
ofile = 'gpcc.nc'
xname = 'lon'
xlim = (70, 80)
yname = 'lat'
ylim = (5, 15)
yincrease = False

x = xr.open_mfdataset(ifiles)[xname].values
ix = x.argsort()
L = (x>=xlim[0]) & (x<=xlim[1])
ixlim = ix[L][0], ix[L][-1]
print(f'xlim: {xlim}; ixlim: {ixlim}')

y = xr.open_mfdataset(ifiles)[yname].values
iy = y.argsort()
if yincrease is False:
    iy = iy[-1::-1]# reverse the indices when y is decreasing along axis
L = (y>=ylim[0]) & (y<=ylim[1])
iylim = iy[L][0], iy[L][-1]
print(f'ylim: {ylim}; iylim: {iylim}')

cmd = f'ncks -v {data_name} -d {xname},{ixlim[0]},{ixlim[1]} -d {yname},{iylim[0]},{iylim[1]} {ifiles} {ofile}'
print(cmd, '...')
s = os.system(cmd)
if s==0:
    print('[OK]:', cmd)
