#!/usr/bin/env python
import numpy as np
import xarray as xr
import os

ifiles = '/tigress/wenchang/MODEL_OUT/CTL2000_noleap_tigercpu_intelmpi_18_576PE/POSTP/????0101.atmos_daily.nc'
ifile = ifiles.replace('????', '0001')
data_name = "precip"
ofile = f'CTL2000_noleap_tigercpu_intelmpi_18_576PE.atmos_daily.{data_name}.nc'
xname = 'grid_xt'
xlim = (70, 80)
yname = 'grid_yt'
ylim = (5, 15)

x = xr.open_mfdataset(ifile)[xname].values
ix = x.argsort()
L = (x>=xlim[0]) & (x<=xlim[1])
ixlim = ix[L][0], ix[L][-1]
print(f'xlim: {xlim}; ixlim: {ixlim}')

y = xr.open_mfdataset(ifile)[yname].values
iy = y.argsort()
L = (y>=ylim[0]) & (y<=ylim[1])
iylim = iy[L][0], iy[L][-1]
print(f'ylim: {ylim}; iylim: {iylim}')

cmd = f'ncrcat -v {data_name} -d {xname},{ixlim[0]},{ixlim[1]} -d {yname},{iylim[0]},{iylim[1]} {ifiles} {ofile}'
print(cmd, '...')
s = os.system(cmd)
if s==0:
    print('[OK]:', cmd)
