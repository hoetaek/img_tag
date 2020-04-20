from setuptools import setup
setup(
    name='img_tag',
    version='0.1.0',
    packages=['img_tag'],
    install_requires=[
        'pydrive',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'img_tag = img_tag.__main__:main'
        ]
    })
