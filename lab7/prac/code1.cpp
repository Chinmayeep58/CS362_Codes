#include <mpi.h>
#include <iostream>
using namespace std;

int main(int agrc, char** argv){
    MPI_Init(&argc, &argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    // MPI_Comm_rank(MPI_COMM_WORLD, &rank)
    int order_amt;
    MPI_Status status; // contains info about the source process, message tag and errors
    // used in mpi_recv, mpi_wait etc.

    if(rank==0){
        order_amt=100;
        cout<<"manager sending order amount="<<order_amt<<endl;
        // MPI_Send(buffer, length of buffer, mpi datatype, dest process rank, tag, mpi_comm_world);
        MPI_Send(&order_amt, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        // MPI_Recv(buffer, length of buffer, mpi datatype, source process rank, tag, mpi_comm_world, status);
        MPI_Recv(&order_amt, 1, MPI_INT, 1, 1, MPI_COMM_WORLD, &status);

        cout<<"manager received final bill after discount: "<<order_amt<<endl;
    }
    else if(rank==1){

    }
    MPI_Finalize();
    return 0;

}

// MPI_Bcast(buffer, count of buffer elements, mpi datatype, root process rank, mpi_comm_world);