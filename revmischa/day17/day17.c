#include <stdio.h>
#include <stdlib.h>

#pragma mark types
typedef unsigned item;
typedef struct node_ {
  item val;
  struct node_ *next;
} node;

#pragma mark config
#define PART2

#pragma mark globals
#ifdef PART2
unsigned stepcount = 50000000;
#else
unsigned stepcount = 2017;
#endif
unsigned stepsize = 324;
unsigned pos = 0;
node head = {.val=0, .next=NULL};
unsigned size = 1;
unsigned used = 0;

// pre-alloc all the nodes we need
size_t nodesize = sizeof(struct node_);
node* nodes;

node* get_idx(unsigned idx) {
  unsigned i = 0;
  node *n = &head;
  while (i < size && n->next != NULL) {
    if (i == idx)
      return n;
    i++;
    n = n->next;
  }

  return NULL;
}

node* find_val(item val) {
  unsigned i = 0;
  node *n = &head;
  while (i < size && n->next != NULL) {
    i++;
    if (n->val == val)
      return n;
    n = n->next;
  }

  return NULL;
}

void insert(unsigned idx, item val) {
  unsigned i = 0;
  node *n = &head;
  while (i < size && i != idx && n->next != NULL) {
    i++;
    n = n->next;
  }

  if (i == size || n == NULL) {
    printf("Insert failed at index %u\n", idx);
    return;
  }
  
  node *oldnext = n->next;

  node *new = &nodes[used++];
  new->val = val;
  new->next = oldnext;
  n->next = new;
}

unsigned wrap(unsigned idx) {
  if (idx >= size)
    return idx % size;
  else
    return idx;
}

unsigned run() {
  nodes = malloc(stepcount * sizeof(node));
  item last_i = 0;
  for (unsigned i = 1; i < stepcount + 1; i++) {
    unsigned ins_idx = wrap(stepsize + pos);
    size++;
    ins_idx = wrap(ins_idx + 1);
    
#ifdef PART2
    if (ins_idx == 0) {
      printf("INSERT AT 0\n");
    }
    if (ins_idx == 1) {
      printf("ins_idx: %u, i: %u\n", ins_idx, i);
      last_i = i;
    }
#else
    insert(ins_idx, i);
#endif
    pos = ins_idx;
  }
  
#ifndef PART2
  node *part1 = get_idx(pos + 2);
  return part1->val;
#else
    return last_i;
#endif
}


int main() {
  printf("Answer: %u\n", run());
}
  
