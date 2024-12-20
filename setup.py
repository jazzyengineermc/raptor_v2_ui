from setuptools import setup

package_name = 'raptor_v2_ui'

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
    maintainer='newans',
    maintainer_email='josh.newans@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'play_face = raptor_v2_ui.play_face:main',
            'play_face_cars = raptor_v2_ui.play_face_cars:main',
            'ui_node = raptor_v2_ui.ui_node:main',
            'raptor_eyes = raptor_v2_ui.raptor_eyes:main'
        ],
        
    },
)
