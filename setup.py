from setuptools import setup


setup(
    name='cldfbench_sanzhi',
    py_modules=['cldfbench_sanzhi'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'sanzhi=cldfbench_sanzhi:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pydictionaria>=2.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
