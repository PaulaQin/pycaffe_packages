# pycaffe_packages
wheel packages of caffe python binding


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

## Add lib files to LD_LIBRARY_PATH
1. find your caffe package path
2. add <caffe package path>/libs to LD_LIBRARY_PATH
  
  Open your .bashrc file and add below script:
  ```
  export LD_LIBRARY_PATH=<caffe package path>/libs:$LD_LIBRARY_PATH
  ```

