# flag_shop

## Description

There's a flag shop selling stuff, can you buy a flag?

## Solution

Launch the instance, download the soruce code before connecting to the machine. Analyse the source code, it has a exploit point, i.e
```
int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }
```
It consist of a vulnerability called integer overflow/signed integer overflow where the value produced after operation exceeds the storage capacity of the variable intended to hold.

Basically what it means is, since ```int``` is 32-bit signed, the maximum value it can hold is 2147483647. which divided by 900 gives 2386092. That means if a number higher than 2386092 is given as the input for number of flags. the cost becomes negative.

By turning cost negative, the total account balance increases.
```
account_balance= account_balance - (-total_cost) -> account_balance+total_cost
```
After analysis, connect to the machine using netcat/nc and use the option to buy flags and the option to buy "Defintely not the flag Flag". Enter the value of number of flags 2390000 and use "check account balance". use the option to buy flags and this time use "1337 Flag"

Flag for the challenge is displayed.
