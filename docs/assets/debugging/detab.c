
#include <stdio.h>

#define TAB_WIDTH 4

char currentCharacter;

int spacesBeforeChar();
int processLine();

int main() {

   while(processLine() != -1);

   return 0;
}

int processLine() {
    int spacesNum;
    if((spacesNum = spacesBeforeChar()) != -1) {
        int tabs = spacesNum / TAB_WIDTH;
        int spaces = spacesNum % TAB_WIDTH;

        for (int i = 0; i < tabs; i++) 
            printf("\t");

        for (int i = 0; i < spaces; i++) 
            printf(" ");

        do {
            printf("%c", currentCharacter);
            if(currentCharacter == '\n')
                return 0;
        } while ((currentCharacter = getchar()) != EOF);

        // While loop exited, thus EOF recieved
        return -1;
        

    } else {
        // Reached EOF while reading in spaces
        return  -1;
    }
}

int spacesBeforeChar() {
    int counter = 0;
    while( (currentCharacter = getchar()) != EOF) {
        if(currentCharacter == ' ') {
            counter++;
        } else {
            return counter;
        }
    }
    return -1;
}

