# Laptop Hardware Diagnostics

A Python-based hardware diagnostics and benchmarking project designed to
collect laptop hardware specifications and evaluate the performance of
individual hardware components.

The project combines Python with PowerShell system commands to automate
hardware information collection and run repeatable performance tests.

## Features

- Collects laptop hardware specifications and system information
- Collects battery health information
- Tests RAM read/write throughput
- Benchmarks CPU computational performance
- Benchmarks GPU computational performance
- Tests disk storage read/write performance
- Runs repeatable benchmarks and measures execution time

<!-- ## Hardware Tests

### RAM

The RAM benchmark allocates large datasets and performs memory-intensive
operations to measure memory throughput.

Measurements include:

- Memory read throughput
- Memory write throughput
- Data transfer time
- Average benchmark performance
- Performance consistency across repeated tests

### CPU

The CPU benchmark uses computational workloads to evaluate processor
performance.

Tests may include:

- Numerical calculations
- Array operations
- Matrix operations
- Single-threaded workloads
- Multi-threaded workloads
- Repeated workloads to evaluate sustained performance

### GPU

GPU performance is evaluated using PyTorch-based computational workloads.

Tests may include:

- Matrix multiplication
- Tensor operations
- GPU execution time
- CPU vs. GPU computation time
- Repeated workloads to evaluate sustained performance

### Disk Storage

Storage performance is evaluated using file I/O workloads.

Tests include:

- Sequential read speed
- Sequential write speed
- File transfer time
- Repeated read/write operations
- Storage performance consistency

### Battery

Battery information is collected using Windows PowerShell and
`powercfg` battery reports.

The project can collect information such as:

- Design capacity
- Full-charge capacity
- Battery health
- Battery information reported by Windows -->

## Technologies

### Programming Languages

- Python
- PowerShell

### Python Packages

- [NumPy](https://numpy.org/) - Numerical computing and array-based
  performance testing
- [PyTorch](https://pytorch.org/) - CPU/GPU tensor operations and
  computational benchmarking

### Other Technologies

- Python `subprocess`
- Windows PowerShell

<!-- ## Project Structure

```text
diagnostics_project/
│
├── README.md
├── requirements.txt
│
├── CPU/
│   └── ...
│
├── RAM/
│   └── ...
│
├── GPU/
│   └── ...
│
├── Disk/
│   └── ...
│
├── Battery/
│   └── ...
│
└── ... -->
