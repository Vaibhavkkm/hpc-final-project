#!/bin/bash
module purge
# load old environment
module load env/deprecated/2020b
echo "load old env"
# load essensial modules
echo "loading EESSI"
module load EESSI

echo "loading OSU-Micro-Benchmarks"
module load OSU-Micro-Benchmarks/7.2-gompi-2023b
echo "lading OpenMPI"
module load OpenMPI/4.1.6-GCC-13.2.0
echo "leading ReFrame"
module load ReFrame/4.6.2
reframe --version
echo "loading python"
module load Python/3.11.5-GCCcore-13.2.0

reframe -C eessi_config.py -c osu_eessi.py -r



