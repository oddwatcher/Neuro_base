import numpy as np
from tqdm import tqdm

#First pass of this program we only foucos on 

class actfunc():
    # This Class describes the activation function together with the differentials
    def relu(s,din):
        if din >= 0:
            if din > 1:
                return 1
            return din
        else:
            return 0

    def relu_d(s,pos):
        if pos > 0:
            return 1
        else:
            return 0

    def leaky_relu(s, din):
        if din < 0:
            out = s.leaky_relu_k*din
        else:
            out = din

        if out > 1:
            out = 1
        if out < -1:
            out = -1
        return out

    def Leaky_relu_d(s, pos):
        if pos < 0:
            return s.leaky_relu_k
        else:
            return 1

    def __init__(self, type:str, **kargs) -> None:
        # actfunc are relu , leaky_relu. if Using leaky_relu specify k = 0
        # After init use self.actfunc to call the corrisponding func and self.diff to get differental
        match type:
            case "relu":
                self.actfunc = self.relu
                self.diff = self.relu_d

            case "leaky_relu":
                if "k" in kargs:
                    self.leaky_relu_k = float(kargs["k"])
                else:
                    self.leaky_relu_k = 0
                self.actfunc = self.leaky_relu
                self.diff = self.Leaky_relu_d
    
class lossfunc():
    def MSE(s,din,target):
        pass
        


class neuron():
    actfunc_type = "relu"
    def __init__(self,actifunc:actfunc,lossfunc:lossfunc,**inputs) -> None:
        pass
    
    
    
