Copyright (C) 2025 Vaibhav KKM

This file is part of did-tesla-msft-fed-hike (https://github.com/Vaibhavkkm/hpc-final-project)

# Performance Analysis Report: OSU Micro-Benchmarks on Aion Cluster

## Introduction
This repository contains the performance analysis results of regression tests for OSU Micro-Benchmarks (version 7.2) conducted on the Aion cluster. The tests evaluate intra-node and inter-node latency (`osu_latency`, 8192 bytes) and bandwidth (`osu_bw`, 1MB) across various architectural configurations using three binary sourcing methods: **Local-compilation**, **EasyBuild**, and **EESSI**. The Aion cluster is equipped with AMD EPYC 7H12 processors, featuring 2 sockets, 8 NUMA nodes, and 128 cores (16 cores per NUMA node).

The results below provide insights into the performance of MPI communication under different scenarios, including same core, same NUMA node, same socket but different NUMA nodes, different sockets, and inter-node communication.

## Results Summary
The table below summarizes the bandwidth (MB/s) and latency (µs) results for Local-compilation, EasyBuild, and EESSI across common test cases.

| Test Case                      | Local-compilation Bandwidth (MB/s) | Local-compilation Latency (µs) | EasyBuild Bandwidth (MB/s) | EasyBuild Latency (µs) | EESSI Bandwidth (MB/s) | EESSI Latency (µs) |
|--------------------------------|------------------------------------|--------------------------------|----------------------------|------------------------|-------------------------|--------------------|
| Inter Node                     | 8687.79                            | 4.85                           | 12118.41                   | 3.92                   | 12106.19                | 3.92               |
| Same Socket, Different NUMA    | 16738.06                           | 1.87                           | 18606.22                   | 2.02                   | 14011.05                | 1.83               |
| Different Socket               | 17260.57                           | 4.22                           | 18153.15                   | 1.92                   | N/A                     | N/A                |
| Same NUMA                      | 16815.12                           | 1.92                           | 18696.45                   | 2.01                   | 17396.05                | 1.85               |

## Local-compilation Results
The following results were obtained using the Local-compilation binary sourcing method on the Aion cluster.

### OSU Bandwidth Test (Inter Node)
- **Size**: 1048576 bytes
- **Bandwidth**: 8687.79 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Inter Node)
- **Size**: 8192 bytes
- **Latency**: 4.85 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same Socket, Different NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 16738.06 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same Socket, Different NUMA)
- **Size**: 8192 bytes
- **Latency**: 1.87 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Different Socket)
- **Size**: 1048576 bytes
- **Bandwidth**: 17260.57 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Different Socket)
- **Size**: 8192 bytes
- **Latency**: 4.22 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 16815.12 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same NUMA)
- **Size**: 8192 bytes
- **Latency**: 1.92 µs
- **Datatype**: MPI_CHAR

## EasyBuild Results
The following results were obtained using the EasyBuild binary sourcing method on the Aion cluster.

### OSU Bandwidth Test (Inter Node)
- **Size**: 1048576 bytes
- **Bandwidth**: 12118.41 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Inter Node)
- **Size**: 8192 bytes
- **Latency**: 3.92 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same Socket, Different NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 18606.22 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same Socket, Different NUMA)
- **Size**: 8192 bytes
- **Latency**: 2.02 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Different Socket)
- **Size**: 1048576 bytes
- **Bandwidth**: 18153.15 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Different Socket)
- **Size**: 8192 bytes
- **Latency**: 1.92 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 18696.45 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same NUMA)
- **Size**: 8192 bytes
- **Latency**: 2.01 µs
- **Datatype**: MPI_CHAR

## EESSI Results
The following results were obtained using the EESSI binary sourcing method on the Aion cluster.

### OSU Bandwidth Test (Inter Node)
- **Size**: 1048576 bytes
- **Bandwidth**: 12106.19 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Inter Node)
- **Size**: 8192 bytes
- **Latency**: 3.92 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same Socket, Different NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 14011.05 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same Socket, Different NUMA)
- **Size**: 8192 bytes
- **Latency**: 1.83 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same NUMA)
- **Size**: 1048576 bytes
- **Bandwidth**: 17396.05 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same NUMA)
- **Size**: 8192 bytes
- **Latency**: 1.85 µs
- **Datatype**: MPI_CHAR

### OSU Bandwidth Test (Same Core)
- **Size**: 1048576 bytes
- **Bandwidth**: 13949.16 MB/s
- **Datatype**: MPI_CHAR

### OSU Latency Test (Same Core)
- **Size**: 8192 bytes
- **Latency**: 1.81 µs
- **Datatype**: MPI_CHAR

## Instructions to Run the Benchmarks
Follow these steps to reproduce the OSU Micro-Benchmarks on the Aion or Iris cluster:

1. **Log in to the Cluster**
   - Connect to the Aion or Iris cluster using SSH.

2. **Create a Working Directory**
   ```bash
   mkdir <folder_name>
   cd <folder_name>
   ```

3. **Clone the Repository**
   - Clone the repository containing the benchmark scripts:
   ```bash
   git clone <ssh-git-link>
   ```

4. **Navigate to the Desired Benchmark Directory**
   - Choose one of the benchmark directories (`local-compilation`, `easybuild`, or `eessi`):
   ```bash
   cd <folder_name>/<benchmark_directory>
   ```

5. **Run the Benchmark Script**
   - Locate the `.sh` script in the directory and execute it:
   ```bash
   bash <script_name>.sh
   ```

6. **Record the Results**
   - Note down the output results for `osu_latency` and `osu_bw` tests for analysis.

## Notes
- Ensure you have the necessary permissions to access the Aion/Iris cluster and execute the benchmark scripts.
- The scripts are configured to run OSU Micro-Benchmarks version 7.2 with the specified parameters (8192 bytes for latency, 1MB for bandwidth).
- Results may vary slightly due to cluster load or network conditions at the time of execution.
- The Same Core test case is exclusive to EESSI results and is not available in the Local-compilation or EasyBuild results.
- EESSI results for the Different Socket test case were not provided in the latest data and are marked as N/A in the summary table.
