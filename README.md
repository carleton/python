# Carleton GAM Library

## Installation

### Native Installation
As root:
```
pip3 install git+https://github.com/carleton/python#egg=gam
```
Sometimes, `pip3` installs files with permissions such that only root can see them.\
This has to be remediated with manual permission corrections.

### Dependency-based Installation
In `requirements.txt`:
```
git+https://github.com/carleton/python.git@main#egg=gam
```

# Carleton GnuPG Library

## Installation

### Encryption Installation
As root:
```
pip3 install git+https://github.com/carleton/python#egg=gpg
```
For some reason, `pip` installs files with permissions such that only root can see them.\
This has to be remediated with manual permission corrections.

### Dependency-based Encryption Installation
In `requirements.txt`:
```
git+https://github.com/carleton/python.git@main#egg=gpg
```

On CLI *(as root)*:
```
pip3 install git+https://github.com/carleton/python#egg=gpg
```

### Encryption Module Usage
Assuming a JSON artifact (file) named `creds.json`:
```
{"login":"you","password":"yourpassword","token":"SOMETOKENTEXT"}
```
*Note: token is optional*

... and it were encrypted with something like:
```
gpg --encrypt --armor -r you@youremail.com -o creds.asc creds.json
```

Sample program:
```
#!/usr/bin/python
from __future__ import print_function
from gpg import ArtifactCredentials

art = ArtifactCredentials()
art.fromFile("creds.asc")
print( '%s=>>> login: %s, password: %s' % ('DBG',art.login(),art.password()))
```

