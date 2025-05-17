#!/bin/bash
#SBATCH --job-name="rfm_OSULatencyTestInterNode"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
module load env/release/2023b
module load toolchain/foss/2023b
srun --cpus-per-task=1 /home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency -m 8192:8192
