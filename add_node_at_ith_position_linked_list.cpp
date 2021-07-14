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

void add(Node** head_ref, int new_data, int pos){
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = nullptr;

    if (pos==1){
        new_node->next = *head_ref;
        *head_ref = new_node;
        return;
    }

    Node* current = *head_ref;

    for(int i=0; i<pos-2; i++){
        current = current->next;
    }
    new_node->next = current->next;
    current->next = new_node;

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

    int data, pos;

    cout<<"Enter the new element"<<endl;
    cin>>data;

    cout<<"Enter the position"<<endl;
    cin>>pos;

    add(&head, data, pos);

    cout<<"The list after inserting new element is:"<<endl;
    print_list(head);

    return 0;
}


