import reframe as rfm
import reframe.utility.sanity as sn
import os

@rfm.simple_test
class OSULatencyTestSameNuma(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency Test (Same NUMA)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency'
    executable_opts = ['-m 8192:8192']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 2
    reference = {
        'aion:batch': {
            'latency': (0.59, -0.1, 0.1, 'us'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '8192' in content:
                        print("Sanity phase: Found '8192' in stdout content")
                        # Extract latency for performance evaluation
                        import re
                        match = re.search(r'8192\s+(\d+\.\d+)', content)
                        if match:
                            latency = float(match.group(1))
                            print(f"Sanity phase: Extracted latency = {latency} us")
                            self.perf_variables['latency'] = latency
                        else:
                            print("Sanity phase: Failed to extract latency")
                        return True
                    else:
                        print("Sanity phase: Pattern '8192' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSULatencyTestSameSocketDiffNuma(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency Test (Same Socket, Different NUMA)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency'
    executable_opts = ['-m 8192:8192']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 16
    reference = {
        'aion:batch': {
            'latency': (2.28, -0.1, 0.1, 'us'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '8192' in content:
                        print("Sanity phase: Found '8192' in stdout content")
                        # Extract latency for performance evaluation
                        import re
                        match = re.search(r'8192\s+(\d+\.\d+)', content)
                        if match:
                            latency = float(match.group(1))
                            print(f"Sanity phase: Extracted latency = {latency} us")
                            self.perf_variables['latency'] = latency
                        else:
                            print("Sanity phase: Failed to extract latency")
                        return True
                    else:
                        print("Sanity phase: Pattern '8192' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSULatencyTestDiffSocket(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency Test (Different Sockets)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency'
    executable_opts = ['-m 8192:8192']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 64
    reference = {
        'aion:batch': {
            'latency': (2.58, -0.1, 0.1, 'us'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '8192' in content:
                        print("Sanity phase: Found '8192' in stdout content")
                        # Extract latency for performance evaluation
                        import re
                        match = re.search(r'8192\s+(\d+\.\d+)', content)
                        if match:
                            latency = float(match.group(1))
                            print(f"Sanity phase: Extracted latency = {latency} us")
                            self.perf_variables['latency'] = latency
                        else:
                            print("Sanity phase: Failed to extract latency")
                        return True
                    else:
                        print("Sanity phase: Pattern '8192' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSULatencyTestInterNode(rfm.RunOnlyRegressionTest):
    descr = 'OSU Latency Test (Inter-Node)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency'
    executable_opts = ['-m 8192:8192']
    num_tasks = 2
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    reference = {
        'aion:batch': {
            'latency': (3.93, -0.1, 0.1, 'us'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '8192' in content:
                        print("Sanity phase: Found '8192' in stdout content")
                        # Extract latency for performance evaluation
                        import re
                        match = re.search(r'8192\s+(\d+\.\d+)', content)
                        if match:
                            latency = float(match.group(1))
                            print(f"Sanity phase: Extracted latency = {latency} us")
                            self.perf_variables['latency'] = latency
                        else:
                            print("Sanity phase: Failed to extract latency")
                        return True
                    else:
                        print("Sanity phase: Pattern '8192' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSUBandwidthTestSameNuma(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth Test (Same NUMA)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw'
    executable_opts = ['-m 1048576:1048576']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 2
    reference = {
        'aion:batch': {
            'bandwidth': (14168.72, -0.1, 0.1, 'MB/s'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '1048576' in content:
                        print("Sanity phase: Found '1048576' in stdout content")
                        # Extract bandwidth for performance evaluation
                        import re
                        match = re.search(r'1048576\s+(\d+\.\d+)', content)
                        if match:
                            bandwidth = float(match.group(1))
                            print(f"Sanity phase: Extracted bandwidth = {bandwidth} MB/s")
                            self.perf_variables['bandwidth'] = bandwidth
                        else:
                            print("Sanity phase: Failed to extract bandwidth")
                        return True
                    else:
                        print("Sanity phase: Pattern '1048576' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSUBandwidthTestSameSocketDiffNuma(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth Test (Same Socket, Different NUMA)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw'
    executable_opts = ['-m 1048576:1048576']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 16
    reference = {
        'aion:batch': {
            'bandwidth': (10821.98, -0.1, 0.1, 'MB/s'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '1048576' in content:
                        print("Sanity phase: Found '1048576' in stdout content")
                        # Extract bandwidth for performance evaluation
                        import re
                        match = re.search(r'1048576\s+(\d+\.\d+)', content)
                        if match:
                            bandwidth = float(match.group(1))
                            print(f"Sanity phase: Extracted bandwidth = {bandwidth} MB/s")
                            self.perf_variables['bandwidth'] = bandwidth
                        else:
                            print("Sanity phase: Failed to extract bandwidth")
                        return True
                    else:
                        print("Sanity phase: Pattern '1048576' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSUBandwidthTestDiffSocket(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth Test (Different Sockets)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw'
    executable_opts = ['-m 1048576:1048576']
    num_tasks = 2
    num_tasks_per_node = 2
    num_cpus_per_task = 64
    reference = {
        'aion:batch': {
            'bandwidth': (12222.29, -0.1, 0.1, 'MB/s'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '1048576' in content:
                        print("Sanity phase: Found '1048576' in stdout content")
                        # Extract bandwidth for performance evaluation
                        import re
                        match = re.search(r'1048576\s+(\d+\.\d+)', content)
                        if match:
                            bandwidth = float(match.group(1))
                            print(f"Sanity phase: Extracted bandwidth = {bandwidth} MB/s")
                            self.perf_variables['bandwidth'] = bandwidth
                        else:
                            print("Sanity phase: Failed to extract bandwidth")
                        return True
                    else:
                        print("Sanity phase: Pattern '1048576' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)

@rfm.simple_test
class OSUBandwidthTestInterNode(rfm.RunOnlyRegressionTest):
    descr = 'OSU Bandwidth Test (Inter-Node)'
    valid_systems = ['aion:batch']
    valid_prog_environs = ['foss-2023b']
    executable = '/home/users/vmangroliya/reframe-omb/omb-7.2-build/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw'
    executable_opts = ['-m 1048576:1048576']
    num_tasks = 2
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    reference = {
        'aion:batch': {
            'bandwidth': (12327.87, -0.1, 0.1, 'MB/s'),
        }
    }

    def __init__(self):
        super().__init__()
        self.perf_variables = {}

    def custom_sanity(self):
        stdout_path = os.path.join(self.stagedir, 'rfm_job.out')
        print(f"Sanity phase: Checking stdout file at {stdout_path}")
        if os.path.exists(stdout_path):
            print(f"Sanity phase: stdout file exists")
            try:
                with open(stdout_path, 'r') as f:
                    content = f.read()
                    print(f"Sanity phase: stdout file content: {content}")
                    if '1048576' in content:
                        print("Sanity phase: Found '1048576' in stdout content")
                        # Extract bandwidth for performance evaluation
                        import re
                        match = re.search(r'1048576\s+(\d+\.\d+)', content)
                        if match:
                            bandwidth = float(match.group(1))
                            print(f"Sanity phase: Extracted bandwidth = {bandwidth} MB/s")
                            self.perf_variables['bandwidth'] = bandwidth
                        else:
                            print("Sanity phase: Failed to extract bandwidth")
                        return True
                    else:
                        print("Sanity phase: Pattern '1048576' not found in stdout content")
                        return False
            except Exception as e:
                print(f"Sanity phase: Failed to read stdout file: {e}")
                return False
        else:
            print(f"Sanity phase: stdout file does not exist")
            return False

    # Set the custom sanity function directly
    sanity_patterns = sn.defer(custom_sanity)
