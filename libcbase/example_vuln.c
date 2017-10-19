#include    <stdio.h>

void vuln (const char* arg){
	char buffer[100];
	strcpy(buffer, arg);
}

int main (int argc, char **argv){
	vuln(argv[1]);
		return 0;
}
