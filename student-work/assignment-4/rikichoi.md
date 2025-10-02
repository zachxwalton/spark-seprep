# Riki Choi
My favourite programming language is C++ because of its functionality in the world of quant finance. I'm not really good at it, neither do I enjoy learning it. But its applications severely outweighs my lack of enjoyment in learning it.

## Example code:

`````

#include <bits/stdc++.h>
using namespace std;

struct MarkovChain {
    vector<vector<double>> P;                    // Row-stochastic transition matrix
    vector<discrete_distribution<int>> dists;    // One sampler per state
    mt19937 rng{random_device{}()};

    explicit MarkovChain(vector<vector<double>> transition) : P(move(transition)) {
        for (auto &row : P) dists.emplace_back(row.begin(), row.end());
    }

    // Sample next state given current state
    int step(int s) { return dists[s](rng); }

    // Simulate n steps starting from s0 (includes s0)
    vector<int> simulate(int n, int s0) {
        vector<int> path; path.reserve(n+1);
        int s = s0; path.push_back(s);
        for (int i = 0; i < n; ++i) { s = step(s); path.push_back(s); }
        return path;
    }

    // Approximate stationary distribution (left eigenvector) with power iteration
    vector<double> stationary(int iters = 1000, double tol = 1e-12) {
        int m = (int)P.size();
        vector<double> pi(m, 1.0 / m), next(m, 0.0);

        for (int k = 0; k < iters; ++k) {
            fill(next.begin(), next.end(), 0.0);
            // pi_next = pi * P
            for (int i = 0; i < m; ++i)
                for (int j = 0; j < (int)P[i].size(); ++j)
                    next[j] += pi[i] * P[i][j];

            // Normalize and check convergence (L1)
            double sum = accumulate(next.begin(), next.end(), 0.0);
            for (double &x : next) x /= sum;

            double diff = 0.0;
            for (int i = 0; i < m; ++i) diff += fabs(next[i] - pi[i]);
            pi.swap(next);
            if (diff < tol) break;
        }
        return pi;
    }
};

int main() {
    // Example: 3-state chain
    //    0 -> {0:0.1, 1:0.6, 2:0.3}
    //    1 -> {0:0.2, 1:0.2, 2:0.6}
    //    2 -> {0:0.7, 1:0.1, 2:0.2}
    vector<vector<double>> P = {
        {0.1, 0.6, 0.3},
        {0.2, 0.2, 0.6},
        {0.7, 0.1, 0.2}
    };

    MarkovChain mc(P);

    // Simulate a short path
    auto path = mc.simulate(10, /*start=*/0);
    cout << "Path: ";
    for (int s : path) cout << s << ' ';
    cout << "\n";

    // Estimate stationary distribution
    auto pi = mc.stationary();
    cout << "Stationary distribution ~ [";
    for (int i = 0; i < (int)pi.size(); ++i) {
        cout << fixed << setprecision(4) << pi[i] << (i+1==(int)pi.size()?"]\n":" , ");
    }
    return 0;
}

`````

### Code Explanation

The program is a Markov chain simulator.

You give it a table of probabilities (the transition matrix) that tells it how likely it is to move from one state to another.

Example: from state 0, maybe there’s a 10% chance you stay in 0, 60% chance you go to 1, 30% chance you go to 2.

The program can then:

Simulate a sequence of states (like rolling a special kind of weighted dice at each step).

Estimate the long-run distribution — i.e. if you ran it forever, what fraction of time would you spend in each state.

So in short, it models a system that moves randomly between states according to fixed probabilities, shows you an example “path” of states, and tells you the long-term chances of being in each state.

To use it, you just save the code into a file, compile it with g++, and run the program in your terminal to see the results.

        
