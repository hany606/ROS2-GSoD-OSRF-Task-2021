from setuptools import setup

package_name = 'gsod_test_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='h.hamed.elanwar@gmail.com',
    description='Simple package for task assesment of GSoD for OSRF 2021',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'print_test = gsod_test_py.print_test:main',
            'customer = gsod_test_py.customer:main',
            'multiplier = gsod_test_py.multiplier:main'

        ],
    },
)
