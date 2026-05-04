from setuptools import setup, find_packages

setup(
    name="unified_observer_architecture",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pyyaml",
        "networkx",
        "fastapi",
        "uvicorn",
        "pytest",
        "pybind11"
    ],
    author="Samuel Jackson Grim",
    description="Unified Observer Architecture for emergent synthetic identity systems",
    python_requires=">=3.10",
)
