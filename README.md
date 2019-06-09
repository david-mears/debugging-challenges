# Debugging practice

9th June: I plan to fix the python bugs

Process:

Read and digest instructions

Set a debugging breakpoint at (original) line 19 and watched the variable `value` to find what was registering as int that wasn't an int

Found that False and True were doing so

REPL python:
```
>>> isinstance(False, int)
True
```

Proposed fix: move the elif which catches booleans to precede the one which catches integers.

Done in this commit: https://github.com/david-mears/debugging-challenges/commit/227cf914c49855ef96456259857c4622a87424fc


Below is the original README

## Welcome to our debugging challenges

Please choose the language you want to learn to debug with. We offer:

  - [Javascript](./Javascript/README.md): in-browser debugging using the [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools/Debugger)
  - [Python](./Python/README.md): debugging a terminal python script using the build-in [PDB](https://docs.python.org/2/library/pdb.html)
  - [Ruby](./Ruby/README.md): debugging a terminal ruby programme using [pry](http://pryrepl.org/)

### Presentation

Unclear what debugging is about? You can find Ben's presentation here:

   [http://slides.com/benjaminkampmann/debugging-101/live#/](slides.com/benjaminkampmann/debugging-101/live#/)

(To navigate through the slides: always go down if possible. If not go right once. Repeat.)
