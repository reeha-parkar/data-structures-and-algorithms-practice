
#include <iostream>

using namespace std;

class Node{
public:
    int data;
    Node* next;
};

Node* head = nullptr;
Node* tail = nullptr;

void print_list(){
    cout<<"The linked list is:"<<endl;
    Node* current = head;

    if(current==nullptr){
        cout<<"The list is empty"<<endl;
    }

    while(current!=nullptr){
        cout<<current->data<<endl;
        current = current->next;
    }
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

void reverse_list(){
    if(head==nullptr){
        cout<<"Can't reverse an empty list, duh"<<endl;
    }
    else{

        Node* current = head;
        Node* prev_node = nullptr;
        Node* next_node = nullptr;

        while(current!=nullptr){
            next_node = current->next;
            current->next = prev_node;
            prev_node = current;
            current = next_node;
        }

        head = prev_node;
    }
}

int main(){

    get_list(1);
    get_list(2);
    get_list(3);
    get_list(4);
    get_list(5);
    get_list(6);
    get_list(7);

    print_list();

    reverse_list();

    print_list();

    return 0;
}
