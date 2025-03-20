from setuptools import setup, find_packages

setup(
    name="generate_highcharts_image",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["highcharts_core"],
    include_package_data=True,
)

