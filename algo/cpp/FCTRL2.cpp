#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using boost::multiprecision::cpp_int;

typedef boost::multiprecision::cpp_int BigInt;

BigInt fact(int i) {
    if ( i < 2) {
        return 1;
    } else {
        return i * fact( i - 1 );
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; 
    cin >> t;
    
    while (t--){
        int n;
        cin >> n;
        BigInt output = fact(n);
        cout << output << "\n";
    }
    
    return 0;
}
