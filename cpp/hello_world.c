int i;
int length = 5;
int max = 6;
int counters[length];
for (i=0; i<length; i++)
    counters[i] = 0;
for(;;) {
    for (i=length-1; i>=0; i--)
        printf("%d", counters[i]);
    printf("\n");
    for(i=0; i<length; i++) {
        counters[i]++;
        if (counters[i] < max)
            break;
        else
            counters[i] = 0;
    }
    if (i >= length)
        break;
}