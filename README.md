# Proj2md

The purpose of this utility script is to allow me to generate Markdown output, from some of the many small projects, utilities that I write on almost a day to day basis.

I could you some of the bigger toold such as Sphinx; And for large projects these are the way to go.... but it you want something quick and simple - maybe this will be enought.


### Installing

A pip install should be enough. There are no special modules needed. 

### Running

A python script was installed as part of the pip-install. TO invoke this just type

    proj2md

It will most likely respond with an error as it is expecting a directory

```text
usage: __main__.py [-h] -d Directory [-t TYPES [TYPES ...]]
__main__.py: error: the following arguments are required: -d/--directory 
```


So ....


    proj2md /home/bob/test

Should now produce output - you can redirect it using standard pipes.


