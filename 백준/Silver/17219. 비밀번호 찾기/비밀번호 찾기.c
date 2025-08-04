#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 1000
#define MAX_LEN 100

typedef struct Node {
    char key[MAX_LEN];
    char value[MAX_LEN];
    struct Node* next;
} Node;

Node* table[TABLE_SIZE];

unsigned int hash(const char* str) {
    unsigned int h = 0;
    while (*str) {
        h = (h * 31) + (unsigned char)(*str++);
    }
    return h % TABLE_SIZE;
}

void insert(const char* key, const char* value) {
    unsigned int idx = hash(key);
    Node* cur = table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0) {
            strcpy(cur->value, value);
            return;
        }
        cur = cur->next;
    }

    Node* new_node = malloc(sizeof(Node));
    strcpy(new_node->key, key);
    strcpy(new_node->value, value);
    new_node->next = table[idx];
    table[idx] = new_node;
}

char* get(const char* key) {
    unsigned int idx = hash(key);
    Node* cur = table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0)
            return cur->value;
        cur = cur->next;
    }
    return NULL;
}

void free_table() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* cur = table[i];
        while (cur) {
            Node* tmp = cur;
            cur = cur->next;
            free(tmp);
        }
        table[i] = NULL;
    }
}

int main(){
    int n,m = 0;    
    scanf("%d %d", &n,&m);
    char site1[21];
    char pw[21];
    for(int i = 0; i < n; i++){
        scanf("%s %s",site1,pw);
        insert(site1,pw);
    }
    char site2[21];
    for (int i = 0; i < m; i++){
        scanf("%s",site2);
        printf("%s\n",get(site2));
    }
    
}