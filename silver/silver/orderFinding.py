from qiskit.extensions import UnitaryGate
from qiskit.circuit.add_control import add_control
import numpy as np

_array = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, -0.4762382+0.87931631j]]
)

U = UnitaryGate(_array, label='U')
CU = add_control(U,1,label='', ctrl_state=1)

def Ux(x,N):

    k=1
    while(N>2**k):
        k=k+1
        
    u = np.zeros([2**k, 2**k], dtype = int) 

    for i in range(N):
        u[x*i%N][i]=1
    for i in range(N,2**k):
        u[i][i]=1
        

    return add_control(UnitaryGate(u,label=f'Ux({x},{N})' ),1, label='', ctrl_state=1)

