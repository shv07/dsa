#include <iostream>
#include <string>
using namespace std;
// passes all the test cases of geeksforgeeks in 0.34s
int main() {
	//code
	int t; cin>>t;
	int *ans = (int*) calloc(t,sizeof(int));
	for(int tmp = 0; tmp<t; tmp++)
	{
	    int n; cin>>n;
	    int *ar = (int*) malloc(n*sizeof(int));
	    for(int i = 0;i<n;i++) 
	        cin>>ar[i];
	    int *leftmax = (int*) calloc(n,sizeof(int));
	    int *rightmax = (int*) calloc(n,sizeof(int));
	    
	    
	    leftmax[0] = ar[0];
	    rightmax[n-1] = ar[n-1];
	    for(int i = 1; i<n;i++)
	    {
	        if(ar[i]>leftmax[i-1])
	            leftmax[i] = ar[i];
	        else
	            leftmax[i] = leftmax[i-1];
	        
	        if (ar[n-1-i]>rightmax[n-1-i+1])
	            rightmax[n-1-i] = ar[n-1-i];
	        else
	            rightmax[n-1-i] = rightmax[n-1-i+1];
	    } 
	    
	    int count = 0;
	    for(int i=1;i<n-1;i++)
	    {
	        int m;
	        if(leftmax[i-1]<rightmax[i+1])
	            m = leftmax[i-1];
	        else
	            m = rightmax[i+1];
	        if (m>=ar[i])
	            count+=m-ar[i];
	       
	   
	    }
	    ans[tmp] = count;
	}
	for(int i=0;i<t;i++)
	    cout<<ans[i]<<"\n";
	return 0;
}
