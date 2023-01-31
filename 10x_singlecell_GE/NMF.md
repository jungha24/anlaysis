#### purpose: 
find a subset of genes which can explain the difference between two cellular model 
#### rational for using NMF: 
it was hard to define distinct clusters of two cellular model. using only gene set which has better explanation of two cell states might make better clustering.
#### method:
apply cNMF of Dylan Kotliar et al,. 2019 (eLife)

#### [1]. install cNMF in conda environment
- task1: run jupyter notebook server in the conda environment
- (1) make conda environment including jupyter
~~~bashscript
conda create -n cnmf_env_jhl --yes --channel bioconda --channel conda-forge --channel defaults python=3.7 fastcluster matplotlib numpy palettable pandas scipy 'scikit-learn>=1.0' pyyaml 'scanpy>=1.8' jupyter && conda clean --yes --all
conda activate cnmf_env_jhl
pip install cnmf
~~~
- (2) move to working directory (env activated state)
- (3) run jupyter notebook (env activated state)
~~~bashscript
jupyter notebook --port=10024 --no-browser
~~~
- (4) (local) run follow command in the terminal and interact with jupyter notebook through chrome 
~~~bashscript
ssh -N -f -L localhost:10024:localhost:10024 -i /Users/jeongha/.ssh/id_rsa -p 40022 mchoilab_dell@147.47.228.43
(chrome) localhost:10024
~~~
