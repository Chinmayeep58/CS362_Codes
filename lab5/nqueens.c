#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 8

int isSafe(int board[], int row, int col){
    for (int i=0;i<row;i++){
        int prevCol=board[i];
        if (prevCol==col){
            return 0;
        }
        if(abs(prevCol-col)==abs(i-row)){
            return 0;
        }
    }
    return 1;
}

void solve(int row, int board[], int *count){
    if (row==N){
        (*count)++;
        return;
    }

    for(int col=0;col<N;col++){
        if(isSafe(board, row, col)){
            board[row]=col;
            solve(row + 1, board, count);
        }
    }
}

int main(){
    int totalSolutions=0;
    double start, end;
    start=omp_get_wtime();

    #pragma omp parallel for reduction(+:totalSolutions)
    for (int col=0;col<N;col++){
        int board[N];
        int localCount=0;
        board[0]=col;
        solve(1, board, &localCount);
        totalSolutions+=localCount;
    }

    end = omp_get_wtime();
    printf("Total number of solutions for %d-Queens: %d\n", N, totalSolutions);
    printf("Execution time: %f seconds\n", end - start);
    return 0;
}