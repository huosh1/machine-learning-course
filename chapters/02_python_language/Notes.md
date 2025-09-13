
# Python Language – Chapter 2 Summary

> Source: *Statistics and Machine Learning in Python* — [Github Page](https://duchesnay.github.io/pystatsml/) 
> *Edouard Duchesnay, Tommy Löfstedt, Feki Younes*
> Complement: [Python Basics Youtube Video](https://www.youtube.com/watch?v=mDKM-JtUhhc&list=PLM6UrOI4VLSDOcPEGe1hLbxew6yvuYg1q)

---

All this Chapter is a remind so i will not write a lot about it
## 2.7 Regular Expressions

```python
# 1. Search (first match anywhere)
re.search(pattern, string)

# 2. Match (only from start of string)
re.match(pattern, string)

# 3. Full match (entire string must match)
re.fullmatch(pattern, string)

# 4. Find all matches
re.findall(pattern, string)

# 5. Find matches as objects (with groups)
re.finditer(pattern, string)

# 6. Replace
re.sub(pattern, replacement, string)

# 7. Split by regex
re.split(pattern, string)

```


## Basics

- A **regex** (regular expression) is a pattern used to search, match or replace text.
- Operates on **strings**.
### Main Functions (`re` module)

```python
# 1. Search (first match anywhere)
re.search(pattern, string)

# 2. Match (only from start of string)
re.match(pattern, string)

# 3. Full match (entire string must match)
re.fullmatch(pattern, string)

# 4. Find all matches
re.findall(pattern, string)

# 5. Find matches as objects (with groups)
re.finditer(pattern, string)

# 6. Replace
re.sub(pattern, replacement, string)

# 7. Split by regex
re.split(pattern, string)
```

---

#### Special Characters

|Symbol|Meaning|Example|
|---|---|---|
|`.`|any character except newline|`a.c` → matches `abc`, `axc`|
|`^`|start of string|`^Hello` matches `"Hello world"`|
|`$`|end of string|`world$` matches `"Hello world"`|
|`[]`|character class|`[abc]` matches `a`, `b` or `c`|
|`[^]`|negation|`[^0-9]` = not a digit|
|`\d`|digit|`\d+` = one or more digits|
|`\D`|non-digit||
|`\w`|word char [a-zA-Z0-9_]||
|`\W`|non-word char||
|`\s`|whitespace|space, tab, newline|
|`\S`|non-whitespace||
|`|`|OR|
|`()`|grouping|`(ab)+`|

#### Quantifiers

|Symbol|Meaning|Example|
|---|---|---|
|`*`|0 or more|`a*` matches `""`, `"a"`, `"aaa"`|
|`+`|1 or more|`a+` matches `"a"`, `"aaa"`|
|`?`|0 or 1|`colou?r` matches `"color"` or `"colour"`|
|`{n}`|exactly n|`\d{3}` → 3 digits|
|`{n,}`|n or more|`\d{2,}`|
|`{n,m}`|between n and m|`\d{2,4}`|

#### Groups & Captures

- `( )` → capture group
- `(?: )` → non-capturing group
- `(?P<name> )` → named group

Example:

```python
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "2025-09-13")
print(m.group(0))  # full match "2025-09-13"
print(m.group(1))  # year
print(m.group(2))  # month
print(m.group(3))  # day
```
#### Flags

Pass with `re.compile()` or as argument:

- `re.I` → ignore case
- `re.M` → multiline (^ and $ match each line)
- `re.S` → dot matches newline
- `re.X` → verbose mode (allow spaces, comments)

Example:

```python
pattern = re.compile(r"hello", re.I)
pattern.search("Hello World")  # match
```
#### Examples

```python
# Find all emails
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

# Replace numbers with X
re.sub(r"\d+", "X", "My number is 12345")  # "My number is X"

# Split on commas or semicolons
re.split(r"[,;]", "a,b;c,d")  # ['a', 'b', 'c', 'd']
```
#### Pro Tips

- Use **raw strings** (`r"pattern"`) to avoid escaping backslashes.    
- Test regex quickly in a REPL or with [regex101](https://regex101.com/).
- Prefer `re.compile()` for reusing patterns.

```python
pat = re.compile(r"\d+")
pat.findall("My code is 123 and 456")
```

## 2.8.1 Operating System Interfaces (`os`)

#### Current Working Directory
```python
import os
cwd = os.getcwd()       # get cwd
os.chdir(cwd)           # set cwd
````

#### Temporary Directory

```python
import tempfile
tmpdir = tempfile.gettempdir()  # usually /tmp
```

#### Path Manipulation

```python
mytmpdir = os.path.join(tmpdir, "foobar")
```

#### Create Directories

```python
os.makedirs(os.path.join(tmpdir, "foobar", "plop", "toto"), exist_ok=True)
```

#### List Directory

```python
os.listdir(mytmpdir)  # returns list of entries
```


## 2.8.2 File Input/Output

#### Writing

```python
fd = open(filename, "w")
fd.write("line\n")
fd.close()

# Recommended: context manager
with open(filename, "w") as f:
    for line in lines:
        f.write(line + "\n")
```

#### Reading

```python
# Line by line
f = open(filename, "r")
f.readline()
f.close()

# All at once
f = open(filename, "r")
lines = f.readlines()
f.close()

# With comprehension
with open(filename, "r") as f:
    lines = [line for line in f]
```

## 2.8.3 Explore Directories

#### Walk Through Directory Tree

```python
for dirpath, dirnames, filenames in os.walk(WD):
    print(dirpath, dirnames, filenames)
```

#### Search with Wildcards (`glob`)

```python
import glob
filenames = glob.glob(os.path.join(tmpdir, "*", "*.txt"))
```

#### Split Filenames

```python
def split_filename_inparts(filename):
    dirname_ = os.path.dirname(filename)
    filename_noext_, ext_ = os.path.splitext(filename)
    basename_ = os.path.basename(filename_noext_)
    return dirname_, basename_, ext_
```

#### File Operations (`shutil`)

```python
import shutil, os

shutil.copy(src, dst)
os.path.exists(dst)   # check existence
shutil.copytree(src, dst, dirs_exist_ok=True)
shutil.rmtree(dst)
shutil.move(src, dst)
```

---

#### 2.8.4 Command Execution (`subprocess`)

```python
import subprocess

# Run command
p = subprocess.run(["ls", "-l"])
print(p.returncode)

# Through shell
subprocess.run("ls -l", shell=True)

# Capture output
out = subprocess.run(
    ["ls", "-a", "/"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)
print(out.stdout.decode("utf-8").split("\n")[:5])
```

Notes:
- Returns `CompletedProcess` object.
- Must **decode bytes** into string for stdout.

---

## 2.8.5 Multiprocessing vs Multithreading

### Multiprocessing

- Each **process** = independent program instance with its own address space.
- Contains code, data, heap, and execution stack.
- Context switching is **expensive**.
- Data sharing is more complex.
- Best for **CPU-bound parallel computation**.

### Multithreading

- Threads share the same memory space (code, heap, globals).
- Only stack/PC/registers are separate.
- Context switching is **faster**.
- Easy data sharing.
- Limited by the **Global Interpreter Lock (GIL)** → blocks true CPU concurrency.
- Best for **I/O-bound concurrency** (network, disk, GUI).

### In Python

- `threading` module → multithreading.
- `multiprocessing` module → multiprocessing (preferred for CPU-bound).
#### Example: Random Forest with Parallelization

#### Bootstrapped Decision Tree

```python
def boot_decision_tree(X_train, X_test, y_train, predictions_list=None):
    N = X_train.shape[0]
    boot_idx = np.random.choice(np.arange(N), size=N, replace=True)
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X_train[boot_idx], y_train[boot_idx])
    y_pred = clf.predict(X_test)
    if predictions_list is not None:
        predictions_list.append(y_pred)
    return y_pred
```

#### Sequential Execution

```python
y_test_boot = np.dstack([boot_decision_tree(X_train, X_test, y_train)
                         for i in range(nboot)]).squeeze()
y_test_vote = vote(y_test_boot)
```

#### Multithreading

```python
from threading import Thread
predictions_list = []
t1 = Thread(target=boot_decision_tree, args=(X_train, X_test, y_train, predictions_list))
t2 = Thread(target=boot_decision_tree, args=(X_train, X_test, y_train, predictions_list))
t1.start(); t2.start()
t1.join(); t2.join()
```

#### Multiprocessing

```python
from multiprocessing import Process, Manager
predictions_list = Manager().list()
p1 = Process(target=boot_decision_tree, args=(X_train, X_test, y_train, predictions_list))
p2 = Process(target=boot_decision_tree, args=(X_train, X_test, y_train, predictions_list))
p1.start(); p2.start()
p1.join(); p2.join()
```

#### Pool of Workers

```python
from multiprocessing import Pool, cpu_count
njobs = int(cpu_count() / 2)
pool = Pool(njobs)

async_results = [pool.apply_async(boot_decision_tree,
                                  args=(X_train, X_test, y_train))
                 for i in range(ntasks)]
pool.close(); pool.join()
y_test_boot = np.dstack([ar.get() for ar in async_results]).squeeze()
```

#### Key Takeaways

- Use `with` for **safe file handling**.
- Use `os`, `glob`, `shutil` for **filesystem manipulation**.
- Use `subprocess` for **system commands**, decode output.
- Prefer **multiprocessing** for CPU-bound tasks, **multithreading** for I/O-bound tasks.

## 2.9 Scripts & Argument Parsing

- Use `argparse` to handle **command line arguments**.  
- Typical pattern:
```python
import argparse, os, re, pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input", nargs="+", help="input text files", type=str)
parser.add_argument("-o", "--output", help="output csv file", type=str, default="word_count.csv")
options = parser.parse_args()

if options.input is None:
    parser.print_help()
    raise SystemExit("Error: input files are missing")

# Count words with regex
regex = re.compile("[a-zA-Z]+")
count = {}
for filename in options.input:
    if os.path.isfile(filename):
        with open(filename, "r") as fd:
            for line in fd:
                for word in regex.findall(line.lower()):
                    count[word] = count.get(word, 0) + 1

# Save results with pandas
df = pd.DataFrame([[k, count[k]] for k in count], columns=["word", "count"])
df.to_csv(options.output, index=False)
````

