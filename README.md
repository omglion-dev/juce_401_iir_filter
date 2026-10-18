# Transposed Direct Form II IIR Filter
Python class implementation of a 2nd-order IIR filter using Transposed Direct Form II topology, for audio DSP coursework.

## Overview
This implementation refactors the original global-variable based `iir_filter()` function into an object-oriented Python class. Internal filter state variables are defined as private members following Python conventions.

The example coefficients are calculated for a 200 Hz Butterworth lowpass filter with sampling rate 48 kHz.

## File
`TransposedDirectForm2IIR.py`

## Dependencies
- Python 3.8+
- NumPy

## How to run
```bash
python main.py
```
