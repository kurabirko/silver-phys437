from math import pi
from qiskit.circuit.library import QFT, CPhaseGate
from qiskit.extensions import UnitaryGate

from math import pi
import numpy as np

def iQFT(num_qubits=0):    
    return QFT(num_qubits, inverse=True)\
        .reverse_bits()\
        .to_gate(label='iQFT')

U =  CPhaseGate(2*pi*0.333984375, label = 'U')

def CUPowFactory(U):
    def CUPow(exponent):
        return U.power(exponent=2**exponent).control(1)
    return CUPow
