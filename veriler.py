import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

#Tarih bilgisini silmek için ilgili satır silme
"""
with open(r"veriler.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the first line
    # lines[1:] from line 2 to last line
    fp.writelines(lines[1:])
    
"""
#değerler sırasıyla
#saniye-pitch-roll-yaw-airspeed-altitude-batarya seviyesi

data=np.loadtxt('veriler.txt')
size=np.shape(data)
print("size of data",size)

time=data[:,0]
pitch=data[:,1]*180.0/np.pi
roll=data[:,2]*180.0/np.pi
yaw=data[:,3]*180.0/np.pi
airspeed=data[:,4]
altitude=data[:,5]
batarya=data[:,6]


#first figure
plt.figure()
plt.title("Hareket Eksenleri")
pl.plot(time,roll,'b-',label="Roll")
pl.plot(time,pitch,'r-',label="pitch")
pl.plot(time,yaw,'g-',label="yaw")
plt.legend()
plt.xlabel("zaman(sn)")
plt.ylabel("Angle (derece)")
plt.grid()


#second figure(Hız)
plt.figure()
pl.plot(time,airspeed)
plt.title("Hız")
plt.xlabel("zaman(sn)")
plt.ylabel("hız(m/sn)")
plt.grid()



# third figure

plt.figure()
pl.plot(time,altitude)
plt.title("İrtifa")
plt.xlabel("zaman(sn)")
plt.ylabel("irtifa(m)")
plt.grid()

#fourth figure
plt.figure()
pl.plot(time,batarya)
plt.title("Batarya")
plt.xlabel("zaman(sn)")
plt.ylabel("batarya(V)")
plt.grid()



plt.show()
