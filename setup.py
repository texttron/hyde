from setuptools import setup, find_packages


setup(
    name='hyde',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'cohere',
        'openai',
        'pyserini',
        'faiss-cpu',
        'transformers'
    ],
)