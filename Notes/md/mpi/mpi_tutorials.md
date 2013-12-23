#Message Passing Interface(MPI)
##Introduction
The goal of the Message Passing Interface is to establish a portable, efficient, and flexible standard for message passing that will be widely used for writing message passing programs. 
*MPI is a specification for the developers and users of message passing libraries. By itself, it is NOT a library - but rather the specification of what such a library should be.
*MPI primarily addresses the message-passing parallel programming model: data is moved from the address space of one process to that of another process through cooperative operations on each process.


##General MPI Program Structure
1. MPI include file
2. BEGIN
2. Some Declarations, prototypes, etc.
3. Serial Code
4. Initialize MPI environment[Parallel code begins]
5. Do work & make message passing calls
6. Terminate MPI environment[Parallel code ends]
7. Serial Code
8. END

##Header File
Required for all programs tha make MPI library calls.

<code>C inclue file</code>
<pre>
	#include "mpi.h"
</pre>
<code> Fortran include file</code>
<pre>
	#include "mpif.h"
</pre>

##Communicators and Groups
* MPI uses objects called communicators and groups to define which collection of processes may communicate with each other.
* Most MPI routines require you to specify a communicator as an argument.

##Rank
* Within a communicator, every process has its own unique, integer identifier assigned by the system when the process initializes. A rank is sometimes also called a "task ID". Ranks are contiguous and begin at zero.
* Used by the programmer to specify the source and destination of messages. Often used conditionally by the application to control program execution (if rank=0 do this / if rank=1 do that).

##Error Handling
* Most MPI routines include a return/error code parameter.
* However, according to the MPI standard, the default behavior of an MPI call is to abort if there is an error. This means you will probably not be able to capture a return/error code other than MPI_SUCCESS.
* How to override the default error handler, you could find something useful <a href="https://computing.llnl.gov/tutorials/mpi/errorHandlers.pdf">hear</a>.

##Environment Management Routines
This group of routines is used for interrogating(查询) and setting the MPI execution environment, and covers an assortment of purposes（各种各样的目的）, such as initializing and terminating the MPI environment, querying a rank's identity, querying the MPI library's version, etc. Most of the commonly used ones are described below.

###MPI_Init
Initializes the MPI execution environment. This function must be called in every MPI program, must be called <code>before any other MPI functions</code> and must be called <code>only once</code> in an MPI program. For C programs, <code>MPI_Init</code> may be used to pass the command line arguments to all processes, although this is not required by the standard and is implementation dependent.
<pre>
MPI_Init (&argc,&argv) 
MPI_INIT (ierr)
</pre>

###MPI_Comm_size
Returns the <code>total number</code> of MPI processes in the specified communicator, such as <code>MPI_COMM_WORLD</code>. If the communicator is <code>MPI_COMM_WORLD</code>, then it represents the number of MPI tasks available to your application.
<pre>
MPI_Comm_size (comm,&size) 
MPI_COMM_SIZE (comm,size,ierr)
</pre>

###MPI_Comm_rank
Returns the <code>rank</code> of the calling MPI process within the specified communicator. Initially, each process will be assigned a unique integer rank <code>between 0 and number of tasks - 1</code> within the communicator <code>MPI_COMM_WORLD</code>. This rank is often referred to as a task ID. If a process becomes associated with other communicators, it will have a unique rank within each of these as well.
<pre>
MPI_Comm_rank (comm,&rank) 
MPI_COMM_RANK (comm,rank,ierr)
</pre>

###MPI_Abort
Terminates all MPI processes associated with the communicator. In most MPI implementations it terminates All processes regardless of the communicator specified.
<pre>
MPI_Abort(comm, errorcode)
MPI_ABORT(comm,  errorcode, ierr)
</pre>

###MPI_Get_processor_name
Returns the processor name. Also returns the length of the name. The buffer for "name" must be at least <code>MPI_MAX_PROCESSOR_NAME</code>characters in size. What is returned into "name" is implementation dependent-may not be the same as the output of the "hostname" or "host" shell commands.
<pre>
MPI_Get_processor_name(&name, &resultlength)
MPI_GET_PROCESSOR_NAME(name, resultlength, ierr)
</pre>

###MPI_Initialized
Indicates whether MPI_Init has been called - returns flag as either logical true (1) or false(0). MPI requires that MPI_Init be called once and only once by each process. This may pose a problem for modules that want to use MPI and are prepared to call MPI_Init if necessary. MPI_Initialized solves this problem.
<pre>
MPI_Initialized (&flag)
MPI_INITIALIZED (flag, ierr)
</pre>

###MPI_Wtime
Returns an elapsed wall clock time in seconds (double precision) on the calling processor.
<pre>
MPI_Wtime ()
MPI_WTIME ()
</pre>

###MPI_Wtick
Returns the resolution in seconds (double precision) of MPI_Wtime.
<pre>
MPI_Wtick ()
MPI_WTICK ()
</pre>

###MPI_Finalize
Terminates the MPI execution environment. This function should be the last MPI routine called in every MPI program - no other MPI routines may be called after it.
<pre>
MPI_Finalize ()
MPI_FINALIZE (ierr)
</pre>

