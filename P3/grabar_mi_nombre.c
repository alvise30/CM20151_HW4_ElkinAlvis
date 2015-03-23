
#include <stdio.h>
#include <stdlib.h>

#define SHELLSCRIPT "\
#/bin/bash \n\
rec -c1 -b16 prueba.wav silence -l 0 1 00:00:03.00 1\% \n\
"
int main(){
  
  puts("Grabe su Nombre");
  system(SHELLSCRIPT);
  puts("Grabacion finalizada");
  
return 0;

}
