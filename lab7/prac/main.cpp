#include <iostream>
#include <mpi.h>
using namespace std;

typedef long long ll;
ll grider(ll seed, ll m, ll a, ll mod, ll n){
    ll r=seed;
    for(int i=0;i<n;i++){
        r=(r*m+a)%mod;
    }
    return r;
}

int main(int argc, char** argv){
    MPI_Init(&argc, &argv);
    int rank;
    int size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(size!=2){
        if(rank==0){
            count<<"run with 2 process only";
            MPI_Finalize(); // terminates the mpi environment
            return 0;
        }
    }

    ll a=1098;
    ll b=1023;
    const ll n=2000000000LL;
    ll alpha, beta;
    double start=MPI_Wtime();
    if(rank==0){
        ll alpha1=grinder(a,31,17,9973,n);
        ll alpha2=grinder(alpha1,37,11,9973,n);
        alpha=(alpha1+alpha2)%9973;
        MPI_Send(&alpha,1,MPI_LONG_LONG,1,0,MPI_COMM_WORLD);
        MPI_Recv(&beta,1,MPI_LONG_LONG,1,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        ll verify=grinder(alpha+beta,7,3,101,n);
        ll r=grinder(alpha*beta+a+b,13,7,9973,n);
        ll password=r%10000;
        double time=MPI_Wtime()-start;
        cout<<"alpha "<<alpha<<endl;
        cout<<"beta "<<beta<<endl;
        cout<<"verification (p1) "<<verify<<endl;
        cout<<"time taken "<<time<<"seconds\n";
    }
    else{
        MPI_Recv(&alpha,1,MPI_LONG_LONG,0,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        ll beta1=grinder(alpha,b,13,9973,n);
        ll beta2=grinder(beta1,4,19,9973,n);
        beta=(beta1+beta2)%9973;
        MPI_Send(&beta,1,MPI_LONG_LONG,0,0,MPI_COMM_WORLD);
        ll verify=grinder(alpha+beta,7,3,101,n);
        cout<<"verification (p2)"<<verify<<endl;
    }
    MPI_Finalize();
    return 0;
}