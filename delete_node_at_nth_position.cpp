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

void delete_position(int p){

    Node* current = head;

    if(head==nullptr){
        cout<<"No list to delete position"<<endl;
    }

    else{

        if(p==1){
            head = current->next; // head points to the second node
            delete current;
            return;
        }

        for(int i=0; i<p-2; i++){
            current = current->next;
        }
    // reached at position-1, so next node is to be deleted
    cout<<"Current node: "<<current->data<<endl;
    Node* next_node = current->next;
    current->next = next_node->next;
    cout<<"Next node: "<<next_node->data<<endl;
    delete next_node;
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

    int pos;
    cout<<"Enter position to be deleted"<<endl;
    cin>>pos;
    delete_position(pos);

    print_list();

    return 0;
}
