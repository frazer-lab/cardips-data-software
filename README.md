# cardips-data-software

Repository for downloading public data and software for use with the cardips
project.

## `environment.sh`
This contains path updates and should be sourced before working with cardips
data.

## Dependencies

Several python packages are needed to download the public data and software and
in some cases parse the data as well.  I'd recommend using Anaconda python
distribution to obtain most of the dependencies. Beyond the standard Anaconda
packages, you'll need to install `pipelines`, `cdpybio`, `projectpy` using
`python setup.py develop`. `cdpybio` and `pipelines` are submodules in this
repo. After cloning this repository from Github, change into the repo directory
and run:

	git submodule init
	git submodule update

`projectpy` is part of the repo.  `pybedtools`, `pysam`, `pyvcf`,
`HTSeq`, and `macs2, should be installed using `pip install`.
