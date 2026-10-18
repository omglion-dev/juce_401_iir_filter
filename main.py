import numpy as np
from transposed_direct_form2_iir import TransposedDirectForm2IIR

def main():
    b = [0.0016822, 0.0033645, 0.0016822]
    a = [1., -1.96298009, 0.96365298]
    
    iir = TransposedDirectForm2IIR(b, a)
    
    x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6], dtype=np.float64)
    y = np.zeros_like(x)
    
    iir.process(x, y)
    print(y)
    
    
if __name__ == "__main__":
    main()