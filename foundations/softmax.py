import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z_max = np.max(z)
        ans = np.exp(z - z_max) / np.sum(np.exp(z - z_max))

        return np.round(ans, decimals=4, out=z)