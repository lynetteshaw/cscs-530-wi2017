## Introduction to PyCX

The purpose of the PyCX Project is to provide a repository of simple Python ABMs and other complex system models 
to people interested in the computational modeling of such systems. In addition to providing these models, 
PyCX also provides modelers with a simple GUI for their own projects, which greatly simplifies the task of 
developing the sorts of simulations we get with NetLogo.

For more information on the project, see ["PyCX: a Python-based simulation code repository for complex systems education"](http://casmodeling.springeropen.com/articles/10.1186/2194-3206-1-2).

&nbsp; 


## The PyCX Repository

The entire PyCX Repository is available for download through the [PyCX Project Sourceforge] (http://pycx.sourceforge.net/) page. 
You can download the entire repository or just the scripts for individual models. You can also download examples from 
our [_Introduction to the Modeling and Analysis of Complex Systems_] (http://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/) textbook we are using. You should feel free to use this code as a basis for developing your own models.

&nbsp; 

## Working with the PyCX GUI

**Notes for using the GUI**:

- Any script using the GUI, be it one in the repository or one you want to build on your own, will require the "pycxsimulator" module. The easiest way to handle this is just to make sure that there you have a copy of the "pycxsimulator.pyc" file in the same directory as your script.

- When running models that use the GUI through Spyder, you will need to make sure to use a "Python Console" (as opposed to a "Ipython Console"). 

&nbsp; 


### Template for programs using the PyCX GUI

Hiroki Sayama, the developer of PyCX and author of [_Introduction to the Modeling and Analysis of Complex Systems_] (http://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/), provides the following template for building models using the PyCX GUI on pg. 175 of the text.

	import matplotlib
	matplotlib.use('TkAgg')
	from pylab import *
	# import necessary modules
	
	# define model parameters
	
	def initialize():
		global # list global variables
		# initialize system states
	
	def observe():
		global # list global variables
		cla() # to clear the visualization space
		# visualize system states

	def update():
		global # list global variables
		# update system states for one discrete time step

	import pycxsimulator
	pycxsimulator.GUI().start(func=[initialize, observe, update])

&nbsp; 


#### Adding text to the "Info" tab
Filling out the "Info" tab of the GUI is handled using a 'docstring' in the initialize function.

	def initialize():
	'''
	This is my first PyCX simulator code.
	It simulates random motion of n particles.
	Copyright 2014 John Doe
	'''
	global xlist, ylist
	...
&nbsp; 


### Including Interactive Parameter Control

The PyCX GUI also allows for interactive parameter control through the GUI via including a "Parameter Setter" function in your model, and passing it to the pycxsimulator.GUI() to run your model. 

In the code below, just substitute your own specifications between the pointed brackets.

	def <parameter setter name> (val = <parameter name>):
		'''
		<explanation of parameter>
		<this part will be displayed when you mouse-over on parameter setter>
		'''
		global <parameter name>
		<parameter name> = int(val) # or float(val), str(val), etc.
		return val
&nbsp; 

The pass this function to the GUI function.

	pycxsimulator.GUI(parameterSetters=<list of parameter setters>).start...

