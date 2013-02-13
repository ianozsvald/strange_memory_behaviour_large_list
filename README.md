strange_memory_behaviour_large_list
===================================

odd memory behaviour, this repo is for understanding

$ python -m memory_profiler bug.py
Starting...
Length of y is 500, length of x is 500
Length of q 250000
0 items of garbage not collected
Finishing...
We see 32 bytes for a complex number
We can project that 250000 complex numbers will take 8000000 bytes
We see 2000072 bytes for a 250000 length array (which will not include the items it holds, just its size)
Press return to exit (and check ps maybe to see final size of this process)
Filename: bug.py

Line #    Mem usage    Increment   Line Contents
================================================
    39                             @profile
    40     9.367 MB     0.000 MB   def wrap_bug_to_see_deallocation():
    41     9.379 MB     0.012 MB       print "Starting..."
    42    35.215 MB    25.836 MB       q = bug()
    43    35.219 MB     0.004 MB       print "Length of q", len(q)
    44    33.309 MB    -1.910 MB       del q
    45    33.309 MB     0.000 MB       assert gc.isenabled()
    46    33.309 MB     0.000 MB       gc.collect()  # make sure we deallocate our object
    47    33.309 MB     0.000 MB       print "{} items of garbage not collected".format(len(gc.garbage))
    48    33.309 MB     0.000 MB       print "Finishing..."


Filename: bug.py

Line #    Mem usage    Increment   Line Contents
================================================
    14                             @profile
    15                             def bug():
    16     9.379 MB     0.000 MB   
    17     9.379 MB     0.000 MB       w = h = 1000
    18     9.379 MB     0.000 MB       x_step = (float(x2 - x1) / float(w)) * 2
    19     9.379 MB     0.000 MB       y_step = (float(y1 - y2) / float(h)) * 2
    20     9.379 MB     0.000 MB       x = []
    21     9.379 MB     0.000 MB       y = []
    22     9.379 MB     0.000 MB       ycoord = y2
    23     9.453 MB     0.074 MB       while ycoord > y1:
    24     9.453 MB     0.000 MB           y.append(ycoord)
    25     9.453 MB     0.000 MB           ycoord += y_step
    26     9.453 MB     0.000 MB       xcoord = x1
    27     9.531 MB     0.078 MB       while xcoord < x2:
    28     9.531 MB     0.000 MB           x.append(xcoord)
    29     9.531 MB     0.000 MB           xcoord += x_step
    30     9.531 MB     0.000 MB       print "Length of y is {}, length of x is {}".format(len(y), len(x))
    31     9.531 MB     0.000 MB       q = []
    32     9.574 MB     0.043 MB       for ycoord in y:
    33    35.215 MB    25.641 MB           for xcoord in x:
    34    35.215 MB     0.000 MB               q.append(complex(xcoord, ycoord))
    35                             
    36    35.215 MB     0.000 MB       return q

