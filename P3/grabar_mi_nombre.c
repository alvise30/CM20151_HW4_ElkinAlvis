
#include <stdio.h>
#include <stdlib.h>

#define SHELLSCRIPT "\
#/bin/bash \n\
arecord -d 3 prueba.wav \n\
"
int main(){
  
  puts("Grabe su Nombre");
  system(SHELLSCRIPT);
  puts("Grabacion finalizada");
  return 0;

}
