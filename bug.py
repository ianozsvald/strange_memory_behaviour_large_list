"""Demonstrate not-yet-understood memory allocation behaviour"""
import sys
import gc
x1, x2, y1, y2 = -2.13, 0.77, -1.3, 1.3

# Requirements:
# psutil (optional - it makes memory_profiler run faster)
# memory_profiler

# Usage:
# $ python -m memory_profiler bug.py


@profile
def bug():

    w = h = 1000
    x_step = (float(x2 - x1) / float(w)) * 2
    y_step = (float(y1 - y2) / float(h)) * 2
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    print "Length of y is {}, length of x is {}".format(len(y), len(x))
    q = []
    for ycoord in y:
        for xcoord in x:
            q.append(complex(xcoord, ycoord))

    return q


@profile
def wrap_bug_to_see_deallocation():
    print "Starting..."
    q = bug()
    print "Length of q", len(q)
    del q
    assert gc.isenabled()
    gc.collect()  # make sure we deallocate our object
    print "{} items of garbage not collected".format(len(gc.garbage))
    print "Finishing..."


if __name__ == "__main__":
    wrap_bug_to_see_deallocation()

    complex_nbr = complex(1.0, 2.0)
    bytes_for_complex = sys.getsizeof(complex_nbr)
    print "We see {} bytes for a complex number".format(bytes_for_complex)
    NBR_ITEMS = 250000
    print "We can project that {} complex numbers will take {} bytes".format(NBR_ITEMS, NBR_ITEMS*bytes_for_complex)
    large_list_of_complex = [complex_nbr] * NBR_ITEMS
    bytes_for_large_list_of_complex = sys.getsizeof(large_list_of_complex)
    print "We see {} bytes for a {} length array (which will not include the items it holds, just its size)".format(bytes_for_large_list_of_complex, NBR_ITEMS)

    raw_input("Press return to exit (and check ps maybe to see final size of this process)")
