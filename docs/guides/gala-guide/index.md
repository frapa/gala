# Gala Language Guide

Gala is designed to be familiar if you come from a C-style language.

---

## Types

Each value in Gala has a type. Currently the supported types are the following:

#### Numeric

 * `int32`
 * `int64`
 * `float32`
 * `float64`
 * `bool`
 
#### Strings 

 * `string` - unicode string

---

## Literals

#### Numeric

 * `int32` and `int64` - Can be defined with binary, octal, decimal or hexadecimal literals
    - Binary: `0b1010101`
    - Octal: `0644`
    - Decimal: `7618`
    - Hexadecimal: `0x1fad`
 * `float32` and `float64` - Can be defined in decimal only. Esponential notation is allowed
    - `12.34` or `123.456e7`
 * `bool`
    - Either `true` or `false`

#### Strings

String are surrounded by single (`'`) or double (`"`) quotes. Examples of string literals are

```
'I am a string - I can contain any character, such as 普'
"I am another string"
```

Strings are always unicode, therefore you can put any characters in them.

If you want to put a quote in a string, you can use a slash `\` to escape them. Double the slash
to escape the slash itself.

```
'I\'m fine with slashes!'
"This is what can be called a \"string\""
'This is a slash: \\'
```

Here are some special escapes for common carachters:

```
'This is a line\nAnd this another'
'\tThis line has a tab before'
'This is a carriage return: \r'
'This a backspace: \b'
'This a form feed: \f'
```

You can also input any unicode characters in decimal or hexadecimal as follows:

```
'This is the letter a: \97'
'This is again the letter a: \x61'
'Yet again the letter a: \u61'
```

---

## Variables

Variables are declared with the Go-like syntax `variable_name type`. For example:

```
year int32 = 2018;
load float32 = 0.57;
passed bool = true;
```

## Functions

Functions are defined as follows

```
fun function_name(arg1 type1, arg2 type2) return_type {
    ...
}
```

Putting the type after the identifier is a bit different from other C-style languages,
but is clear to read and remains readable even for function types.
The type signature of the function will be:

```
fun (type1, type2) return_type
```

which can be read as "a function that takes `type1` and `type2` and returns `return_type`".

#### Return statement

To return a value from a function, use the return statement:

```
fun generate_a_one() int32 {
    return 1;
}
```

#### Function invocation

To call a function and get the result, use the invocation syntax:

```
one inte32 = generate_a_one();
```