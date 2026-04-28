from setuptools import setup, find_packages

setup(
    name="contador_objetos",
    version="0.2.0",
    description="Librería para segmentación y conteo de objetos en imágenes cenitales",
    author="Gabriel Lopez",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "contador_objetos": ["imagenes/*.jpg"]
    },
    install_requires=[
        "opencv-python",
        "numpy",
        "matplotlib",
        "pandas"
    ],
)
