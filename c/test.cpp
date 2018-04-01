#include <iostream>
#include <time.h>
int main(){
	clock_t tStart= clock();
	// printf("%.2f",(double)(clock()-tStart)/CLOCKS_PER_SEC);

	std::string s1[5]={};
	int lenS1= sizeof(s1)/sizeof(*s1);
	for (int i; i<lenS1; i++){
		// printf("%.2f",(double)(clock()-tStart)/CLOCKS_PER_SEC);
		if((double)(clock()-tStart)/CLOCKS_PER_SEC> 2.0){
			break;	
		} 
		else{
			// toSolve:1> once inside, cannot break
			std::cin>>s1[i];
		}
	}
	for(std::string s: s1){
		if(s.compare("")==0) break;
		std::cout<<s;
		if(s.compare("")!=0) std::cout<<std::endl;
		// toSolve:2> list line no endl !!
	}
	// std::cout<<"whatHappened?"; 덯어씌우기가 안됨! ~ c__ single file.subilme-build
	return 0;	
}