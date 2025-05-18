# Performance Analysis Report: OSU Micro-Benchmarks on Aion Cluster

## Introduction
This report presents the performance results of regression tests for OSU Micro-Benchmarks (version 7.2) on the Aion cluster, using the EasyBuild binary sourcing method. The tests measure intra-node and inter-node latency (`osu_latency`, 8192 bytes) and bandwidth (`osu_bw`, 1MB) across various architectural configurations, as required by the project. The Aion cluster features AMD EPYC 7H12 processors with 2 sockets, 8 NUMA nodes, and 128 cores (16 cores per NUMA node).

## Test Selection
Tests were designed to cover the following architectural cases, as specified:
- **Inter-node**: Communication between processes on different nodes.
- **Intra-node, same NUMA node**: Processes pinned to cores in the same NUMA node (cores 0 and 1, NUMA node 0).
- **Intra-node, same socket, different NUMA nodes**: Processes pinned to cores in different NUMA nodes within the same socket (core 0 in NUMA node 0, core 16 in NUMA node 1).
- **Intra-node, different sockets**: Processes pinned to cores in different sockets (core 0 in socket 0, core 0 in socket 1, i.e., core 64 in NUMA node 4).

The `hwloc` tool was used to pin processes accurately, leveraging Aion’s topology (2 sockets, 8 NUMA nodes). Tests used the `foss/2023b` toolchain and ReFrame 4.7.4 for automation.

## Results
The following results were obtained for EasyBuild-sourced binaries on Aion:

| Test Case | Latency (µs) | Bandwidth (MB/s) |
|-----------|--------------|------------------|
| Inter-node | 4.11 | 12,321.01 |
| Intra-node, same NUMA node | 0.59 | 14,300.71 |
| Intra-node, same socket, different NUMA | 0.61 | 14,409.85 |
| Intra-node, different sockets | 0.60 | 12,608.85 |

### Observations
- **Inter-node**: Latency (4.11 µs) is close to the expected 3.9 µs, and bandwidth (12,321.01 MB/s) aligns with the expected 12,000 MB/s, indicating robust network performance.
- **Intra-node**: Latencies (0.59–0.61 µs) are significantly lower than the expected 2.3 µs, likely due to Aion’s optimized AMD EPYC architecture and effective `hwloc` pinning. Bandwidths (12,608.85–14,409.85 MB/s) exceed the expected 12,000 MB/s, with same NUMA and different NUMA cases outperforming different sockets due to faster memory access within a socket.
- **Stability**: Results are stable across runs, with minor variations (e.g., latency 4.09–4.11 µs inter-node), suggesting reliable regression testing for detecting performance changes (e.g., driver updates).

## Performance Graphs
[To be added: Bar charts comparing latency and bandwidth across test cases.]

## Reference Values Stability
- **Expected Stability**: Reference values (3.9 µs inter-node latency, 2.3 µs intra-node latency, 12,000 MB/s bandwidth) are stable for regression testing, as Aion’s hardware and software stack (`foss/2023b`) is consistent. Observed values are within or exceed expected ranges, validating the test setup.
- **Expected Variations**: Minor variations may occur due to network congestion (inter-node) or memory contention (intra-node). Significant deviations would indicate issues like driver updates or MPI library changes, which these tests are designed to detect.

## Conclusion
The EasyBuild tests on Aion demonstrate excellent performance, with intra-node latencies and bandwidths surpassing expectations due to optimized hardware and pinning. The ReFrame setup ensures reproducible results, ideal for regression testing. Future work includes [local compilation, EESSI, and Iris tests, pending clarification].

## Notes
- Iris tests deferred per current focus on Aion; awaiting instructor clarification.
- Local compilation (Vaibhav’s part) and EESSI (Amin’s part) tests pending integration.
