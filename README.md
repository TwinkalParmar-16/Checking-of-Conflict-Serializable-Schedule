# Checking of Conflict Serializable Schedule

This program reads a concurrent schedule involving n transaction with read and write
instructions on data items from an input file (sample input file attached) and find
whether the schedule is Conflict Serializable or not using the graph-based method. 
In case of conflict serializable schedule, program will give the serializability order 
and for non-serializable schedule, give the cycle(s) present in the graph.
This program is able to handle any finite number of transactions and data items.
There is not any constraints on number of transactions and data items.
