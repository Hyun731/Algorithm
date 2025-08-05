#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 1000
#define MAX_LEN 100
#define MAX_N 500000

typedef struct Node {
    char key[MAX_LEN];
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

void insert(const char* value) {
    unsigned int idx = hash(value);
    Node* cur = table[idx];
    while (cur) {
        if (strcmp(cur->key, value) == 0) {
            return;
        }
        cur = cur->next;
    }

    Node* new_node = malloc(sizeof(Node));
    strcpy(new_node->key, value);
    new_node->next = table[idx];
    table[idx] = new_node;
}

int get(const char* key) {
    unsigned int idx = hash(key);
    Node* cur = table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0)
            return 1;
        cur = cur->next;
    }
    return 0;
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
char matched[MAX_N][21];
int main(){
    int n, m;
    char a[21];
    int cnt = 0;

    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        scanf("%s", a);
        insert(a);
    }

    for (int i = 0; i < m; i++) {
        scanf("%s", a);
        if (get(a)) {
            strcpy(matched[cnt++], a);
        }
    }
    qsort(matched, cnt, sizeof(matched[0]), strcmp);
    printf("%d\n", cnt);
    for (int i = 0; i < cnt; i++) {
        printf("%s\n", matched[i]);
    }

    free_table();
    return 0;
}