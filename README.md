# pycaffe_packages
These are wheel packages of caffe python binding. The package are built from the BVLC/caffe [source code](https://github.com/BVLC/caffe) on GitHub, with the guide from the offical caffe [documentation](https://caffe.berkeleyvision.org/installation.html).

There are three packages, all of them are only cpu version.
1. *caffe-1.0-py3-none-any.whl* : Python3 binding on linux
2. *caffe-1.0-py2-none-any.whl* : Python2 binding on linux
3. *caffe-windows-py3-none-any.whl*: Python3.5 binding on Windows


# How to install
## Install with pip on Linux

**For Python3**
```
python3 -m pip install https://raw.githubusercontent.com/PaulaQin/pycaffe_packages/master/caffe-1.0-py3-none-any.whl
```

**For Python2**
```
python -m pip install https://raw.githubusercontent.com/PaulaQin/pycaffe_packages/master/caffe-1.0-py2-none-any.whl
```

## Install with pip on Windows
```
python -m pip install https://raw.githubusercontent.com/PaulaQin/pycaffe_packages/master/caffe-windows-py3-none-any.whl
```

## Add lib files to LD_LIBRARY_PATH
1. find your caffe package path
2. add <caffe package path>/libs to LD_LIBRARY_PATH
  
  Open your .bashrc file and add below script:
  ```
  export LD_LIBRARY_PATH=<caffe package path>/libs:$LD_LIBRARY_PATH
  ```

