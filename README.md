# BinaryCircuit
This is Python Command Line App for Degital Design.
This isn't optimised as of now.

#### To Install it 
* Clone into your working folder by using this command or download in zip format :

  ```
  git clone https://github.com/Devansh0210/BinaryCircuit.git
  ```
* Install using `python` :

  ```
  cd Binarycircuit
  python setup.py install
  ```
  
#### Getting KMap and Truthtable for given Boolean Function
* Syntax:

  ```cmd
  bincircuit equation "<YOUR FUNCTION>" --kmap --table
  ```
  
* Example :
  ```
  bincircuit equation "A'B+AB'" --kmap --table
  ```
  Output :
  ```
  KMap : 

  ___|  0 |  1 |
    0|  0 |  1 |
    1|  1 |  0 |

  Truth Table :

  | A | B | Output|
  -----------------
  | 0 | 0 |   0   |
  | 0 | 1 |   1   |
  | 1 | 0 |   1   |
  | 1 | 1 |   0   |
  ```
  
#### Generating K-Map and Truth table from given Minterms :

* Syntax :
  ```
  bincircuit minterms <No of Literals> "<Minterms seperated by ','>" --kmap --table
  ```
* Example :
  ```
  bincircuit minterms 3 "0,2,4,6,7" --kmap --table
  ```
  
  Output :
  ```
  Truth Table :

  | A | B | C | Output|
  ---------------------
  | 0 | 0 | 0 |   1   |
  | 0 | 0 | 1 |   0   |
  | 0 | 1 | 0 |   1   |
  | 0 | 1 | 1 |   0   |
  | 1 | 0 | 0 |   1   |
  | 1 | 0 | 1 |   0   |
  | 1 | 1 | 0 |   1   |
  | 1 | 1 | 1 |   1   |

  KMap :

  ___| 00 | 01 | 11 | 10 |
    0|  1 |  0 |  0 |  1 |
    1|  1 |  0 |  1 |  1 |
  ```
  
