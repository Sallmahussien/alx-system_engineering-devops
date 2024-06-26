# Project: 0x03. Shell, init files, variables and expansions

## Resources

#### Read or watch:

* [Expansions](https://linuxcommand.org/lc3_lts0080.php)
* [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
* [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
* [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
* [The alias Command](https://www.linfo.org/alias.html)
* [Technical Writing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240412%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240412T162653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=631f9856a75a2715fa3fb75ca21637e864f3b77bc58e10a7a3f4f783f419465d)
## Learning Objectives

### General

* What happens when you type <code>$ ls -l *.txt</code>
## Tasks

* **0. <o>**
  * [0-alias](./0-alias): Bash script that creates an alias named `ls` with value `rm *`.

* **1. Hello you**
  * [1-hello_you](./1-hello_you): Bash script that prints `hello user`, where user is the
  current Linux user.

* **2. The path to success is to take massive, determined action**
  * [2-path](./2-path): Bash script that adds `/action` to the `PATH`.

* **3. If the path be beautiful, let us not ask where it leads**
  * [3-paths](./3-paths): Bash script that counts the number of directories in the `PATH`.

* **4. Global variables**
  * [4-global_variables](./4-global_variables): Bash script that lists environment variables.

* **5. Local variable**
  * [5-local_variables](./5-local_variables): Bash script that lists all local variables,
  environment variables and functions.

* **6. Local variable**
  * [6-create_local_variable](./6-create_local_variable): Bash script that creates
  a new local variable named `BETTY` with value `Holberton`.

* **7. Global variable**
  * [7-create_global_variable](./7-create_global_variable): Bash script that
  creates a new global variable named `HOLBERTON` with value `Betty`.

* **8. Every addition to true knowledge is an addition to human power**
  * [8-true_knowledge](./8-true_knowledge): Bash script that prints the result of the
  addition of 128 with the value stored in the environment variable
  `TRUEKNOWLEDGE`, followed by a new line.

* **9. Divide and rule**
  * [9-divide_and_rule](./9-divide_and_rule): Bash script that prints the result
  of `POWER` divided by `DIVIDE`. `POWER` and `DIVIDE` are environment variables.

* **10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath**
  * [10-love_exponent_breath](./10-love_exponent_breath): Bash script that displays the
  result of `BREATH` to the power of `LOVE`. `BREATH` and `LOVE` are environment variables.

* **11. There are 10 types of people in the world -- Those who understand binary, and those who don't**
  * [11-binary_to_decimal](./11-binary_to_decimal): Bash script that converts a number
  in base 2 stored in the environment variable `BINARY` to base 10.

* **12. Combination**
  * [12-combinations](./12-combinations): Bash script that prints all possible combinations
  of two letters, except `oo`, as follows:
    * Letters are lower cases, from `a` to `z`.
    * One combination per line.
    * Alpha-ordered.

* **13. Floats**
  * [13-print_float](./13-print_float): Bash script that prints a number stored in the
  environment variable `NUM` with two decimal places.

* **14. Decimal to Hexadecimal**
  * [100-decimal_to_hexadecimal](./14-decimal_to_hexadecimal): Bash script
  that converts a number in base 10 stored in the environment variable `DECIMAL` to base 16.

* **15. Everyone is a proponent of strong encryption**
  * [101-rot13](./100-rot13): Bash script that encodes and decodes text using the rot13
  encryption.

* **16. The eggs of the brood need to be an odd number**
  * [102-odd](./101-odd): Bash script that prints every other line from the input,
  starting with the first line.

* **17. I'm an instant star. Just add water and stir.**
  * [103-water_and_stir](./102-water_and_stir): Bash script that adds the two numbers
  stored in the environment variables `WATER` and `STIR` and prints the result.
  * `WATER` is in base `water`, `STIR` is in base `stir`, and the result is
  in base `behlnort`.