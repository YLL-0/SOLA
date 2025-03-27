# Review of C Programming

The following serves as a quick review of the basic data types, operations, and statements in the C programming language. For a deeper understanding, readers are encouraged to consult additional resources. This section is also helpful for those familiar with related languages like C++ or Java.

## Recommended Books
1. **The C Programming Language**, 2nd ed., B. Kernighan and D. Ritchie, Prentice Hall, 1988, ISBN 0131103628.
2. **Programming in C**, 3rd ed., S. Kochan, Sams, 2004, ISBN 0672326663.
3. **C Primer Plus**, 5th ed., S. Prata, Sams, 2004, ISBN 0672326965.

---

## 1.5.1 Basic Data Types
C has four basic data types:
- **int**: Stores whole numbers.
- **float**: Stores real numbers.
- **double**: Stores real numbers with higher precision.
- **char**: Stores character symbols.

### Example Code:
```c
#include <stdio.h>
int main()
{
    int x, y;
    char a;
    float f, e;
    double d;

    x = 4;
    y = 7;
    a = 'H';
    f = -3.4;
    d = 54.123456789;
    e = 54.123456789;

    printf("%d %c %f %lf\n", x, a, e, d);
    printf("%d %c %.9f %.9lf\n", x, a, e, d);
}
```

### Output:
```
4 H 54.123455 54.123457
4 H 54.123455048 54.123456789
```

- The `float` type runs out of precision, while `double` retains accuracy.

---

## 1.5.2 Basic Arithmetic
C supports the following arithmetic operations:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)

### Example Code:
```c
#include <stdio.h>
int main()
{
    int x, y;
    int r1, r2, r3, r4, r5;

    x = 4;
    y = 7;

    r1 = x + y;
    r2 = x - y;
    r3 = x / y;
    r4 = x * y;

    printf("%d %d %d %d\n", r1, r2, r3, r4);

    r3++;
    r4--;
    r5 = r4 % r1;

    printf("%d %d %d\n", r3, r4, r5);
}
```

### Output:
```
11 -3 0 28
1 27 5
```

- The modulus operator (`%`) works only with integers.

---

## 1.5.3 Loops
C provides three types of loops:
1. **for**: Executes a fixed number of iterations.
2. **while**: Executes an unknown number of iterations, with a condition checked before each iteration.
3. **do-while**: Executes at least once, with a condition checked after each iteration.

### Example Code:
```c
#include <stdio.h>
int main()
{
    int i, x;
    x = 0;

    for (i = 0; i < 4; i++)
    {
        x = x + i;
        printf("%d\n", x);
    }

    while (i < 7)
    {
        x = x + i;
        i++;
        printf("%d\n", x);
    }

    do
    {
        x = x + i;
        i++;
        printf("%d\n", x);
    } while (i < 9);
}
```

### Output:
```
0
1
3
6
10
15
21
28
36
```

---

## 1.5.4 Conditionals and Blocks
C conditionals include:
- **if-else**: Tests for equality (`==`), inequality (`!=`), and relative size (`>`, `<`, `>=`, `<=`).
- Logical operators:
  - AND (`&&`)
  - OR (`||`)

### Example Code:
```c
#include <stdio.h>
int main()
{
    int i, x;
    x = 0;

    for (i = 0; i < 5; i++)
    {
        if (i % 2 == 0 || i == 1)
            x = x + i;
        else
            x = x - i;

        printf("%d\n", x);
    }
}
```

### Output:
```
0
1
3
0
4
```

- Indentation is for readability only and does not affect execution.

---

## 1.5.5 Flow Control
C provides two flow control statements for loops:
1. **continue**: Skips the rest of the current iteration and starts the next one.
2. **break**: Terminates the loop immediately.

### Example Code:
```c
#include <stdio.h>
int main()
{
    int i, x;
    x = 0;

    for (i = 0; i < 5; i++)
    {
        if (i % 2 == 0)
            continue;

        x = x - i;

        if (i % 4 == 0)
            break;

        printf("%d\n", x);
    }
}
```

### Output:
```
-1
-4
```

- Out of five iterations, only two reach the `printf()` statement.

### Additional Flow Control Statements:
1. **exit**: Terminates the program immediately.
2. **goto**: Jumps to a named line of code (discouraged due to potential complexity).

---

## Exercises

### 1. Unix vs. Windows System Software
System software on a Unix system performs the same basic services as system software on a Microsoft Windows system. However, there are some fundamental differences in how the system software is designed and developed.  
**Task**: Describe at least two differences.

---

### 2. Debugger Operations
**Task**: Briefly describe two operations that a debugger can perform (i.e., commands that you can give to a debugger).

---

### 3. Compiling for Debugging
**Task**: Why must a program specifically be compiled for debugging to be able to execute that program in a debugger? What two things does the compiler do to assist a debugger?

---

### 4. Text Editor Assistance
**Task**: Describe two ways a text editor can assist with writing program code (as opposed to writing generic text using a word processor).

---

### 5. Unix Programs and Shell Commands
A Unix system typically has many programs that can be run from its graphical user interface (menus).  
**Task**: For the system you are using, pick five programs and identify the actual filename that is being executed. Use a shell to type the name of the program at the prompt to start the program instead of starting it from the menu. Read the man page for the program and discover what options can be given to the program at startup.

---

### 6. Text Editor Features
**Task**: For the text editor of your choice, identify what keystroke or menu option it provides in order to display the line number of the current cursor location. Also, identify how to jump the cursor to a given line.

---

### 7. Debugging Code
**Task**: Debug the following code by compiling it for debugging and executing it within a debugger.  
**Question**: At which line of code does the program crash? Why does it crash there?

```c
#include <stdio.h>
#include <math.h>
main(int argc, char *argv[])
{
    int n, i;
    int d2, count;
    double d1;

    while (1)
    {
        printf("Enter a number (0 to quit): ");
        scanf("%d", &n);
        if (n == 0)
            break;

        count = 0;
        for (i = 0; i < n; i++)
        {
            d1 = (double)n / (double)i;
            d2 = n / i;
            if (fabs(d1 - (double)d2) < 0.00001)
                count++;
        }

        if (count == 2)
            printf("%d is prime\n", n);
        else
            printf("%d is not prime\n", n);
    }
}
```

---

### 8. Closest Integer with Whole Number Square Root
**Task**: Write a program that prompts the user for a positive integer and then reports the closest integer having a whole number square root.  
**Example**:  
- Input: `8` → Output: `9`  
- Input: `18` → Output: `16`

---

### 9. Sum of Digits
**Task**: Write a program that prompts the user for a positive integer and then computes the sum of all the digits of the number.  
**Example**:  
- Input: `2784` → Output: `21`  
- Input: `59` → Output: `14`

---

### 10. Contact Information Manager
**Task**: Write a program that manages contact information for a group of people. The program should save the first name, last name, and telephone number for up to 12 people.  
**Features**:
- Add a person.
- Delete a person.
- Update the information for a person.
- Display all information for all current entries.  

**Question**: How could you break up the programming work into a set of subproblems? Describe the subproblems, the order in which you would work on them, and any testing you would do for each subproblem before proceeding to the next.

---

### 11. Debugging Sorting Code
The following program compiles and executes but does not do what its designer intended.  
**Task**: Use a debugger to track down what is going wrong.  
**Question**: Is it a bug or a program design flaw?

```c
#include <stdio.h>
main()
{
    int n[5], s, i, j, w;

    for (i = 0; i < 5; i++)
    {
        printf("Enter any integer: ");
        scanf("%d", &(n[i]));

        s = 0; /* find index of smallest */
        for (j = 1; j <= i; j++)
            if (n[j] < n[s])
                s = j;

        w = n[i]; /* swap smallest with current */
        n[i] = n[s];
        n[s] = w;
    }

    for (i = 0; i < 5; i++)
        printf("%d\n", n[i]);
}
```

**Hint**: Set a breakpoint at line `w = n[i];` and use the debugger to inspect the variables.

---

## Summary
This review covered:
- Basic data types (`int`, `float`, `double`, `char`).
- Arithmetic operations and loops (`for`, `while`, `do-while`).
- Conditionals (`if-else`) and flow control (`continue`, `break`, `exit`, `goto`).
- Exercises to practice debugging, writing programs, and understanding Unix system tools.

For deeper understanding, refer to the recommended books or consult the C standard documentation.