// #include <stdio.h>
// int main(int a, char** b){printf("%d",a-*b[0]+96); return 0;}
// int main(int a, char** b){return a-*b[0]-94;}
#include <stdio.h>
int main(){int a,b; scanf("%d%d",&a,&b); putc("%d",a-b); return 0;}