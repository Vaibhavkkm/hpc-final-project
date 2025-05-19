# OSU Micro-Benchmarks Performance Report

## Overview
This repository contains the performance results of the OSU Micro-Benchmarks executed on the Aion cluster using ReFrame 4.7.4. The benchmarks evaluate latency and bandwidth across various configurations, including same NUMA, same socket different NUMA, different sockets, and inter-node setups.

## Test Environment
- **Cluster**: Aion
- **Partition**: batch
- **Compiler toolchain**: gompi-2023b
- **ReFrame Version**: 4.7.4
- **Date**: May 19, 2025
- **Latency test**: message size = 8192 bytes
- **Bandwidth test**: message size = 1,048,576 bytes (1MB)
## Performance Results

### Latency Tests
| Test Case                        | Latency (μs) | Reference (μs)    |
|----------------------------------|--------------|-------------------|
| OSULatencyTestSameNuma           | 0.57         | 0.57 ± 0.1        |
| OSULatencyTestSameSocketDiffNuma | 0.59         | 0.59 ± 0.1        |
| OSULatencyTestDiffSocket         | 0.58         | 0.58 ± 0.1        |
| OSULatencyTestInterNode          | 4.75         | 4.75 ± 0.1        |

### Bandwidth Tests
| Test Case                           | Bandwidth (MB/s) | Reference (MB/s)    |
|-------------------------------------|------------------|---------------------|
| OSUBandwidthTestSameNuma            | 14781.65         | 14781.65 ± 0.1      |
| OSUBandwidthTestSameSocketDiffNuma  | 14245.88         | 14245.88 ± 0.1      |
| OSUBandwidthTestDiffSocket          | 14333.54         | 14333.54 ± 0.1      |
| OSUBandwidthTestInterNode           | 12323.91         | 12323.91 ± 0.1      |

## Notes
- All tests passed successfully within the specified reference bounds.
- Debug logs were not visible in the output, likely due to ReFrame's logging configuration.
- A stalling issue from earlier runs was resolved by unsetting Slurm CPU binding variables and ensuring proper resource allocation.

## Repository Contents
- **report.md**: Detailed performance report (this content in markdown format).
- **scripts/**: ReFrame scripts used for running the benchmarks (if applicable).
- **logs/**: Placeholder for any available log files (if generated).

## Usage
To reproduce the results:
1. Set up ReFrame 4.7.4 in the foss-2023b environment on the Aion cluster.
2. Configure the batch partition and unset Slurm CPU binding variables.
3. Run the OSU Micro-Benchmarks using the provided ReFrame scripts.
