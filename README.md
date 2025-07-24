# Strategic-network
The project is grounded in the paper “Eccentricity-Based Strategic Network,” which investigates which network structures maximize overall welfare when individuals’ utility depends on the eccentricity (largest shortest path to any node), cost of maintaining links, and a decreasing benefit function.

# Key Features
    Mathematical Model:
    Extends classical distance-based network utility models to an eccentricity-based framework, introducing new efficiency criteria for various network topologies.

# Network Types Analyzed:

- Star networks

- Complete networks

- Double-node networks

- Empty networks

# Efficiency Analysis:
Formal propositions, proofs, and Python implementations to compute and compare the total utility for different network structures under varying benefit/cost conditions.

# Main Concepts
Strategic Network Formation:
Networks form as individuals weigh the benefits (modeled as a decreasing function of eccentricity) versus the cost of direct links.

# Eccentricity Metric:
Each node’s utility is calculated using its eccentricity, representing how far a node is from the most distant node in its component.

# Efficiency:
The optimal (efficient) network maximizes total societal utility for given costs and benefit functions.

Code Included
- Calculation of degree, eccentricity, and shortest paths in graphs.

- Construction functions for star, complete, random, and empty networks.

- Computation of individual and total utility for a network.

- Tools to compare efficiencies of different network forms as parameters vary.

# Usage
- This project is intended for researchers and students interested in network optimization, graph theory, economics, or social network analysis. The code allows you to:

- Construct and analyze custom networks.

- Experiment with different cost/benefit settings.

- Reproduce theoretical results and extend them further.

# Applications
- Social and economic network planning

- Analysis of network resilience and efficiency

- Theoretical exploration of incentives and link formation 
