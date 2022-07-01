#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#define N_RAND 4
typedef unsigned int uint;

void print_flag() {
	char flag[64];
	FILE* f;

	f = fopen("flag", "r");
	if (f == NULL) {
		perror("Could not open your flag :C");
		exit(1);
	}

	if (!fgets(flag, sizeof(flag), f)) {
		perror("Could not read your flag :C");
		exit(1);
	}	

	printf("Here is your flag: %s\n", flag);
}

void gen_random_nums(uint *nums, int length)
{
    int i;

    srand(time(NULL));
    for(i = 0; i < length; i++)
    {
        nums[i] = rand();
    }
}

void validate_code(uint code, uint *nums, int length)
{
    uint test_code = 0x1337beef;
    int i;

    for (i = 0; i < length; i++) {
        test_code += nums[i] >> 7;
    }

    for (i = 0; i < length; i++) {
        test_code |= nums[i] >> 16;
        test_code |= (nums[i] & 0xffff) << 16;
    }

    for (i = 0; i < length; i++) {
        test_code ^= nums[i];
    }

    if (code == test_code) {
        puts("\n()()()() CODE ACCEPTED ()()()()");
        print_flag();
    } else {
        puts("\n)(-)(-)( CODE REJECTED )(-)(-)(");
    }
}

void system_init()
{
    uint rand_nums[N_RAND];
    uint code;
    int i;
    
    gen_random_nums(rand_nums, N_RAND);
    puts("------------d--------3-------------c-");
    puts("--6----2--------------------7--------");
    puts("------------ DOOR LOCKED -------b----");
    puts("-----1--e------------4------9--------");
    puts("--5------0------f----------------a---");
    for (i = 0; i < 37; i++) {
        printf(".");
        fflush(stdout);
        //sleep(1);
    }
    puts("\n\n:::::: SYSTEM CORE MALFUNCTION ::::::");
    for (i = 1; i < N_RAND + 1; i++)
    {
        printf("------- CORE VALUE %d: %d\n", i, rand_nums[i-1]);
    }
    puts("<<<< Oh well, we will do it live <<<<");
    for (i = 0; i < 37; i++) {
        printf(".");
        fflush(stdout);
        //sleep(1);
    }
    puts("\n\n>>>> ENTER VALIDATION CODE >>>>");
    printf("CODE: ");
    fflush(stdout);
    scanf("%d", &code);

    validate_code(code, rand_nums, N_RAND);
}

int main()
{
    system_init();
	return 0;
}