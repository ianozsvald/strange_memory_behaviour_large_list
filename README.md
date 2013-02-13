strange_memory_behaviour_large_list
===================================

odd memory behaviour, this repo is for understanding

    $ python -m memory_profiler bug.py

See output.txt for a full stdout grab. This program allocates 250,000 complex numbers and consumes 25MB of RAM rather than the projected 10MB - if you can give me guidance on what's happening, I'd be very happy.
