#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *part_1 = "flag{this_isnt_";

char *make_flag_part(char *part_2) {
    char *parts_2_3;
    char *part_3 = "is_it?}";

    parts_2_3 = (char *) malloc(strlen(part_2) + strlen(part_3) + 1);
    sprintf(parts_2_3, "%s%s", part_2, part_3);

    return parts_2_3;
}

int main()
{
    char *parts_2_3;
    char *part_2 = "so_hard_";

    parts_2_3 = make_flag_part(part_2);

    if (0) {
        printf("%s%s\n", part_1, parts_2_3);
        free(parts_2_3);
    } else {
        printf("Disassemblers are pretty cool :D");
    }

	return 0;
}