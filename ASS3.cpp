#include<iostream>
#include<vector>
#include<queue>
using namespace std;

double frac(vector<double> weight,vector<double> profit,int cap)
{
    priority_queue<pair<double,int>> pq;
    for (int i=0;i<weight.size();i++)
    {
        pq.push({profit[i]/weight[i],i});
    }
    double total=0;
    while (!pq.empty())
    {
        int index=pq.top().second;
        pq.pop();
        if (weight[index]<=cap)
        {
            cap-=weight[index];
            total+=profit[index];
        }
        else
        {
            total+=((cap/weight[index])*profit[index]);
            cap=0;
        }
    }
    return total;
}

int main()
{
    int n,cap;
    cout<<"cap:";
    cin>>cap;
    cout<<"Enetr the no of items: ";
    cin>>n;
    vector<double> weight(n,0),profit(n,0);
    cout<<"weight,profit";
    for (int i=0;i<n;i++)
    {
        cin>>weight[i]>>profit[i];
    }
    double t=frac(weight,profit,cap);
    cout<<t;
    return 0;
}