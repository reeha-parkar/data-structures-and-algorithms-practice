
#include <iostream>

using namespace std;

class Node{
public:
    int data;
    Node* next;
};

Node* head = nullptr;
Node* tail = nullptr;

void print_list(Node* head){
    Node* current = head;

    if(current==nullptr){
        return;
    }

    cout<<current->data<<endl;
    print_list(current->next);

}

void get_list(int element){

    Node* new_node = new Node();
    new_node->data = element;
    new_node->next = nullptr;

    if(head == nullptr){
        head = new_node;
        tail = new_node;
    }
    else{
        tail->next = new_node;
        tail = new_node;
    }
}

void reverse_list(Node* head_node){
    Node* current = head_node;

    if(current->next==nullptr){
        head = current;
        return;
    }

    reverse_list(current->next);
    Node* next_node = current->next;
    next_node->next = current;
    current->next = nullptr;
}

int main(){

    get_list(1);
    get_list(2);
    get_list(3);
    get_list(4);
    get_list(5);
    get_list(6);
    get_list(7);

    cout<<"The original list is: "<<endl;
    print_list(head);

    reverse_list(head);

    cout<<"The reversed list is: "<<endl;
    print_list(head);

    return 0;
}

