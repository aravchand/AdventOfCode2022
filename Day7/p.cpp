#include <bits/stdc++.h>
using namespace std;

using ll = long long;
#define all(x) x.begin(), x.end()

string stringify(stack<string> s)
{   
    bool f = 1;
    string ans = "";
    while (!s.empty())
    {
        if(!f) ans += "-";
        f = 0;
        ans += s.top();
        s.pop();
    }
    return ans;
}

class Dir
{
public:
    string name;
    ll size = 0;
    vector<Dir*> subdirs;
    vector<string> files;
    Dir(string n = ""): name(n) {}

    void addFile(ll fileSize)
    {
        size += fileSize;
    }
    void addSubdir(Dir &subdir)
    {
        subdirs.push_back(&subdir);
    }

    ll sumSize()
    {
        ll sum = size;
        for (Dir* subdir : subdirs)
        {
            sum += subdir->sumSize();
        }
        return sum;
    }
};

int main()
{
    freopen("input.in", "r", stdin);
    string line;
    stack<string> current_path; 
    map<string, Dir> directories;

    while (getline(cin, line))
    {
        if(!current_path.empty() && current_path.top() == " a") cout << "HELP\n"<<line<<"\n";
     
        if (line[0] == '$')
        {
            if (line == "$ cd /")
            {
     
                current_path = stack<string>();
                current_path.push("/");
     
                if(directories[stringify(current_path)].name == "") 
                    directories[stringify(current_path)] = Dir("/");
     
            }
            else if (line == "$ ls")
            {
                // we dont need to do anything
            }
            else if (line == "$ cd ..")
            {
                current_path.pop();
            }
            else
            {
                //  012345
                // "$ cd a"
                string dir = line.substr(5);
                current_path.push(dir);
                if(directories[stringify(current_path)].name == "") {
                    directories[stringify(current_path)] = Dir(dir);
                }
            }
        }
        else
        {
            // 01234
            //"dir a"
            if (line.substr(0, 3) == "dir")
            {

                string dir = line.substr(4);

                stack<string> cpy = current_path;
                cpy.push(dir);
                if(directories[stringify(cpy)].name == "")
                    directories[stringify(cpy)] = Dir(dir);
                
                directories[stringify(current_path)].addSubdir(directories[stringify(cpy)]);
            }
            else
            {
                //          this is cur. dir.    gets integer form of size... we can ignore name (rest of line string) since unimportant to us
                directories[stringify(current_path)].addFile(stoi(line.substr(0, line.find(" "))));
            }
        }
    }

    // p1:
    ll ans1 = 0;

    // p2:
    ll ans2 = 1e12;
    ll remainingDiskSpace = 70000000 - directories["/"].sumSize();
    ll minExtraNeeded = 30000000 - remainingDiskSpace;

    for(auto dir : directories) {
        ll totSize = dir.second.sumSize();
        // cout << dir.first << " " << totSize << "\n";
        // print(dir.second.subdirs);
        
        ans1 += (totSize <= 100000LL) ? totSize : 0;
        ans2 = min(ans2, totSize > minExtraNeeded ? totSize : (ll)1e12); // if is big enough to be good
    }
    cout << "p1: " << ans1 << "\n";
    cout << "p2: " << ans2 << "\n";


    
    
    

}