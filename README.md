<p align="center">
  <img src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/banner.png" width="700" height="200">
</p>
<h1 align="center">Sorting-Algorithms-Visualizer</h1>

<div align="center">

  <a href="">![Repo Size](https://img.shields.io/github/repo-size/Kacper0199/Sorting-Algorithms-Visualizer?color=green)</a>
  <a href="">![Repo Elements](https://img.shields.io/github/directory-file-count/Kacper0199/Sorting-Algorithms-Visualizer?color=orange)</a>
  <a href="">![Version](https://img.shields.io/pypi/pyversions/pygame)</a>
  <a href="">![Last Commit](https://img.shields.io/github/last-commit/Kacper0199/Sorting-Algorithms-Visualizer?color=purple)</a>
  <a href="">![Repo Language](https://img.shields.io/github/languages/top/Kacper0199/Sorting-Algorithms-Visualizer?color=ff69b4)</a>

</div>

---

The purpose of this project is to visualize some fundamental sorting algorithms using simple functions and python module pygame.

---

- [1. Algorithms Preview](#1-algorithms-preview)
- [2. Installation](#2-installation)
- [3. Get Started](#3-get-started)
- [4. Contributing](#4-contributing)

## 1. Algorithms Preview

|Visualization|Algorithm|Best Time Complexity|Avg Time Complexity|Worst Time Complexity| 
|:------------------------------------------------------------------------------------------------------------------------------------------------------:|:---:|:---:|:---:|:---:|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/selection_sort.gif">       |  Selection sort  |$$n^{2}$$|$$n^{2}$$|$$n^{2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/insertion_sort.gif">       |  Insertion sort   |$$n$$|$$n^{2}$$|$$n^{2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/bubble_sort.gif">     |  Bubble sort   |$$n$$|$$n^{2}$$|$$n^{2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/cocktail_sort.gif">    |  Cocktail sort  |$$n$$|$$n^{2}$$|$$n^{2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/shell_sort.gif">           |   Shell sort   |$$nlogn$$|$$n^{4/3}$$|$$n^{3/2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/quick_sort.gif">  |   Quick sort    |$$nlogn$$|$$nlogn$$|$$n^{2}$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/merge_sort.gif">          |   Merge sort   |$$nlogn$$|$$nlogn$$|$$nlogn$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/heap_sort.gif">         |   Heap sort    |$$nlogn$$|$$nlogn$$|$$nlogn$$|
| <img width="400" height="250" alt="" src="https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/pictures/radix_sort.gif">  |   Radix sort   |$$n$$|$$n\frac{k}{d}$$|$$n\frac{k}{d}$$|

## 2. Installation

Copy the repository by forking and then downloading it using:

```bash
git clone https://github.com/<YOUR-USERNAME>/Sorting-Algorithms-Visualizer
```

Install requirements use:

```bash
cd Sorting-Algorithms-Visualizer
pip install -r requirements.txt
```

Run App:

```bash
cd Sorting-Algorithms-Visualizer
python3 main.py
```

## 3. Get Started

Running **_main.py_** you can sort array (in ascending order) represented by bars.

- Change number of elements in array by pressing left/right arrow keys:

       →  (increase size of array - up to 300 elements)
       
       ←  (decrease size of array - up to 10 elements)

- Select sorting algorithm by pressing:

     <kbd>1</kbd> : Selection sort
     
     <kbd>2</kbd> : Insertion sort
     
     <kbd>3</kbd> : Bubble sort
     
     <kbd>4</kbd> : Cocktail sort
     
     <kbd>5</kbd> : Shell sort
     
     <kbd>6</kbd> : Quick sort
     
     <kbd>7</kbd> : Merge sort
     
     <kbd>8</kbd> : Heap sort
     
     <kbd>9</kbd> : Radix sort

- Press <kbd>Enter</kbd> to start sorting

- To shuffle and create new array hit <kbd>Space</kbd>

## 4. Contributing

Feel free to contribute if you want to implement other sorting algorithms in **_algorithms.py_** or create better visualizer. **Please be sure to checkout [CONTRIBUTING](https://github.com/Kacper0199/Sorting-Algorithms-Visualizer/blob/main/CONTRIBUTING.md) if you want to help develop this project!**
