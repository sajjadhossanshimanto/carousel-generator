### Size
- any squire size
- 1080 x 1080 square
- 512 x 512

### Resource
- screen [link](https://github.com/jainmohit2001/carousel-gen/tree/master) ![image](insperation.png)
- generate with ai [linnk](https://github.com/FranciscoMoretti/carousel-generator) 
![video](https://github.com/FranciscoMoretti/carousel-generator/assets/16997807/50cb033d-84d5-4214-93aa-45c6f524d0b1)



### generate output
approaches :
1. use nbconvert to generate single cell output then trim.
1. for most of the dataframe cells there plain text format available as well. so put them to `codebeautify`
    - what will happen for mark down
1. some how convert `from IPython.display import display` to image
    - possible with `ipywidges`
    - i think this what the nbconvert does
2. mannual
    - `pygements` for code
    - markdown to image `markdown2`
    - html to image `selenium`

its not necessarily I have to choise any single of them. i might use any combnation of them