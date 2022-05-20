# EezPass

EezPass is a really personalisable random password generator

<details>
  <summary><h3>Importation</h3></summary>

  To import **EezPass**, you just have put the *eezpass.py* file in the same folder as your code file.<br>
  ![image](https://user-images.githubusercontent.com/99663083/169581649-4f57038f-2621-4d2e-81df-6937fcb72dec.png)

  After you have checked that, use the **from ... import ...** command by adding the following line on top of your code :
  ```py
  from eezpass import *
  ```

  By doing this, Python will automatically add the *__pycache__* folder into your code folder like shown on the image.
</details>

<details>
  <summary><h3>Configuration</h3></summary>
  
  First, you need to create an instance of the *EezPass class* with this code :
  ```py
  <instance_name> = EezPass(<admin_password>)
  ```
  After that, you just have to set a few parameters before starting using the password generator :
  - The charsets you will use (a = lower letters, m = upper letters, n = numbers, s = special characters)
  - The password's length
  With the following code :
  ```py
  myPass.set_charsets('amns')
  myPass.set_length(16)
  ```
</details>
