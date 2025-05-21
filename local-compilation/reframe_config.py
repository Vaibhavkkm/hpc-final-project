site_configuration = {
    'systems': [
        {
            'name': 'aion',
            'descr': 'Aion Cluster',
            'hostnames': ['aion'],
            'modules_system': 'lmod',  # Specify Lmod as the module system
            'partitions': [
                {
                    'name': 'batch',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'environs': ['foss-2023b'],
                }
            ]
        },

        {
            'name': 'iris',
            'descr': 'Iris Cluster',
            'hostnames': ['iris'],
            'modules_system': 'lmod',  # Specify Lmod as the module system
            'partitions': [
                {
                    'name': 'batch',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'environs': ['foss-2023b'],
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'foss-2023b',
            'modules': ['env/release/2023b', 'toolchain/foss/2023b'],
        }
    ]
}
