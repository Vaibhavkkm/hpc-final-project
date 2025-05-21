import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OSULatencyIntraNodeDiffNumaEasyBuildTest(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency Test with EasyBuild (Intra-Node, Same Socket, Different NUMA Nodes)'
    valid_systems = ['*']
    valid_prog_environs = ['foss-2023b']
    modules = ['perf/OSU-Micro-Benchmarks/7.2-foss-2023b']
    executable = 'osu_latency'
    executable_opts = ['-m 8192:8192']  # Fixed message size
    num_tasks = 2
    num_tasks_per_node = 2  # Intra-node test
    pre_run = [
        'module use /home/users/vmangroliya/.local/easybuild/modules/all',
        'hwloc-bind --cpubind pu:0 --membind numa:0 pu:16 --membind numa:1 -- srun'
    ]
    reference = {
        '*': {
            'latency': (2.3, -0.1, 0.1, 'us')  # Expected ~2.3 µs, ±10%
        }
    }

    maintainers = ['VaibhavKKM']
    tags = {'latency', 'easybuild', 'intranode', 'diff_numa'}

    def __init__(self):
        super().__init__()
        self.sanity_patterns = sn.assert_found(r'8192\s+\d+\.\d+', self.stdout, 'Output validation')
        self.performance_patterns = {
            'latency': sn.extractsingle(r'8192\s+(\d+\.\d+)', self.stdout, 1, float)
        }
