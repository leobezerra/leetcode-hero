# Sweep Line Algorithm
In computational geometry, a **sweep line algorithm** or **plane sweep algorithm** is an algorithmic paradigm that uses a conceptual sweep line or sweep surface to solve various problems in Euclidean space. It is one of the key techniques in computational geometry.

The idea behind algorithms of this type is to imagine that a line (often a vertical line) is swept or moved across the plane, stopping at some points. Geometric operations are restricted to geometric objects that either intersect or are in the immediate vicinity of the sweep line whenever it stops, and the complete solution is available once the line has passed over all objects.

In mathematics, a **[Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram)** is a partition of a plane into regions close to each of a given set of objects. In the simplest case, these objects are just finitely many points in the plane (called seeds, sites, or generators). For each seed there is a corresponding region consisting of all points of the plane closer to that seed than to any other. These regions are called Voronoi cells. The Voronoi diagram of a set of points is dual to its Delaunay triangulation.

![Animation of Fortune's algorithm, a sweep line technique for constructing Voronoi diagrams.](https://upload.wikimedia.org/wikipedia/commons/2/25/Fortunes-algorithm.gif)
##### [From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Sweep_line_algorithm)

## Problems
1. [Maximum Intervals Overlap](geeks-for-geeks/README.md)
+ Level: Medium 
2. [Rectangle Area](leetcode/README.md)
+ Level: Medium 
3. [Rectangle Overlap](leetcode/README.md)
+ Level: Easy 

## Implementations:
+ C++
+ Python 3

## Disclaimer
> This material was used in the course SPECIAL TOPICS IN COMPUTER XIV - Programming Interviewing Practices of the Digital Metropolis Institute of the Federal University of Rio Grande do Norte.

Authors:
+ [Giovanne Santos](https://github.com/gsdante)
+ [Marlus Marcos](https://github.com/marlusmarcos)
+ [Thiago Silva](https://github.com/silva-thiago)
+ [Yan Carlos](https://github.com/yandl5)

<- [BACK TO HOME](../README.md)