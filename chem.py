from time import time
import matplotlib.pyplot as plt
import pennylane as qml
from numpy import complex128
from pennylane.ops.qubit import PauliX, PauliZ
from qiskit import *
from pennylane import numpy as np

class chemsitry:
    def __init__(self, time_step, total_qubit):
        self.time_step = time_step
        self.total_qubit = total_qubit

        self.cost_history = []


    def GHZ_state_prep(self):
        qml.Hadamard(wires=2)
        qml.CNOT(wires=(2,3))
        qml.SWAP(wires = (1,3))
    
    def givens_rotation(self, wire_index):
        qml.IsingXX(wires= (wire_index, wire_index+1))
        qml.IsingYY(wires=(wire_index, wire_index +1))

    def perfect_pairing(self):
        pass