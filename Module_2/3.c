#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>

bool signalReceived = false; 

void myHandle(int mySignal)
{
	//printf("myHandle with signal %d\n", mySignal); 
	if(mySignal == 2)
	{
		if(signalReceived == false)
		{
			signalReceived = true; 
		}
		else
		{
			signalReceived = false; 
		}
	}
	else if(mySignal == 10)
	{
		printf("Exit status: 0 \n"); 
		exit(0); 
	}
	else
	{
		printf("Signal received: %d\n", mySignal); 
	}
}

int main(int argc, char *argv[])
{
	int i = 0; 
	signal(SIGINT, myHandle); 
	signal(SIGUSR1, myHandle);  

	while(1)
	{
		if(signalReceived == true)
		{
			printf("Iteration: i = %d\n", i); 
		}

		i++; 
		sleep(2); 
	}

	return 0; 
}
