# ReFrame OSU Tests

## Setup
1. Clone repo: git clone <your-repo-url>
2. Load modules: module purge; module load env/release/2023b toolchain/foss/2023b system/hwloc devel/ReFrame/4.7.4-GCCcore-13.2.0
3. Copy ~/.reframe/settings.py
4. Unset Slurm variables: unset SLURM_CPUS_PER_TASK SLURM_TRES_PER_TASK
5. Run tests:
   
6. Check results:
   

## Results
- Inter-node latency: 4.11 µs (Aion, EasyBuild, 8192 bytes, within 3.51–4.29 µs)
- Inter-node bandwidth: 12321.01 MB/s (Aion, EasyBuild, 1MB, within 10,800–13,200 MB/s)

## Notes
- Unset SLURM_CPUS_PER_TASK/SLURM_TRES_PER_TASK if Slurm conflicts occur.
- Use --keep-stage-files to preserve rfm_job.out.
- If stage directory varies, use: find ~/reframe-omb/stage/ -name rfm_job.out -exec cat {} \;
