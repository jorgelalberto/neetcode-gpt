import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z = 1/ (1 + np.exp(-z))
        return np.round(z, decimals=5, out=z)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.maximum(z, 0)