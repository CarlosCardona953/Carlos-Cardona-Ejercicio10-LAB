#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import csv
import urllib
from io import StringIO
from io import BytesIO
from datetime import datetime
import scipy.signal as signal
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


os.system("curl https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt > Transacciones.txt")


data = pd.read_csv("Transacciones.txt",delimiter = ";", header = None, decimal=",")

fecha = data[0].str[0:-8:1]
hora = data[1].str[10:]
tiempo  = fecha+hora
tiempo =np.array(pd.to_datetime(tiempo,format='%d/%m/%Y %H:%M:%S'))
dinero = np.array(data[2])
data.set_index(tiempo,inplace=True)


# In[4]:


plt.figure(figsize=(20,7))
plt.plot(tiempo,dinero,label="Dinero")
plt.legend()
plt.savefig("Transacciones2008/2010.png")
plt.show()


# In[6]:


N  = 2    # Orden del filtro
Wn = 0.0001 # Corte de frecuencia
B, A = signal.butter(N, Wn)
dinero_filtrado = signal.filtfilt(B,A, dinero)


# In[7]:



fig = plt.figure(figsize=(30,10))
ax1 = fig.add_subplot(211)
plt.plot(tiempo,dinero, 'b-')
plt.plot(tiempo,dinero_filtrado, 'r-',linewidth=2)
plt.ylabel(r"Dinero $")
plt.legend(['Original','Filtrado'])
plt.title("Transacciones")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(tiempo,dinero-dinero_filtrado, 'b-')
plt.ylabel(r"Dinero $")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("Transacciones con filtro.png")
plt.show()


# In[8]:


plt.figure(figsize=(20,7))
ruido=dinero-dinero_filtrado
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.savefig("Correlacion.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




