#!/bin/bash

# Script to run OSU benchmarks with ReFrame and display results
echo "============================================================="
echo "Starting OSU Benchmarks with ReFrame"
echo "============================================================="

# Clean up directories
echo -e "\nCleaning up previous directories...\n------------------------------------"
rm -rf __pycache__/ stage/ output/
echo "Cleanup completed."

# Clear all loaded modules
module -f purge

# Load required modules
module load env/release/2023b toolchain/foss/2023b system/hwloc

# Run ReFrame with OSU benchmarks, explicitly using 1 node
echo -e "\nRunning ReFrame job...\n------------------------------------"
srun --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 --nodes=1 bash -c 'unset SLURM_CPU_BIND SLURM_CPU_BIND_TYPE SLURM_CPU_BIND_VERBOSE SLURM_CPU_BIND_LIST; module load devel/ReFrame/4.7.4-GCCcore-13.2.0 && reframe -C reframe_config.py -c osu_benchmarks.py -r'
echo -e "\n------------------------------------\nReFrame job completed.\n"

# Display output files for OSU benchmark tests with separators
echo "============================================================="
echo "OSU Benchmark Results"
echo "============================================================="

echo -e "\nOSU Bandwidth Test (Different Socket):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSUBandwidthTestDiffSocket/rfm_job.out

echo -e "\nOSU Latency Test (Different Socket):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSULatencyTestDiffSocket/rfm_job.out

echo -e "\nOSU Bandwidth Test (Inter Node):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSUBandwidthTestInterNode/rfm_job.out

echo -e "\nOSU Latency Test (Inter Node):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSULatencyTestInterNode/rfm_job.out

echo -e "\nOSU Bandwidth Test (Same NUMA):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSUBandwidthTestSameNuma/rfm_job.out

echo -e "\nOSU Latency Test (Same NUMA):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSULatencyTestSameNuma/rfm_job.out

echo -e "\nOSU Bandwidth Test (Same Socket, Different NUMA):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSUBandwidthTestSameSocketDiffNuma/rfm_job.out

echo -e "\nOSU Latency Test (Same Socket, Different NUMA):\n------------------------------------"
cat output/aion/batch/foss-2023b/OSULatencyTestSameSocketDiffNuma/rfm_job.out

echo -e "\n============================================================="
echo "OSU Benchmarks Completed"
echo "============================================================="
