# CrappyCipher
A not very hard to break cipher algorithm, BUT IT DOES WORK.

----
**How to use**

Command Version arguemnts:

ciph - ciph (string) - Input this on the command to cipher a word
  
unciph - unciph (cipher) - Input this on the command to uncipher a word

Class Version:

Create a object of the class CrapCiph, e.g. ```c = new CrapCiph()``` 

To cipher something use the ciph function, e.g. ```string = c.ciph("Hello")``` | Arugments: (<string>)

To uncipher something use the unciph function, e.g. ```string = c.unciph("6003876528-8422104574-9005814792-9005814792-9255976314-83387174-")``` | Arugments: (<Ciphered String>)
  
As I said above, its not very hard to break, it simply times the char value by a seed, which it generates randomly and stores in the output. Because of the way it works though, every string will have 99999899 posible outputs.
But it does at least work, so whiles its shit, its also quite quick since its so simple.

I may make it work as a class in the future, but right now I cant be bothered
