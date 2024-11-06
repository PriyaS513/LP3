#include <iostream>
using namespace std;

int recursive_fibonacci(int n)
{
    if(n == 0) return 0;
    if(n == 1) return 1;
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
}

int iterative_fibonacci(int n)
{
    if(n == 0) return 0;
    if(n == 1) return 1;
    int pre = 0, curr = 1;
    for(int i = 2; i <= n; i++)
    {
        int temp = pre;
        pre = curr;
        curr = curr + temp;
    }
    return curr;
}

int main()
{
    int n, ch;
    do{
        cout<<"Enter the length of Fibonachi Series\n";
        cin>>n;
        cout<<"Choose the approach\n";
        cout<<"1. Recursive Approach\n";
        cout<<"2. Non Recursive Apprach\n";
        cout<<"3. Exit\n";
        cin>>ch;
        switch(ch)
        {
            case 1:
                for(int i=0; i<n; i++) cout<<recursive_fibonacci(i)<< " ";
                cout<<endl;
                break;
            case 2:
                for(int i = 0; i <n; i++) cout << iterative_fibonacci(i) << " ";
                cout << endl;
                break;
            case 3:
                cout<<"Thank you!!!";
                return 0;
            default:
                cout<<"Invalid Choice!!!";
        }
    }
    while (ch!=3);
    return 0;
}
