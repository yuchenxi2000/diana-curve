import numpy as np
from fractions import Fraction


def to_frac(a):
    return str(Fraction(a).limit_denominator(1000))

def to_frac_tex(a):
    frac = Fraction(a).limit_denominator(1000)
    if frac.numerator < 0:
        return '-\\frac{' + str(-frac.numerator) + '}{' + str(frac.denominator) + '}'
    else:
        return '\\frac{' + str(frac.numerator) + '}{' + str(frac.denominator) + '}'


class FourierInterp:
    def __init__(self, point_array, nk):
        self.k_points = np.fft.fft(point_array)
        self.nk = nk
        self.N = self.k_points.shape[0]

    def eval(self, t):
        # $ t \in [0, 1) $
        s = np.zeros_like(t, dtype=np.complex128)
        for i in range(0, self.nk + 1):
            s += np.exp(1j * 2 * np.pi * t * i) * self.k_points[i]
        for i in range(-self.nk, 0):
            s += np.exp(1j * 2 * np.pi * t * i) * self.k_points[i + self.N]
        return s / self.N

    def gen_equation(self, t_begin):
        # 这里的t乘了2pi
        sx = ''
        sy = ''
        for i in range(1, self.nk + 1):
            Ap = self.k_points[i]
            An = self.k_points[self.N-i]
            Zr = An.imag - Ap.imag + 1j * (Ap.real + An.real)
            Zi = Ap.real - An.real + 1j * (Ap.imag + An.imag)
            phase_r = np.angle(Zr) - i * t_begin
            phase_i = np.angle(Zi) - i * t_begin
            sx += f'{to_frac(abs(Zr)/self.N)}*sin({i}*t+{to_frac(phase_r)})+'
            sy += f'{to_frac(abs(Zi)/self.N)}*sin({i}*t+{to_frac(phase_i)})+'
        sx += f'{to_frac(self.k_points[0].real / self.N)}'
        sy += f'{to_frac(self.k_points[0].imag / self.N)}'
        return sx, sy
    
    def gen_equation_tex(self, t_begin):
        # 这里的t乘了2pi
        sx = ''
        sy = ''
        for i in range(1, self.nk + 1):
            Ap = self.k_points[i]
            An = self.k_points[self.N-i]
            Zr = An.imag - Ap.imag + 1j * (Ap.real + An.real)
            Zi = Ap.real - An.real + 1j * (Ap.imag + An.imag)
            phase_r = np.angle(Zr) - i * t_begin
            phase_i = np.angle(Zi) - i * t_begin
            sx += f'{to_frac_tex(abs(Zr)/self.N)}\\sin({i if i != 1 else ""}t+{to_frac_tex(phase_r)})+'
            sy += f'{to_frac_tex(abs(Zi)/self.N)}\\sin({i if i != 1 else ""}t+{to_frac_tex(phase_i)})+'
        sx += f'{to_frac_tex(self.k_points[0].real / self.N)}'
        sy += f'{to_frac_tex(self.k_points[0].imag / self.N)}'
        return sx, sy
    
    def gen_equation_mma(self, t_begin):
        # 这里的t乘了2pi
        sx = ''
        sy = ''
        for i in range(1, self.nk + 1):
            Ap = self.k_points[i]
            An = self.k_points[self.N-i]
            Zr = An.imag - Ap.imag + 1j * (Ap.real + An.real)
            Zi = Ap.real - An.real + 1j * (Ap.imag + An.imag)
            phase_r = np.angle(Zr) - i * t_begin
            phase_i = np.angle(Zi) - i * t_begin
            sx += f'{to_frac(abs(Zr)/self.N)}*Sin[{i if i != 1 else ""}t+{to_frac(phase_r)}]+'
            sy += f'{to_frac(abs(Zi)/self.N)}*Sin[{i if i != 1 else ""}t+{to_frac(phase_i)}]+'
        sx += f'{to_frac(self.k_points[0].real / self.N)}'
        sy += f'{to_frac(self.k_points[0].imag / self.N)}'
        return sx, sy
