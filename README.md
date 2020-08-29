# BinaryCircuit
This is Python Command Line App for Degital Design.
This isn't optimised as of now.

#### To Install it 
* Clone into your working folder by using this command :

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
  bincircuit equation " A'B+AB' " --kmap --table
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
