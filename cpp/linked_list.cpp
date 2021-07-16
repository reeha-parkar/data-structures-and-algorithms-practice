#include <iostream>

using namespace std;

class Node{
public:
    int data;
    Node* next;
};

void print_list(Node* n){
    while(n!=nullptr){
        cout<<n->data<<endl;
        n = n->next;
    }
}

int main(){
    Node* head = nullptr;
    Node* second = nullptr;
    Node* third = nullptr;

    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 1;
    head->next = second;
    second->data = 2;
    second->next = third;
    third->data = 3;
    third->next = nullptr;

    print_list(head);

    return 0;
}

