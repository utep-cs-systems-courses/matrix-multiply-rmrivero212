# Parallel Matrix Multiply Report

## Assignment Details

This assignment took just a couple of days to complete. The actual parallel
implementatino didn't come right away since I was having a bit of trouble
understanding the concept. However, after studying the coding examples
provided and reviewing the nyMP cheat sheet I was able to add a simple bit or
parallelism into my matrix mutliply method.

## Problems Encountered

Although I was technically able to parallize the matrix mutliply there was an
issue that I ran into that didn't affect the output time wise but more like
the resulting matrix. Where I struggled was in the implementation of creating
a shared system where the individual processes could share the data within the
matrices that they were assigned to. For example the resulting matrix would
have the top half filled with numbers while the bottom half of the matrix
would be filled with nothing but zeros. I would soon come to learn that this
was because I hadn't marked the parallelism as shared. So that is one bug that
I could not solve but overall the program runs just about as expected with no
errors and a reasonable output of time when compared to the regular matrix
mutliply.

## Performance Measurements

When it came to altering the amount of threads being ran simultaneously the
results were a little bit everywhere with some times resulting in very little
speed up in performance. Sometimes there were times outputed that had little
to no deviation but I will let the actual results speak for themselves:

Key: * MM  == Matrix Multiply
     * MMP == Matrix Multiply Parallel
(These times were calculated through a 128 X 128 matrix multiplication. Both
matrices contained only the value of 2 accross all rows and columns. Time
results are calculated in Monotonic time)
1 Thread:
  * MM  Time: 6.0182
  * MMP Time: 5.8096
2 Threads:
  * MM  Time: 6.0885
  * MMP Time: 5.0638
4 Threads:
  * MM  Time: 6.0583
  * MMP Time: 2.6925
8 Threads:
  * MM  Time: 6.0092
  * MMP Time: 2.6844

As shown above, the time differences were almost slightly changed when threads
began to be added. Once the 4 thread threshold is passed that is when we see
the parallel matrix multiply time essentially execute twice as fast as the
regular matrix mutliply. The regular matrix multiplies time remained almost
constant which is excpected since it does not use the power of multiple
processes. Although the resulting matrix may not be correct, this experiment
does show the time differences when it comes to executing computations in both
parallel and non-parallel settings.

## Final Observations

This was a simple case where parallel computing sped up the execution time and
performed more efficiently rather than a regular concurrent execution. On
larger scales it is true that parallel computing is a thing of the future that
all modern machines should utilize when making efforts towards faster
computing. This was a fun little experiment.
