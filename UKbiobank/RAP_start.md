### RAP (research analysis platform) usage
#### RAP start
- https://dnanexus.gitbook.io/uk-biobank-rap/getting-started/platform-overview 
1. genearate account of RAP
2. connect the account to UK biobank AMS account
3. generate authentication tocken
  * install dx
  * https://documentation.dnanexus.com/downloads
  * https://github.com/dnanexus/dx-toolkit/issues/488
  ~~~bashscript
  $ pip3 install dxpy

  # If you use later version of MacOS with Z shell (zsh), enable tab completion by running the following command or adding it to your .zshrc 
    ##  autoload -Uz compinit && compinit
    ##  autoload bashcompinit && bashcompinit
    ##  eval "$(register-python-argcomplete dx|sed 's/-o default//')"
  
  # Installation of Java, R and C++ SDK from tarball
  $ source /Users/jeongha/software/py3env/bin/activate
  (py3env) pip install argcomplete
  (py3env) pip install dxpy
  (py3env) which python #/Users/jeongha/software/py3env/bin/python
  (py3env) vi /Users/jeongha/software/dx-toolkit/bin/dx
    ## used this path to replace the shebang
    ## -> #!/Users/jeongha/software/py3env/bin/python
  (py3env) vi /Users/jeongha/software/dx-toolkit/bin/register-python-argcomplete
    ## -> #!/Users/jeongha/software/py3env/bin/python
    
  (py3env) cd dx-toolkit && source environment
  (py3env) echo "autoload -Uz compinit && compinit" >> ~/.zshrc && source ~/.zshrc
  $ dx
  ~~~
  * logging in with an authentication tocken
  * https://documentation.dnanexus.com/user/helpstrings-of-sdk-command-line-utilities
  ~~~bashscript
  dx login --token TOKEN
  ~~~
4. create a project
  * PROJECTS > New Project > rename project name and enter application ID

