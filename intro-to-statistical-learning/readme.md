An Introduction to Statistical Learning with Applications in R

Springer Texts in Statistics 

Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani

http://www.StatLearning.com


This is meant to "translate" the examples and explanations in the An Introduction to Statistical Learning with Application in R to Python and to build on those examples with interactive visualizations. 


# Data Sets

All data sets are available in the <a href="https://cran.r-project.org/web/packages/ISLR/ISLR.pdf">ISLR</a> library (in R) except for `Boston` which is part of `MASS` and `USArrests` which is part of `base`. 

Additional data sets may be found on the web site at http://faculty.marshall.usc.edu/gareth-james/ISL/data.html.

R Package `ISLR`

https://cran.r-project.org/web/packages/ISLR/ISLR.pdf


# Chapters 

* <a href="chapter-02/index.md">Chapter 02</a>


# Python Packages 

* `numpy` (NumPy) is a package for scientific computing with powerful arrays. https://numpy.org/
* `pandas` is a library for high-performance, easy-to-use data structures and data analysis tools. https://pandas.pydata.org/pandas-docs/stable/index.html
* `matlibplot` is a comprehensive library for creating static, animated, and interactive visualizations in Python. https://matplotlib.org/
* `seaborn` is a library for making statistical graphics in Python and is built on top of matplotlib. https://seaborn.pydata.org/introduction.html


# Code Style 

I find myself working in many different languages, each with their own syntax requirements, code organization, library and namespace structure, etc. This includes C#, JavaScript/TypeScript, R, and Python. For me, the following guidelines and code style allows me to quickly and easily be consistent across the languages without introducing soft errors. You may find them helpful or refer to your own coding style. 


## Objectives
* Achieve high-level of code readability. Sometimes readability is about being verbose and somtimes it is about being concise, but it is usually never about being lazy. 
* Increased maintainability - even at the cost of potentially being overly explicit by design.
* Reduce lookups, cross referencing, conflicts and confusion. e.g. determining class namespace sources.
* Self-documenting code that reads well. 
* Maintain and understand appropriate scope of variables. 
* Reduce barrier to entry for new developers coming into the language or not familiar with all the packages and libraries. 

## Variable Declarations 
* All variables will be appropriately type hinted to explictly show their data/class types. This will help you track down the reference and get help on the class and helps when a class is created by a factory or other method that does not explicitly state its return. You may know the data type if you first create it, work with it, are very familiar with the source library, etc. but when you come back later or someone else with less experience or knowledge of your code might need to study it longer to understand the returned class in a factory pattern, builder pattern, or other where the instantiation of the class happens within the method. 
* Reduce the "trackdown" time when wanting to research a class, object, or method. 
* A lot of the code has overly redudant variable declaration and notes to help beginners understand (hopefully) and make it easier to get back to the documentation through the namespaces.


## Libraries and Imports 
* Library names will not be short-cutted or aliased when possible to prevent difficulty of identifying a library further down in code without referring back to the original import. 
* Imports will be careful not to pollute the global namespace where it makes sense and to allow easy referencing of libraries classes and components that may be less common. 
* Reducing alias dependencies and polluting the global namespace is meant to reduce potential conflicts, but there are common aliases used and if they make more sense to you, you should continue to use them. 