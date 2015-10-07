# cardips-data-software

Repository for downloading public data and software for use with the cardips
project.

## `environment.sh`
This contains path updates and should be sourced (`source environment.sh `)
before working with cardips data.

## Dependencies

Several python packages are needed to download the public data and software and
in some cases parse the data as well.  I'd recommend using Anaconda python
distribution to obtain most of the dependencies. You can load the cardips
Anaconda environment using `conda create --name cardips --file conda_env.txt`.
You should name the Anaconda environment `cardips` or you'll likely run into
problems with some of the code.  Beyond the packages in `conda_env.txt`, you'll
need to install `pipelines`, `cdpybio`, `cardipspy` and `WASP` using `python
setup.py develop`. `cdpybio`, `pipelines` and `WASP` are submodules in this
repo. After cloning this repository from Github, change into the repo directory
and run:

	git submodule init
	git submodule update

`cardipspy` is part of the repo. `pybedtools`, `pysam`, `pyvcf`, `HTSeq`, and
`macs2`, should be installed using `pip install`.

## Conda Environment

If the python environment is updated, please update the environment file using
`conda list -e > conda_env.txt`.
