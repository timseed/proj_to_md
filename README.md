
## TO specify which file type to process

    proj2md -d <dir> -t json py
    
The default value is just "py"
=======
# Proj2Md 

## Install

    python setup.py install 

## Useage


### Help 

    proj2md -h 

```text
proj2md --help
usage: __main__.py [-h] -d Directory [-t FILE_TYPES]

Project to md

optional arguments:
  -h, --help            show this help message and exit
  -d Directory, --directory Directory
                        Project directory
  -t FILE_TYPES, --types FILE_TYPES
                        Output only file types [py] default. Use multiple -t
                        to add more file types
```

### Example

This will stream to the STDOUT


    proj2md -d /home/user/python_proj 

To output a MD file just pipe it


    proj2md -d /home/user/python_proj > Proj.md

# Tech Docs

Sphinx Docs available at 

[./Doc/build/html/index.html](./Doc/build/html/index.html)


