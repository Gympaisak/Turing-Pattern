
import numpy as np
import math

#Initial condition functions:

def InitialConditions(rows,columns,model,constants=1):
    if (model=="StandardDeviation"):
        U,V = StandardDeviation(rows,columns,constants)
    elif (model=="InitializeGrayScott"):
        U,V = InitializeGrayScott(rows,columns,constants)
    elif (model=="RandomFlip"):
        U,V = RandomFlip(rows,columns,constants)
    elif (model=="Empty"):
        U,V = Empty(rows,columns,constants)
    return U,V

def StandardDeviation(rows,columns,constants):
    #Creating the initial values of morphogen U and V in a [rows, columns] matrix for each. 
    #Each value of U and V is a standard distribution of scale standard_deviation around the centre mean_centre.
    mean_centre = 1
    standard_deviation = 0.1
    U = np.random.normal(mean_centre, standard_deviation,[rows,columns]) 
    V = np.random.normal(mean_centre, standard_deviation,[rows,columns]) #Creating the initial values of morphogen V. With a standard distribution of scale 1 around the centre 2
    return U, V

def InitializeGrayScott(rows,columns,constants):
    U = np.ones([rows,columns])
    V = np.zeros([rows,columns])
    chance = 2
    for i in range(0,rows):
        for j in range(0,columns):
            if (np.random.randint(0,100)<chance):
                V[i,j] = 1
    
    return U ,V

def RandomFlip(rows, columns, constants):
    """Creates two matrices for the two morphogens U and V with the 
        initial conditions that V = 1 and U = 0 in about val%
        of the cells, and U = 1 and V = 0 in the rest of the cells"""

    U = np.zeros((rows, columns))  # U matrix filles with zeros
    V = np.zeros((rows, columns))  # V matrix filles with zeros

    val = 5
    for r in range(rows):
        for c in range(columns):
            """Setting the initial condition on the matrices U and V so that (100-val)% of the cells
                contains U = 1 and V = 0 and val % of the cells contains U = 0 and V = 0"""
            U[r, c] = 1
            V[r, c] = 0

            if (np.random.randint(0, 100) < val):
                U[r, c] = 0
                V[r, c] = 1
    

    return U, V

def Empty(rows, columns, constants):
    U = np.zeros((rows, columns))  # U matrix filles with zeros
    V = np.zeros((rows, columns))  # V matrix filles with zeros
    
    return U, V









#Reaction diffusion models:

def ReactionDiffusionFunction(U,V,model,reactionDiffusionConstants):
    if (model=="Schnakenberg"):
        deltaU, deltaV = Schnakenberg(U,V,reactionDiffusionConstants)
    elif (model=="GiererMeinhardt"):
        deltaU, deltaV = GiererMeinhardt(U,V,reactionDiffusionConstants)
    elif (model=="angelfishPomacanthus"):
        deltaU, deltaV = angelfishPomacanthus(U,V,reactionDiffusionConstants)
    elif (model=="GrayScott"):
        deltaU, deltaV = GrayScott(U,V,reactionDiffusionConstants)
    elif (model=="Linear"):
        deltaU, deltaV = Linear(U,V,reactionDiffusionConstants)
    return deltaU, deltaV


def  Schnakenberg(U,V,reactionDiffusionConstants):
    if (reactionDiffusionConstants == 1):
        c1 = 0.1; c2 = 0.9; cm1 = 1; c3 = 1; DU = 1; DV = 40

    f = c1 - cm1*U + c3*U*U*V
    g = c2 - c3*U*U*V
    
    deltaU = DU*Laplacian(U) + f
    deltaV = DV*Laplacian(V) + g
    
    return deltaU,deltaV


def GiererMeinhardt(U,V,reactionDiffusionConstants):
    c1 = 1; c2 = 1; c3 = 1; c4 = 1;c5 = 1; k  = 1; DU = 1; DV = 1
    
    f = c1 - c2*U + c3*(U*U/((1+k*U*U)*V))
    g = c4*U*U - c5*V
    
    deltaU = DU*Laplacian(U) + f
    deltaV = DV*Laplacian(V) + g
    
    return deltaU,deltaV


def angelfishPomacanthus(U,V,reactionDiffusionConstants):
    c1 = 0.08; c2 = -0.08; c3 = 0.05; ga = 0.03; c4 = 0.1; c5 = -0.15; gl = 0.06; DU = 0.007; DV = 0.03
    
    f = c1*U + c2*V + c3 - ga*U
    g = c4*U + c5 - gl*V
    
    
    deltaU = DU*Laplacian(U) + f
    deltaV = DV*Laplacian(V) + g
    
    return deltaU,deltaV



def GrayScott(U,V,reactionDiffusionConstants):
    #U=A, V=B. I think this means that V will create the pattern.
    #F = 0.062; k = 0.063; DU = 0.06; DV = 0.12 #Just made a homogeanous spread of U I think.
    #F = 0.062; k = 0.063; DU = 0.20; DV = 0.10 #Same as above
    #F = 0.062; k = 0.063; DU = 0.10; DV = 0.20 #Same as above
    #F = 0.55; k = 0.62; DU = 0.5; DV = 1 #Taken from https://www.karlsims.com/rd.html
    if (reactionDiffusionConstants==1):
        F = 0.055; k = 0.062; DU = 1; DV = 0.5 #Realised that the convolution worked differerntly. Taken from https://www.karlsims.com/rd.html
    
    f = -U*V*V + F*(1-U)
    g = U*V*V - (F+k)*V
    
    convolutedU = GrayScottConvolution(U)
    convolutedV = GrayScottConvolution(V)
    
    deltaU = DU*convolutedU + f
    deltaV = DV*convolutedV + g
    
    return deltaU,deltaV



def Linear(U, V,reactionDiffusionConstans):
    if (reactionDiffusionConstans==1):
        a = 1.5; b = -2; c = 2; d = -2 ; DU = 1; DV = 40 #Amandas constants?
    elif (reactionDiffusionConstans==2): #Trying to use Alan Turings constants.
        # I=1, N=10, p=1 fick jag mönster för men värdena blev enorma.
        # I=1, N=1, p=1 Mönstret blev mindre med N mindre. Jag fick mönster men värdena blev enorma.
        # I=3, N=10, p=1 fick jag mönster för men värdena blev INF!
        # I=1, N=10, p=4 Mönstret blev mindre med större p. fick jag mönster för men värdena blev enorma.
        I = 1
        N = 10 #ska va antal celler i ringen?
        p = 1 #Ska vara radien på ringen?

        a = I - 2
        b = 2.5
        c = -1.25
        d = I + +1.5
        DUprick = 1
        DVprick = 1/2
        DU = (N/(2*math.pi*p))**(2)*DUprick
        DV = (N/(2*math.pi*p))**(2)*DVprick

    elif (reactionDiffusionConstans==3):
        DU = 1/4
        DV = 1/4
        a = 1
        b = 1
        c = 1
        d = a


    #a = 1; b = 1; c = b; d = a; DU = 1/4; DV = 1/4 #Makes no pattern and the concentration of U increases exponentially
    #a = 1; b = 1; c = -b; d = a; DU = 1/4; DV = 1/4  #Same as above
    
    f = a*U + b*V
    g = c*U + d*V
    
    deltaU = DU*Laplacian(U) + f
    deltaV = DV*Laplacian(V) + g
    
    return deltaU,deltaV


# Calculating the laplacian functions:

def Laplacian(U):
    [r,c] = np.shape(U) #[r,c] is the number of rows and columns in the matrix/array U.
    
    ordning_UH = np.linspace(1,c-1,c-1, dtype=np.int32) #if for example c=5 -> ordning_UH = [1,2,3,4]
    ordning_UH = np.append(ordning_UH,0) # Adds a 0 at the end. If for example c=5 -> ordning_UH = [1,2,3,4,0]
    
    ordning_UV = np.linspace(0,c-2,c-1, dtype=np.int32) #if for example c=5 -> ordning_UV = [0,1,2,3]
    ordning_UV = np.concatenate([[c-1],ordning_UV]) #Adds a c-1 to the start. If for example c=5 -> ordning_UH = [4,0,1,2,3]
    
    if (r==c):
        ordning_UN = ordning_UH
        ordning_UU = ordning_UV
    else:
        ordning_UN = np.linspace(1,r-1,r-1, dtype=np.int32) #if for example r=5 -> ordning_UH = [1,2,3,4]
        ordning_UN = np.append(ordning_UN,0)# Adds a 0 at the end. If for example r=5 -> ordning_UH = [1,2,3,4,0]
        
        ordning_UU = np.linspace(0,r-2,r-1, dtype=np.int32) #if for example r=5 -> ordning_UV = [0,1,2,3]
        ordning_UU = np.concatenate([[r-1],ordning_UU]) #Adds a r-1 to the start. If for example r=5 -> ordning_UH = [4,0,1,2,3]
    
    """
    If U = [1,2,3] Then UH = [2,3,1], UV = [3,1,2], UN = [4,5,6], UU = [7,8,9]
           [4,5,6]           [5,6,4]       [6,4,5]       [7,8,9]       [1,2,3]
           [7,8,9]           [8,9,7]       [9,7,8]       [1,2,3]       [4,5,6]
    """
    
    UH = U[:,ordning_UH]
    UV = U[:,ordning_UV]    
    UN = U[ordning_UN,:]
    UU = U[ordning_UU,:]
    #print(UU)
    
    laplacianU = UH + UV + UN + UU -4*U
    return laplacianU


def GrayScottConvolution(U):
    [r,c] = np.shape(U) #[r,c] is the number of rows and columns in the matrix/array U.
    
    ordning_UH = np.linspace(1,c-1,c-1, dtype=np.int32) #if for example c=5 -> ordning_UH = [1,2,3,4]
    ordning_UH = np.append(ordning_UH,0) # Adds a 0 at the end. If for example c=5 -> ordning_UH = [1,2,3,4,0]
    
    ordning_UV = np.linspace(0,c-2,c-1, dtype=np.int32) #if for example c=5 -> ordning_UV = [0,1,2,3]
    ordning_UV = np.concatenate([[c-1],ordning_UV]) #Adds a c-1 to the start. If for example c=5 -> ordning_UH = [4,0,1,2,3]
    
    if (r==c):
        ordning_UN = ordning_UH
        ordning_UU = ordning_UV
    else:
        ordning_UN = np.linspace(1,r-1,r-1, dtype=np.int32) #if for example r=5 -> ordning_UH = [1,2,3,4]
        ordning_UN = np.append(ordning_UN,0)# Adds a 0 at the end. If for example r=5 -> ordning_UH = [1,2,3,4,0]
        
        ordning_UU = np.linspace(0,r-2,r-1, dtype=np.int32) #if for example r=5 -> ordning_UV = [0,1,2,3]
        ordning_UU = np.concatenate([[r-1],ordning_UU]) #Adds a r-1 to the start. If for example r=5 -> ordning_UH = [4,0,1,2,3]
    
    """
    If U = [1,2,3] Then UH = [2,3,1], UV = [3,1,2], UN = [4,5,6], UU = [7,8,9], UUH = [8,9,7], UUV = [9,7,8], UNH = [5,6,4], UNV = [6,4,5]
           [4,5,6]           [5,6,4]       [6,4,5]       [7,8,9]       [1,2,3]        [2,3,1]        [3,1,2]        [8,9,7]        [9,7,8]
           [7,8,9]           [8,9,7]       [9,7,8]       [1,2,3]       [4,5,6]        [5,6,4]        [6,4,5]        [2,3,1]        [3,1,2]
    """
    
    UH = U[:,ordning_UH]
    UV = U[:,ordning_UV]    
    UN = U[ordning_UN,:]
    UU = U[ordning_UU,:]
    UUH = UU[:,ordning_UH]
    UUV = UU[:,ordning_UV]
    UNH = UN[:,ordning_UH]
    UNV = UN[:,ordning_UV]
    #print(UU)
    
    convolutedU = 0.2*UH + 0.2*UV + 0.2*UN + 0.2*UU + 0.05*UUH + 0.05*UUV + 0.05*UNH + 0.05*UNV -U
    return convolutedU


def Create(rows, columns, val=5):
    """Creates two matrices for the two morphogens U and V with the 
        initial conditions that V = 1 and U = 0 in about val%
        of the cells, and U = 1 and V = 0 in the rest of the cells"""

    U = np.zeros((rows, columns))  # U matrix filles with zeros
    V = np.zeros((rows, columns))  # V matrix filles with zeros
    Unext = np.zeros((rows, columns)) # temporary matrix for U
    Vnext = np.zeros((rows, columns)) # temporary matrix for V

    for r in range(rows):
        for c in range(columns):
            """Setting the initial condition on the matrices U and V so that (100-val)% of the cells
                contains U = 1 and V = 0 and val % of the cells contains U = 0 and V = 0"""
            U[r, c] = 1
            V[r, c] = 0

            if np.random.randint(0, 100) < val:
                U[r, c] = 0
                V[r, c] = 1
    

    return U, V, Unext, Vnext


def MSE(U, Unext):
    """Function that stops loop when mean-square-error
    between twop time steps is less than 5e-11,
    and makes an array to store the MSE values"""
    
    m = np.square(np.subtract(U,Unext)).mean()  # computes mean square error between U and Unext

    if m < (10**-10):
        #print(MSElist)
        # If mean square value 'm' is less then 5e-11 the computation stops
        return False, m

    else:
        return True, m

