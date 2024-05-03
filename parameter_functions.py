import numpy as np

class ParameterClass:
    def __init__(self, choice):
        if (choice == "AmandaSchnackenberg"):
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "RandomFlip" #For the shnackenberg model. Amandas initial condition.
            
            #Choosing reaction diffusion model and its constants
            self.reactionDiffusionModel = "Schnakenberg"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 0.001           # time step size
            self.tmax = 300           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=10 #Frames per second.
            self.sped_up = 3 #How much the animation is sped up in comparison to real time.

        elif (choice == "IsakSchnackenberg"):
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "StandardDeviation" #For the shnackenberg model. Isaks initial condition.

            self.reactionDiffusionModel = "Schnakenberg"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 0.001           # time step size
            self.tmax = 100           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=10 #Frames per second.
            self.sped_up = 3 #How much the animation is sped up in comparison to real time.


        elif (choice == "GrayScott1"):
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "InitializeGrayScott" #For the gray Scott model.

            self.reactionDiffusionModel = "GrayScott"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 1           # time step size
            self.tmax = 600           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps =10 #Frames per second.
            self.sped_up = 25 #How much the animation is sped up in comparison to real time.


        elif (choice == "GrayScott2"): #Only changed the animation constants and made tmax slightly bigger compared to "GrayScott1"
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "InitializeGrayScott" #For the gray Scott model.

            self.reactionDiffusionModel = "GrayScott"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 1           # time step size
            self.tmax = 600           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=1 #Frames per second.
            self.sped_up = 50 #How much the animation is sped up in comparison to real time.
        
        elif (choice == "angelfishPomacanthus1"): 
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "StandardDeviation" #For the gray Scott model.

            self.reactionDiffusionModel = "angelfishPomacanthus"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 0.01           # time step size
            self.tmax = 600           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=1 #Frames per second.
            self.sped_up = 50 #How much the animation is sped up in comparison to real time.
        
        elif (choice == "angelfishPomacanthus2"): #Uses another initial condition
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "RandomFlip" #For the gray Scott model.

            self.reactionDiffusionModel = "angelfishPomacanthus"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 0.001           # time step size
            self.tmax = 600           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=1 #Frames per second.
            self.sped_up = 50 #How much the animation is sped up in comparison to real time.
        
        elif (choice == "TuringLinear"): 
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "StandardDeviation" #For the gray Scott model.

            self.reactionDiffusionModel = "Linear"; self.reactionDiffusionConstants = 3

            # time parameters
            self.dt = 0.01           # time step size
            self.tmax = 10           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=1 #Frames per second.
            self.sped_up = 50 #How much the animation is sped up in comparison to real time.

        elif (choice == "TuringLinearAmanda"): 
            #initial condition parameters
            self.rows = 50; self.columns = 50; self.initialModel = "StandardDeviation" #For the gray Scott model.

            self.reactionDiffusionModel = "Linear"; self.reactionDiffusionConstants = 1

            # time parameters
            self.dt = 0.01           # time step size
            self.tmax = 10           # end time. TO DO: equilibrium is reached after 75 sec
            self.steps = int(self.tmax / self.dt)+1 # number of time steps 
            self.time = np.linspace(0, self.tmax, self.steps)  # array of time steps

            # constant concerning the time limit when the pattern no longer change form
            self.trueTime = False       # set to True if pattern should evolve until t = tmax

            # Parameters used in the animation code.
            self.fps=1 #Frames per second.
            self.sped_up = 50 #How much the animation is sped up in comparison to real time.