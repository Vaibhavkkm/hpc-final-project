import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSUBandwidthIntraNodeDiffNumaEasyBuildTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth Test with EasyBuild (Intra-Node, Same Socket, Different NUMA Nodes)'
    valid_systems = ['aion']
    valid_prog_environs = ['foss-2023b']
    modules = ['perf/OSU-Micro-Benchmarks/7.2-foss-2023b']
    executable = 'osu_bw'
    executable_opts = ['-m 1048576:1048576']  # Fixed message size (1MB)
    num_tasks = 2
    num_tasks_per_node = 2  # Intra-node test
    pre_run = [
        'module use /home/users/vmangroliya/.local/easybuild/modules/all',
        'hwloc-bind --cpubind pu:0 --membind numa:0 pu:16 --membind numa:1 -- srun'
    ]
    reference = {
        'aion': {
            'bandwidth': (12000, -0.1, 0.1, 'MB/s')  # Expected ~12,000 MB/s, adjust after run
        }
    }

    maintainers = ['Asal']
    tags = {'bandwidth', 'easybuild', 'intranode', 'diff_numa'}

    def __init__(self):
        super().__init__()
        self.sanity_patterns = sn.assert_found(r'1048576\s+\d+\.\d+', self.stdout, 'Output validation')
        self.performance_patterns = {
            'bandwidth': sn.extractsingle(r'1048576\s+(\d+\.\d+)', self.stdout, 1, float)
        }
