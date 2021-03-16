# Simple Calculator 

Previously we have developed very basic calculator Which only performed addition.
Now In this App you are allowed to do multiplication,division,substraction,addition,etc.

## List of changes done
- other operator added
- manual entry from keyboard option removed
- backspace bar added
- tradition multiplication and division sign

![Screenshot 2021-03-16 at 10 08 57 AM](https://user-images.githubusercontent.com/63470232/111257162-ab020f80-8640-11eb-9847-918140d56b44.png)

![Screenshot 2021-03-16 at 10 09 44 AM](https://user-images.githubusercontent.com/63470232/111257172-af2e2d00-8640-11eb-9efc-27b30dbac119.png)

## Use of BackSpace Button

```
#BackSpace Button
def cancel():
    lst = myEntry.get()
    lst = list(lst)
    lst = lst[0:len(lst)-1]
    lst = "".join(lst)
    myEntry.delete(0,END)
    myEntry.insert(0,lst)
 ```





![Screenshot 2021-03-16 at 10 10 02 AM](https://user-images.githubusercontent.com/63470232/111257184-b2c1b400-8640-11eb-9c4e-43ea42f82a63.png)

![Screenshot 2021-03-16 at 10 10 18 AM](https://user-images.githubusercontent.com/63470232/111257195-b5bca480-8640-11eb-85c3-a58dd67c1713.png)
