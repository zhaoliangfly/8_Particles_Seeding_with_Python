
from math import sqrt
import random

Particle_Number=8
Radius_Exclusion=0.5
Allowed_Uplimite=10000
Box_X=4.2
Box_Y=4.2
Box_Z=4.2
Frames=10000

Sta_Interval=0.2
Sta_Length=30

def distance(x1,y1,z1,x2,y2,z2):
	d=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
	return d

#file_write=open("8_random_seed.dat","w")
x=[0 for i in range(0,Sta_Length)]
y=[0 for i in range(0,Sta_Length)]
z=[0 for i in range(0,Sta_Length)]

frame=1
while frame <= Frames:
	p=[]
	frame += 1
	n=1
	while n <= Particle_Number:
		if n==1:
			a=[random.uniform(0,4.2),random.uniform(0,4.2),random.uniform(0,4.2)]
			p.append(a)
			n += 1
		if n>=2:
			seeding_time=0
			while seeding_time <= Allowed_Uplimite:
				b=[random.uniform(0,4.2),random.uniform(0,4.2),random.uniform(0,4.2)]
				success=0
				for j in range(1,n):
					if distance(b[0],b[1],b[2],p[j-1][0],p[j-1][1],p[j-1][2])>Radius_Exclusion:
						success += 1
					else:
						seeding_time += 1
						break
				if success == n-1:
					p.append(b)
					n += 1
					break
	
	for i in range(0,Particle_Number):
		x[int(p[i][0]*1.0/Sta_Interval)] += 1
		y[int(p[i][1]*1.0/Sta_Interval)] += 1
		z[int(p[i][2]*1.0/Sta_Interval)] += 1
    
for i in range(0,Sta_Length):
	print i*Sta_Interval,(x[i]*1.0/(1.0*Frames*Sta_Interval*4.2*4.2)+y[i]*1.0/(1.0*Frames*Sta_Interval*4.2*4.2)+z[i]*1.0/(1.0*Frames*Sta_Interval*4.2*4.2))/3.0/0.602







		



