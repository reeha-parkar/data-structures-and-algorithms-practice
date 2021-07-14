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

void append(Node** head_ref, int new_data){
    // allocate new node:
    Node* new_node = new Node();
    Node* last = *head_ref;
    new_node->data = new_data;
    new_node->next = nullptr;

    if(*head_ref==nullptr){
        *head_ref = new_node;
        return;
    }

    while(last->next!=nullptr){
        last = last->next;
    }
    last->next = new_node;
    return;
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

    cout<<"The original list is:"<<endl;
    print_list(head);

    int data;

    cout<<"Enter the new element"<<endl;
    cin>>data;

    append(&head, data);

    cout<<"The list after inserting new element is:"<<endl;
    print_list(head);

    return 0;
}

