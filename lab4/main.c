#include <stdio.h> 
#include <stdlib.h> 
#include <omp.h> 
#include <time.h> 
#define N 10 
 
int main() { 
    int A[N], result[N]; 
    srand(time(NULL)); 
    for(int i=0;i<N;i++) { 
        int unique; 
        do { 
            unique=rand()%50+1; 
            int duplicate=0; 
 
            for(int j=0;j<i;j++) { 
                if(A[j]==unique) { 
                    duplicate=1; 
                    break; 
                } 
            } 
 
            if(!duplicate) { 
                A[i]=unique; 
                break; 
            } 
 
        } while(1); 
    } 
 
    printf("Unsorted Array:\n"); 
    for(int i=0;i<N;i++) 
        printf("%d ", A[i]); 
    printf("\n\n"); 
 
    int seq[N]; 
    for(int i=0;i<N;i++) 
        seq[i]=A[i]; 
 
    long long seqShuffles=0; 
    double start=omp_get_wtime(); 
    int sorted=0; 
 
    while(!sorted) { 
        sorted=1; 
        for(int i=0; i<N-1;i++) { 
            if(seq[i]>seq[i+1]) { 
                sorted=0; 
                break; 
            } 
        } 
 
        if(!sorted) { 
            for(int i=0;i<N;i++) { 
                int j=rand()%N; 
                int temp=seq[i]; 
                seq[i]=seq[j]; 
                seq[j]=temp; 
            } 
            seqShuffles++; 
        } 
    } 
 
    double seqTime=omp_get_wtime()-start; 
 
    printf("Sequential Sorted Array:\n"); 
    for(int i=0;i<N;i++) 
        printf("%d ", seq[i]); 
    printf("\n"); 
    printf("Sequential Time: %.3f sec\n", seqTime); 
    printf("Sequential Shuffles: %lld\n\n", seqShuffles); 
 
    int threadList[3] = {2, 4, 8}; 
    double parTime[3]; 
    long long parShuffles[3]; 
 
    for(int t=0;t<3;t++) { 
 
        int T=threadList[t]; 
        omp_set_num_threads(T); 
 
        int found=0; 
        long long totalShuffles=0; 
 
        start=omp_get_wtime(); 
 
        #pragma omp parallel shared(found, result, totalShuffles) 
        { 
            int local[N]; 
            for(int i=0;i<N;i++) 
                local[i]=A[i]; 
 
            long long localShuffles=0; 
            int sorted; 
 
            while(!found) { 
                sorted=1; 
                for(int i=0;i<N-1;i++) { 
                    if(local[i]>local[i+1]) { 
                        sorted=0; 
                        break; 
                    } 
                } 
 
                if(sorted) { 
                    #pragma omp critical 
                    { 
                        if(!found) { 
                            for(int i=0;i<N;i++) 
                                result[i]=local[i]; 
                            found=1; 
                        } 
                    } 
 
                } else { 
                    for(int i=0;i<N;i++) { 
                        int j=rand()%N; 
                        int temp=local[i]; 
                        local[i]=local[j]; 
                        local[j]=temp; 
                    } 
 
                    localShuffles++; 
                } 
            } 
 
            #pragma omp atomic 
            totalShuffles+=localShuffles; 
        } 
 
        parTime[t]=omp_get_wtime()-start; 
        parShuffles[t]=totalShuffles; 
 
        printf("Parallel Run (Threads = %d)\n", T); 
        printf("Sorted Array:\n"); 
        for(int i=0;i<N;i++) 
            printf("%d ", result[i]); 
        printf("\n"); 
        printf("Time Taken: %.3f sec\n", parTime[t]); 
        printf("Total Shuffles: %lld\n\n", parShuffles[t]); 
    } 
 
    printf("Summary Table:\n"); 
    printf("Threads\tTime\tShuffles\tSpeedup\n"); 
 
    for(int t=0;t<3;t++) { 
        double speedup=seqTime/parTime[t]; 
         printf("%d\t%.3f\t\t%lld\t\t%.2f\n",  threadList[t],  parTime[t], 
parShuffles[t], speedup); 
    } 
 
    return 0; 
} 