import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MaxNLocator
import cycler as cycler
import datetime

def readsamples(filename,tburn,nwalkers,iterations):
	df1=pd.read_csv(filename,delimiter=',')
	data=np.zeros(df1.shape[0]*(df1.shape[1]-1)).reshape(df1.shape[0],(df1.shape[1]-1))
	for i in range(0,int(df1.shape[1]-1)):
	    data[:,i]=np.array(df1.iloc[:,i+1]) # Put dataframe into array. Dataframe has no. columns = no. parameters.
	data2=np.zeros((df1.shape[0]-tburn*nwalkers)*(df1.shape[1]-1)).reshape((df1.shape[0]-(tburn*nwalkers)),(df1.shape[1]-1))
	for i in range(0,int(df1.shape[1]-1)):
	    for j in range(1,nwalkers+1):
	        data2[(iterations-tburn)*(j-1):(iterations-tburn)*(j),i]=np.array(df1.iloc[iterations*j-iterations+tburn:iterations*j,i+1])
	samplesnoburn=data2
	return samplesnoburn

def plot1(x,y,xerr,yerr,xlim,ylim,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(5.83,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
#	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
#	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

#	fig=plt.figure(); ax=fig.add_subplot(numberofplots,1,1)

	f, axarr=plt.subplots()
	
	axarr.errorbar(x,y,yerr,xerr,fmt='o',ms=6,elinewidth=2,capsize=3,mew=1.5,color='#0d76e8') #f55f4e red #0d76e8 blue

	formatplot(axarr,xlabel,ylabel,legend,xlim,ylim,False,False,False,title)
	plt.show()

def plot2(x,y,yerr,fitx,fity,xlim,ylim,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(5.83,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
#	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
#	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

#	fig=plt.figure(); ax=fig.add_subplot(numberofplots,1,1)

	f, axarr=plt.subplots()

	axarr.plot(fitx,fity,'-',color='#f55f4e')
	axarr.errorbar(x,y,yerr,fmt='o',ms=6,elinewidth=2,capsize=3,mew=1.5,color='#0d76e8') #f55f4e red #0d76e8 blue

	formatplot(axarr,xlabel,ylabel,legend,xlim,ylim,False,False,False,title)
	plt.show()


def plot3(x,y,yerr,samplesnoburn,xlim,ylim,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(5.83,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
#	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
#	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

#	fig=plt.figure(); ax=fig.add_subplot(numberofplots,1,1)

	f, axarr=plt.subplots()

	axarr.errorbar(x,y,yerr,fmt='o',ms=6,elinewidth=2,capsize=3,mew=1.5,color='#0d76e8') #f55f4e red #0d76e8 blue

	xmod=np.linspace(0,300,50)
	for b,m,Pb,Yb,lnVb in samplesnoburn[np.random.randint(len(samplesnoburn), size=20)]:
		ymod=m*xmod+b
		axarr.plot(xmod,ymod,'k-',label='_nolegend_',alpha=0.1)

	formatplot(axarr,xlabel,ylabel,legend,xlim,ylim,False,False,False,title)
	plt.show()

def plot4(x,y,yerr,samplesnoburn,xlim,ylim,xlabel='x',ylabel='y',legend=False,title=False):

	plt.close("all")

	my_dpi=150

	figure_options={'figsize':(5.83,5.83)} #figure size in inches. A4=11.7x8.3, A5=8.27x5.83
	font_options={'size':'20','family':'sans-serif','sans-serif':'Arial'}
	plt.rc('figure', **figure_options)
	plt.rc('font', **font_options)

	# get colormap
#	cmap=plt.cm.Set1
	# build cycler with 5 equally spaced colors from that colormap,supply cycler to the rcParam
#	plt.rcParams["axes.prop_cycle"] = cycler.cycler('color', cmap(np.linspace(0,1,9)) )

#	fig=plt.figure(); ax=fig.add_subplot(numberofplots,1,1)

	f, axarr=plt.subplots()

	axarr.errorbar(x,y,yerr,fmt='o',ms=6,elinewidth=2,capsize=3,mew=1.5,color='#0d76e8') #f55f4e red #0d76e8 blue

	xmod=np.linspace(0,300,50)
	for b,m,Pb,Yb,lnVb,S in samplesnoburn[np.random.randint(len(samplesnoburn), size=20)]:
		ymod=m*xmod+b
		axarr.plot(xmod,ymod,'k-',label='_nolegend_',alpha=0.1)

	formatplot(axarr,xlabel,ylabel,legend,xlim,ylim,False,False,False,title)
	plt.show()


def formatplot(ax,xlabel,ylabel,legend,xlim,ylim,logx,logy,logxy,title):
	my_dpi=150
	
#	logx=False
#	logy=False
#	logxy=False

	######### SET AXES LIMITS #########

	if xlim!=False:
		ax.set_xlim(xlim)
	if ylim!=False:
		ax.set_ylim(ylim)

	######### SET TICK VALUES #########

	ax.tick_params(axis='both',pad=10)
#	ax.set_xticks([0,2e-5,4e-5,6e-5])
#	ax.set_yticks([0,2,4,6,8])

	######### SET TITLES AND LABLES #########

	if title!=False:
		ax.set_title(title)
	if xlabel!=False:
		ax.set_xlabel(xlabel, labelpad=12)
	if ylabel!=False:
		ax.set_ylabel(ylabel, labelpad=12)

	######### SET LINE THICKNESSES #########

#	ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%1.e"))
#	ax.axhline(linewidth=2, color='k')      
#	ax.axvline(linewidth=2, color='k')
	ax.spines['bottom'].set_linewidth(2)
	ax.spines['top'].set_linewidth(2)
	ax.spines['left'].set_linewidth(2)
	ax.spines['right'].set_linewidth(2) 

	######### SET TICKS #########

	if logx==True:

		ax.set_xscale("log")

	elif logy==True:

		ax.set_yscale("log")

	elif logxy==True:

		ax.set_xscale("log")
		ax.set_yscale("log")

	else:
		minorLocatorx=AutoMinorLocator(2) # Number of minor intervals per major interval
		minorLocatory=AutoMinorLocator(2)
		ax.xaxis.set_minor_locator(minorLocatorx)
		ax.yaxis.set_minor_locator(minorLocatory)

	ax.tick_params(which='major', width=2, length=8, pad=9, direction='in')
	ax.tick_params(which='minor', width=2, length=4, pad=9, direction='in')


	######### CALL LEGEND #########

	if legend==True:
		ax.legend(loc='best', fontsize=22,numpoints=1)
#	filename='plot_'+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'_.pdf'

#	plt.savefig(filename,dpi=my_dpi,bbox_inches='tight')


