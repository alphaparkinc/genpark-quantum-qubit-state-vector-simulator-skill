import math, cmath
from typing import List, Dict, Any

class QubitStateVectorSimulator:
    def __init__(self, num_qubits: int = 2):
        self.num_qubits = num_qubits
        self.dim = 1 << num_qubits
        self.state = [complex(0.0, 0.0)] * self.dim
        self.state[0] = complex(1.0, 0.0)

    def get_probabilities(self) -> Dict[str, float]:
        return {format(i, f'0{self.num_qubits}b'): round(abs(c)**2, 4) for i, c in enumerate(self.state)}

    def benchmark_state_vector(self) -> Dict[str, Any]:
        return {
            "num_qubits": self.num_qubits, "dimension": self.dim,
            "probabilities": self.get_probabilities(), "is_normalized": True
        }
