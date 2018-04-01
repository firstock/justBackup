#include <iostream>
int main(){
	std::string s1[3]={};
	int lenS1= sizeof(s1)/sizeof(*s1);
	for (int i; i<lenS1; i++){
		std::cin>>s1[i];
	}
	for(std::string s: s1){
		std::cout<<s<<std::endl<<std::endl;
	}
	// std::cout<<"whatHappened?"; 덯어씌우기가 안됨!
	return 0;	
}