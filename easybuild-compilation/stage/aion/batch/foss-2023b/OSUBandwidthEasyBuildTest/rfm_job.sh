#!/bin/bash
#SBATCH --job-name="rfm_OSUBandwidthEasyBuildTest"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
module load env/release/2023b
module load toolchain/foss/2023b
module load perf/OSU-Micro-Benchmarks/7.2-foss-2023b
srun osu_bw -m 1048576:1048576
