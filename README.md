# Meadowrun Test Repository

Example user code for meadowrun tests.


## Conda environment in myenv.yml

The following packages are checked for presence in the meadowrun tests:

- requests
- pandas
- meadowrun

Creating myenv.yml from scratch in a `test_repo_conda_env` environment - needs to run on Linux (WSL works):

```bash
conda env create -n test_repo_conda_env
conda activate test_report_conda_env
conda install requests pandas meadowrun -c defaults -c conda-forge -c meadowdata
conda env export > myenv.yml
```

## Pip environment in requirements.txt

The following packages are checked for presence in the meadowrun tests:

- requests
- pandas
- meadowrun

Creating requirements.txt from scratch in the `env` virtual environment folder - needs to run on Linux (WSL works):

```bash
python3 -m venv env
source env/bin/activate
python -m pip install requests pandas meadowrun
python -m pip freeze > requirements.txt
```