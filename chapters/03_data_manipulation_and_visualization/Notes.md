# Data Manipulation And Visualization – Chapter 3 Summary

> Source: _Statistics and Machine Learning in Python_ — [Github Page](https://duchesnay.github.io/pystatsml/)  
> _Edouard Duchesnay, Tommy Löfstedt, Feki Younes_  
> Complement: [Python Data Science Youtube Video](https://www.youtube.com/watch?v=GPVsHOlRBBI&list=PLM6UrOI4VLSDOcPEGe1hLbxew6yvuYg1q&index=5)

---

**NumPy** is an extension to the Python programming language, adding support for large, multi-dimensional (numerical) arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays.

Numpy functions are executed by compiled in C or Fortran libraries, providing the performance of compiled languages.

### Create arrays

```python
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)

# Initial Placeholders
np.zeros((3,4))
np.ones((2,3,4),dtype=np.int16)
d = np.arange(10,25,5)
np.linspace(0,2,9)
e = np.full((2,2),7)
f = np.eye(2)
np.random.random((2,2))
np.empty((3,2))


## Copying arrays

h = a.view()   # Create a view of the array with the same data
np.copy(a)     # Create a copy
h = a.copy()   # Create a deep copy
```

**Explications — intérêt :**

- `np.array` convertit des listes Python en tableaux numériques rapides, avec **un seul type** par array (meilleure perf mémoire + vectorisation).
    
- Les _constructeurs_ (`zeros`, `ones`, `arange`, `linspace`, `full`, `eye`, `random`, `empty`) servent à **initialiser rapidement** des tenseurs pour calculs/matrices/poids ML.
    
- **Copies vs vues :** `view()` ne duplique pas les données (⚠️ modifications vues des deux côtés), `copy()` duplique (sécurité, plus de mémoire). Utilise `view` pour la perf quand tu sais ce que tu fais ; `copy` pour éviter les effets de bord.
    

---

### I/O

```python
# Saving & Loading On Disk

>>> np.save('my_array', a)
>>> np.savez('array_npz', a, b)
>>> np.load('myarray.npy')

# Saving & Loading Text Files
>>> np.loadtxt('myfile.txt')
>>> np.genfromtxt("my_file.csv, delimiter= )
>>> np.savetxt("myarray.txt", a, delimiter= )
```

**Explications — intérêt :**

- `np.save`/`np.load` (format **.npy**) : **rapide, sans perte**, préserve le dtype/shape → idéal pour datasets intermédiaires.
- `np.savez` (format **.npz**) : archive **plusieurs arrays** nommés.
- `loadtxt`/`genfromtxt` : lire du **texte/CSV**. `genfromtxt` gère mieux les **valeurs manquantes**.
- `savetxt` : export texte/CSV (lisible mais plus lent et perte de dtype complexe).
    
- ⚠️ Petits correctifs si tu t’en sers :
    
    - `np.load('my_array.npy')` (nom exact écrit par `save`)
    - `np.genfromtxt("my_file.csv", delimiter=',')`
    - `np.savetxt("myarray.txt", a, delimiter=' ')`

---

### Inspecting Your Array

```python
a.shape        # Array dimensions
len(a)         # Length of array
b.ndim         # Number of array dimensions
e.size         # Number of array elements
b.dtype        # Data type of elements
b.dtype.name   # Name of data type
b.astype(int)  # Convert to different type
```

**Explications — intérêt :**

- Ces attributs te donnent la **morphologie et le type** (shape/ndim/size/dtype) pour debugger pipeline ML.
    
- `astype` **cast** les données (⚠️ crée une _copie_ → coût mémoire/temps ; attention aux pertes de précision).
    

---

## Data Types

```python
np.int64       # Signed 64-bit integer types
np.float32     # Standard double-precision floating point
np.complex     # Complex numbers represented by 128 floats
np.bool        # Boolean type storing TRUE and FALSE values
np.object      # Python object type
np.string_     # Fixed-length string type
np.unicode_    # Fixed-length unicode type

np.info(np.ndarray.dtype)   # Asking For Help
```

**Explications — intérêt :**

- Le **dtype** impacte **précision, mémoire, perf** (ex : `float32` pour GPU/ML, `float64` pour précision num.).
- `object` casse souvent la vectorisation (lent) → à éviter pour le calcul numérique.
- `np.info` te donne de l’aide rapide sur les dtypes et méthodes.

---

## Array Mathematics

```python
#Arithmetic Operations
np.subtract(a, b)   # Subtraction
np.add(b, a)        # Addition
np.divide(a, b)     # Division
np.multiply(a, b)   # Multiplication
np.exp(b)           # Exponentiation
np.sqrt(b)          # Square root
np.sin(a)           # Print sines of an array
np.cos(b)           # Element-wise cosine
np.log(a)           # Element-wise natural logarithm
e.dot(f)            # Dot product

#Comparison
a == b               # Element-wise comparison
a < 2                # Element-wise comparison
np.array_equal(a, b) # Array-wise comparison

#Aggregate Functions
a.sum()          # Array-wise sum
a.min()          # Array-wise minimum value
b.max(axis=0)    # Maximum value of an array row
b.cumsum(axis=1) # Cumulative sum of the elements
a.mean()         # Mean
np.median(b)     # Median
np.corrcoef(a)   # Correlation coefficient
np.std(b)        # Standard deviation
```

**Explications — intérêt :**

- Toutes ces **opérations sont vectorisées** → énormes gains de perf vs boucles Python
- Les **reductions** (`sum`, `mean`, `std`, etc.) peuvent prendre `axis=` pour agréger par dimension (colonnes/lignes).
- `dot` = produit matriciel (multiplication linéaire).
- ⚠️ `log/exp/divide` : attention aux **zéros** et valeurs négatives → NaN/inf.

---

## Subsetting, Slicing, Indexing

```python
#Subsetting
a[2]      # 3
b[1,2]    # 6.0
```

**Explications — intérêt :** indexation directe (accès O(1)). Sur 2D : `[row, col]`.

```python
#Slicing
a[0:2]        # array([1, 2])
b[0:2,1]      # array([2., 5.])
b[:1]         # array([[1.5, 2., 3.]])
c[1,...]      # array([[[3., 2., 1.],[4., 5., 6.]]])
a[::-1]       # array([3, 2, 1])
```

**Explications — intérêt :**

- Les _slices_ sont des **vues** (pas des copies) → ultra rapide, **modifie l’original** si on assigne.
- `...` (ellipsis) remplace “toutes les dimensions restantes”.

```python
#Boolean Indexing
a[a<2]   # array([1])
```

**Explications — intérêt :**

- Les **masques booléens** filtrent les données façon SQL (`WHERE`).
- ⚠️ retourne **une copie** (sauf si utilisé à gauche d’une assignation : `a[a<2]=...` modifie `a`).

```python
#Fancy Indexing
b[[1, 0, 1, 0],[0, 1, 2, 0]]
# array([ 4. , 2. , 6. , 1.5])

b[[1, 0, 1, 0]][:,[0,1,2,0]]
# array([[ 4. , 5. , 6. , 4. ],
#        [ 1.5, 2. , 3. , 1.5],
#        [ 4. , 5. , 6. , 4. ],
#        [ 1.5, 2. , 3. , 1.5]])
```

**Explications — intérêt :**

- **Indexation avancée** par listes d’indices (réordonne/sélectionne n’importe quels éléments).
- ⚠️ **toujours une copie** → pas de modification in-place sauf si l’indexation est à gauche.

```python
a.sort()         # Sort an array
c.sort(axis=0)   # Sort along axis
```

**Explications — intérêt :**

- Tri **in-place** (modifie l’array). `axis` contrôle la dimension triée. Pour un tri sans modifier, utilise `np.sort(a)`.

---

## Array Manipulation

```python
###Transposing Arrays

i = np.transpose(b)
i.T   # Permute array dimensions
```

**Explications — intérêt :**

- Transposer permute les axes (colonne ↔ ligne), essentiel pour algèbre linéaire (cohérence des shapes).
    

```python
### Changing Array Shape

b.ravel()           # Flatten
g.reshape(3,-2)     # Reshape
h.resize((2,6))     # Resize
```

**Explications — intérêt :**

- `ravel()` **aplatit** (vue si possible → rapide).
    
- `reshape` remodèle **sans copier** si compatible (met `-1` pour laisser NumPy déduire).
    
- `resize` change la **taille** _et_ peut remplir/tronquer (modifie l’array, ⚠️ à manier avec soin).
    

```python
### Adding/Removing Elements

np.append(h,g)
np.insert(a, 1, 5)
np.delete(a,[1])
```

**Explications — intérêt :**

- Opérations **non vectorielles** qui **créent de nouveaux arrays** (coûteux). À éviter dans des boucles — préfère pré-allouer ou concaténer par batch.
    

```python
### Combining Arrays

np.concatenate((a,d),axis=0)  # Concatenate
np.vstack((a,b))              # Stack vertically
np.r_[e,f]                    # Row-wise stack
np.hstack((e,f))              # Stack horizontally
np.column_stack((a,d))        # Column-wise stack
np.c_[a,d]                    # Column-wise concat
```

**Explications — intérêt :**

- Fusionner des arrays pour **assembler des datasets / features**.
    
- `vstack/hstack/column_stack` sont des wrappers pratiques autour de `concatenate`.
    

```python
### Splitting Arrays

np.hsplit(a,3)
# [array([1]), array([2]), array([3])]

np.vsplit(c,2)
# [array([[[1.5, 2., 1.],[4., 5., 6.]]]),
#  array([[[3., 2., 3.],[4., 5., 6.]]])]
```

**Explications — intérêt :**

- Découper des arrays en **blocs** (train/test, colonnes/features).
    
- `hsplit` coupe **horizontalement** (colonnes), `vsplit` **verticalement** (lignes).
    
