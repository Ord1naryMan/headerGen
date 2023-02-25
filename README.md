# Attention

This project is in beta so it may have A LOT of bugs and can work not how you expect it to 

# Info

This project is designed for lazy me.

But i desided to leave it in GitHub

So this script takes .cpp file read it and generate header file

# Description

As you know functions in c++ love to be stored in .cpp 

But main.cpp should see them for using

So here it comes, skeleton of .cpp file should be in .h file

And i decided to try creating script for checking .cpp and creating skeleton in .h file

# Usage

This program can work with classes and without

Just run
```sh
headergen my_header-2.2.cpp
```

Then it automatically create my_header-2.2.h file and write everything here

Name can differ from example

But there is some issues:
1. This script just doesn't know names of public and private members of a class so you have to add them manually

2. This script just doesn't know what functions are public and what are private so you have to add 'public' and 'private' words manually

3. If you are using std:: or  other stuff like this in junction defenition, script may have undefined behavior

Note: you should use using dirrectives in .cpp file and manually add std:: and everything like this in .h file


#Installing

```sh
bash install.sh
```
