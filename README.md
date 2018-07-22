# An Open Souce Programming Language

Gala is a typed multi-paradigm scripting and programming language, designed to be as
simple as possible, while also offering familiar features such as function, classes.

If you come from a C-style language such as C, C++, Javascript, Go, Python, or similar, you
should be immediately productive with Gala.

Gala is at a very early stage of development and as such it does not support many use-cases.

## Current Features 

### Language

 * **Simplicity & familiarity** - You should be able to start without reading too much docs.
 * **Unabiguous** - There is typically one obvious way to do it.
 * **Typed** - Types help you write correct code.
 
### Implementation

The current compiler implementation is called Pygala and is written in Python/Clang.

 * **Fast** - Gala is transpiled to C and compiled with Clang. This means it should be as fast as C.
 * **Compiled** - Deployment is as easy as dropping the executable to the target system.
 * **Portable** - Thanks to tranpilation to C, it runs everywhere where C does.

## Roadmap Features 

This describes the future features we want to have into the language

### Language

 * **Unicode-only** - Get away with encoding problems.
 * **Powerful** - Include useful construct such as modules, classes, hash maps, lists
    to make development fast and complexity manageable.
 * **Safe** - No memory problems.
 * **Concurrent** - Concurrent programming should be as easy as Go.
 * **Big standard library** - Based on C libraries and therefore stable and feature rich.
 * **Automatic type inference** - Just like in Go.
    
### Implementation

 * **Clear errors** - Provide clear compilation errors.
 * **Fast compilation** - Use caching automatically.
 * **Hot reloading** - Embed the hot reloading into the compiler.
    Just type your code and it's running.
 * **Package management** - Integrate package management into the compiler so that there is
    a standard way to handle dependencies

## Motivation

All languages that I tried have some problems: either they are not concurrent and scalable,
they have crappy libraries, they are too low level or they are configuration and dependency
hells.

## Interested?

Intrested in gala. Check out the [docs](/gala/docs/) or drop me an e-mail at francescopasa@gmail.com.