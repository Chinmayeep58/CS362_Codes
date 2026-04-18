#include <stdio.h>
#include <omp.h>
#include <time.h>
#include <stdlib.h>
#define n 10

int main(){
    int arr[n];
    int res[n];
    srand(time(NULL));
    // selecting non repeating elements for the array
    for(int i=0;i<n;i++){
        int unique;
        do{
            unique=rand()%50+1;
            int duplicate=0;
            for(int j=0;j<i;j++){
                if(arr[j]==unique){
                    duplicate=1;
                    break;
                }
            }
            if(!duplicate){
                arr[i]=unique;
                break;
            }
        }
        while(1);
    }

    printf("Unsorted array: \n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");

    int seq[n];
    for(int i=0;i<n;i++){
        seq[i]=arr[i];
    }

    long long shuffles=0;
    double start=omp_get_wtime();
    int sorted=0;
    while(!sorted){
        sorted=1;
        // check if any element breaks the sorting rule
        for(int i=0;i<n-1;i++){
            if(seq[i]>seq[i+1]){
                sorted=0;
                break;
            }
        }
        // applying bogo sort if still not sorted
        if(!sorted){
            for(int i=0;i<n;i++){
                int j=rand()%n;
                int temp=seq[i];
                seq[i]=seq[j];
                seq[j]=temp;
            }
            // increment the number of shuffles
            shuffles++;
        }
    }
    double seqtime=omp_get_wtime()-start;
    printf("seq sorting time:%.3f \n",seqtime);
    printf("seq sorting shuffles:%lld \n",shuffles);

    int tlist[3]={2,4,8};
    double paratime[3];
    long long parashuffles[3];

    for(int t=0;t<3;t++){
        int th=tlist[t];
        omp_set_num_threads(th);
        int found=0;
        long long totshuffles=0;
        start=omp_get_wtime();
        #pragma omp parallel shared(found, res, totshuffles)
        {
            int local[n];
            for(int i=0;i<n;i++){
                local[i]=arr[i];
            }
            long long currshuffles=0;
            int sorted=0;
            while(!found){
                sorted=1;
                for(int i=0;i<n-1;i++){
                    if(local[i]>local[i+1]){
                        sorted=0;
                        break;
                    }
                }
                if(sorted){
                    #pragma omp critical
                    {
                        if(!found){
                            for(int i=0;i<n;i++){
                                res[i]=local[i];
                            }
                            found=1;
                        }
                    }
                }
                else{
                    for(int i=0;i<n;i++){
                        int j=rand()%n;
                        int temp=local[i];
                        local[i]=local[j];
                        local[j]=temp;
                    }
                    currshuffles++;
                }
            }
            #pragma omp atomic
            totshuffles+=currshuffles;
        }
        paratime[t]=omp_get_wtime()-start;
        parashuffles[t]=totshuffles;
        printf("for %d threads\n",th);
        printf("time taken is: %.3f\n",paratime[t]);
        printf("total shuffles are: %lld\n",parashuffles[t]);
    }
    return 0;
}