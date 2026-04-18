#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#define n 8

int issafe(int board[], int row, int col){
    for(int i=0;i<row;i++){
        int prev=board[i];
        // checking for same col
        if(prev==col){
            return 0;
        }
        // checking for same diagonal
        if(abs(prev-col)==abs(i-row)){
            return 0;
        }
    }
    return 1;
}

void solve(int row, int board[], int *count){
    if(row==n){
        (*count)++;
        return;
    }
    for(int i=0;i<n;i++){
        if(issafe(board,row,i)){
            board[row]=i;
            solve(row+1,board,count);
        }
    }
}

int main(){
    int total=0;
    double start=omp_get_wtime();
    #pragma omp parallel for reduction(+:total)
    for(int i=0;i<n;i++){
        int board[n];
        int local=0;
        board[0]=i;
        solve(1,board,&local);
        total+=local;
    }
    double time=omp_get_wtime()-start;
    printf("total number of solutions: %d\n",total);
    printf("time taken: %.3f\n",time);
    return 0;
}