from setuptools import setup

package_name = 'panda_move'

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
    maintainer='ezza',
    maintainer_email='ezza@todo.todo',
    description='Simple panda move demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_panda = panda_move.move_panda:main',
        ],
    },
)
