from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author='Seb Szacik',
    description='SnapshotAlyzer 30000 is tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['guru'],
    url='https://github.com/h0oper/snapshotalyzer_mk1',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        guru=guru.guru:cli
        ''',
)