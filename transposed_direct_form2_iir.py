import numpy as np

class TransposedDirectForm2IIR:
    def __init__(self, b_coeffs, a_coeffs):
        """
        Transposed Direct Form II IIR Filter
        :param b_coeffs: feedforward coefficients (b0, b1, b2)
        :param a_coeffs: feedback coefficients (a0=1, a1, a2)
        """
        # 私有状态变量，对应原来的 s_1, s_2
        self._s1 = 0.0
        self._s2 = 0.0
        self._b = np.array(b_coeffs, dtype=np.float64)
        self._a = np.array(a_coeffs, dtype=np.float64)

    def process(self, x: np.ndarray, y: np.ndarray):
        """
        x: input array
        y: output array (pre-allocated, same length as x)
        """
        for i in range(len(x)):
            x0 = x[i]
            y0 = self._b[0] * x0 + self._s1
            self._s1 = self._b[1] * x0 + self._s2 - self._a[1] * y0
            self._s2 = self._b[2] * x0 - self._a[2] * y0
            y[i] = y0

    def reset(self):
        """Reset filter internal state, clear s1, s2"""
        self._s1 = 0.0
        self._s2 = 0.0
