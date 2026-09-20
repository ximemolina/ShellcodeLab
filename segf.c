// gcc -w -fno-pie -static -O0 -fno-stack-protector -z execstack -ggdb -mpreferred-stack-boundary=4 segf.c

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int not_executed() {
  printf("******** Esta funcion no se ejecuta a menos que **********\n");
  exit(2);
}

int main(int count, char *arg[]) {
  char buffer[50];

  if (count < 2) {
    printf("Se debe ingresar texto como entrada. Saliendo...\n");
    exit(1);
  }

  strcpy(buffer, arg[1]);
  printf("Yo soy main() y no ejecuto ninguna otra funcion.\n");

  return 0;
}
