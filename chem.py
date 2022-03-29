from time import time
import matplotlib.pyplot as plt
import pennylane as qml
from numpy import complex128
from pennylane.ops.qubit import PauliX, PauliZ
from qiskit import *
from pennylane import numpy as np

class Finance:
    def __init__(self, time_step, total_qubit):
        self.time_step = time_step
        self.total_qubit = total_qubit

        self.cost_history = []


    def Create_Gp(self):
        pass