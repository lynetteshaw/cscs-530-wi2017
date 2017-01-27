
# **Incorporating Randomness into ABM**
## 1/27/2017
&nbsp;


As has been mentioned, one of the major advantages of an ABM approach is its amenability to modeling stochastic processes, specifically those involving a large number of variables (e.g. as is the case when looking at the probabilistic interactions of many hetergeneous individuals). 
Knowing how to incorporate randomness into an ABM in an informed and principled fashion is an important part of creating good models of complex systems. Some understanding of _**pseudo-randomness**_ , _**basic probability distributions**_ , and the _**Monte Carlo method**_ is thus a necessary part of knowing how to build and analyze ABMs.

&nbsp;

## Where Randomness and Probability get Incoporated

### *__Initialization__*
Given the degree to which complex systems can be characterized by their *__sensitivity to variations in initial conditions__*, incorporation of randomness in the initialization of individual ABM runs is an important tool for parsing out how strongly coupled particular emergent outcomes are to particular starting states. 

Randomness during initialization can also be thought of as helping modelers avoid imposing unnecessarily strong assumptions in their models by allowing systems to start in more "uninformed" states.

###  *__Interaction__*
Another characteristic aspect of complex systems is the degree to which *__noise in interactions__* between agents and/or the environment can play a role in _generating_ emergent order. In order to get at this "noisiness" in interactions, ABM allows modelers to make use of probabilistic (i.e. non-deterministic) inputs and rules at the individual level.  

Consequently, having a clear understanding of the sorts of underlying distributions you expect to matter for the types of rules and inputs you are interested in modeling is an important of ABM design.

### *__Analysis__*
Per the non-deterministic nature of most ABM, individual runs of a model at the same parameter settings often end up with quite different outcomes. Because of this, single ABM runs are insufficient to accurately characterize and analyze the relationship between system parameters and system outcomes. Instead, we rely on the logic of *__Monte Carlo__* simulation methods to be able to disentangle the fundamental features of systems parameterized in a particular way and the idiosyncratic features of individual instantations of them.
