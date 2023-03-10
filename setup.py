from setuptools import setup, find_packages
setup(
    name='ikuai_local_api',
    url = 'https://github.com/loyurs/ikuai_local_api.git',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    keywords="ikuai",
    entry_points={
        'console_scripts': [
            'ikuai_local_api=ikuai_local_api.excute:main',
        ],
    },
    author='loyu',
    author_email='loyurs@163.com',
    description='用于调用本地爱快',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
