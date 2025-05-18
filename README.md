# ReFrame OSU Tests

## Setup
1. Clone repo
2. Load modules: `module load env/release/2023b toolchain/foss/2023b devel/ReFrame/4.7.4-GCCcore-13.2.0`
3. Copy `~/.reframe/settings.py`
4. Run tests:
   ```bash
   reframe -C ~/.reframe/settings.py -c tests/easybuild/latency_test.py -r --system=aion --keep-stage-files
   reframe -C ~/.reframe/settings.py -c tests/easybuild/bandwidth_test.py -r --system=aion --keep-stage-files
   reframe -C ~/.reframe/settings.py -c tests/easybuild/latency_intranode_same_numa.py -r --system=aion --keep-stage-files
   reframe -C ~/.reframe/settings.py -c tests/easybuild/latency_intranode_diff_numa.py -r --system=aion --keep-stage-files
