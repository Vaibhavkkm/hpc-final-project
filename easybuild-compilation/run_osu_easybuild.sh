#!/bin/bash

# Script to run OSU EasyBuild benchmarks with ReFrame and display results
echo "============================================================="
echo "Starting OSU EasyBuild Benchmarks with ReFrame"
echo "============================================================="

# Detect system (e.g., aion or iris) based on hostname
HOSTNAME=$(hostname -f)
if [[ $HOSTNAME =~ ^aion-cluster ]] || [[ $HOSTNAME =~ ^aion-[0-9]+ ]]; then
    SYSTEM="aion"
elif [[ $HOSTNAME =~ ^iris-cluster ]] || [[ $HOSTNAME =~ ^iris-[0-9]+ ]]; then
    SYSTEM="iris"
else
    echo "Error: Unknown system (hostname: $HOSTNAME). Expected aion-cluster, aion-<number>, iris-cluster, or iris-<number>."
    exit 1
fi

echo "Running on system: $SYSTEM"

# Clean up directories
echo -e "\nCleaning up previous directories...\n------------------------------------"
rm -rf output/ stage/
echo "Cleanup completed."

# Clear all loaded modules
module -f purge

# Load required modules
module load env/release/2023b toolchain/foss/2023b system/hwloc devel/ReFrame/4.7.4-GCCcore-13.2.0

# Unset SLURM variables
unset SLURM_CPUS_PER_TASK SLURM_TRES_PER_TASK

# Run ReFrame with EasyBuild tests, using the detected system
echo -e "\nRunning EasyBuild job...\n------------------------------------"
reframe -C ~/.reframe/settings.py -c tests/easybuild -r --system="$SYSTEM" --keep-stage-files
echo -e "\n------------------------------------\nReFrame job completed.\n"

# Display output files for OSU EasyBuild benchmark tests with separators
echo "============================================================="
echo "OSU EasyBuild Benchmark Results"
echo "============================================================="

echo -e "\nOSUBandwidthEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSUBandwidthEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSULatencyEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSULatencyEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSUBandwidthIntraNodeDiffNumaEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSUBandwidthIntraNodeDiffNumaEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSULatencyIntraNodeDiffNumaEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSULatencyIntraNodeDiffNumaEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSUBandwidthIntraNodeDiffSocketsEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSUBandwidthIntraNodeDiffSocketsEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSULatencyIntraNodeDiffSocketsEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSULatencyIntraNodeDiffSocketsEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSUBandwidthIntraNodeSameNumaEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSUBandwidthIntraNodeSameNumaEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\nOSULatencyIntraNodeSameNumaEasyBuildTest:\n------------------------------------"
cat output/$SYSTEM/batch/foss-2023b/OSULatencyIntraNodeSameNumaEasyBuildTest/rfm_job.out
echo -e "\n------------"

echo -e "\n============================================================="
echo "OSU EasyBuild Benchmarks Completed"
echo "============================================================="
