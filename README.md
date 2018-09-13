# Pydownloader 

With this script, can be make testing  the download and access a diferents websites, for testing the filters UTM or firewall.


## Requerimenst.
```
pip install lib_sysblack
pip install unipath
```

## execute Test.
```
python -m unittest discover -v
```

## Download Binario for windows
[https://github.com/sistemasnegros/pydownloader/blob/master/dist/pydownloader.exe](https://github.com/sistemasnegros/pydownloader/raw/master/dist/pydownloader.exe)

## add data file csv: pydownloader.csv
```
# Extension,Link, Note                    
txt,http://domaintest/test.txt,text plain

```
## Build for Windows.
```
pyinstaller main.spec
```

## Some Examples.

#### Mode basic with python installed.
```
python python main.py  
```

#### Mode basic on windows with binary.
```
pydownloader.exe -v 
```

