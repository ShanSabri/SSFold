# SSFold
🧬 SSFold is a dynamic programming algorithm for predicting the optimal RNA secondary structure. It was developed as part of my written qualifying exam at UCLA in partial fulfillment of my PhD requirement. A full write-up can be found [**here**](http://shansabri.com/SSFold/wqe.pdf "here").  


### Motivation
RNA folding is the process by which a linear ribonucleic acid (RNA) molecule acquires secondary structure through intra-molecular interactions. The folded domains of RNA molecules are often the sites of specific interactions with proteins in forming RNA-protein (ribonucleoprotein) complexes. These structures play an immense role in the function of a single-stranded RNA molecules and therefore predicting these secondary structures allow for functional predictions.

Structural prediction of RNA has been a fundamental issue in bioinformatics dating back to the early ‘90s. RNA secondary structure predictions are constructed on a model of intra-molecular base pairing interactions. Historically, this model has been built on one of three prediction methods:

 1. Utilizing mutual information (MI) in a covariation-based approach
 2. Context free grammars, typically stochastic in nature
 3. Energy-based models

The ultimate goal of this project is to accurately predict a secondary structure of a given RNA molecule simply off sequence information alone. 

### Method
An algorithm proposed by [Ruth Nussinov et al. (1978)](http://epubs.siam.org/doi/10.1137/0135006) was used as a foundation for SSFold since it does not rely on experimental data and utilizes sequences information alone. The goal of the Nussinov algorithm is to build a structure with the greatest amount of base parings. Since base pairings form energetically favorable interactions through hydrogen bonds, it can be implied that the larger number of base pairings lead to a more energetically favorable structure. The goal of SSFold is to take into account the stabilizing energies of stacked base pairs, which in turn implies greater stability of helix features, while also considering the size of loop structures in each prediction. Generally loops that are too big or too small become unstable due to steric constraints.

As with the Nussinov algorithm, SSFold is recursive and solves small subsequences to produce an optimal structure. Bases are appended to a substructure on an individual basis until defined conditions limits the addition. Additionally, SSFold enforces the following criteria for accurate secondary structure prediction:
1.  Sharp hairpin loops are prohibited. Hairpin loops must contain at least 3 bases.
2. Base triples are excluded such that two base pairs (i, j) and (i’, j’) are either identical or i ≠ i’ and j ≠ j’
3.  Pseudoknots are prohibited




### Results
I have benchmarked SSFold using experimentally validated structures against Nussinov’s algorithm and show that SSFold more accurately predicts structures that are simple, such that they contain a single structural feature (i.e. hairpin). Of the five cases tested, SSFold computed a perfect prediction for the two simple cases. In respect to the more complex structures (molecules with more than one structural feature), I show SSFold to preform better than Nussinov’s algorithm in terms of structural similarity and energetic stability. 

[![image](https://i.imgur.com/9nQ3nym.png "image")](https://i.imgur.com/9nQ3nym.png "image")

Notice in the rather simplified example above the Nussinov algorithm base pairs a uracil at position 8 with an adenine at position 19, albeit the presence of another uracil at position 7, thereby disrupting stem formation. This structure ultimately produces a free energy of -8.60 Kcal/mol at 37° C. SSFold, on the other hand, shifts the uracil in the U8 – A19 base paring down a position to preserve stem feature formation (i.e. prioritize base stacking). Stacking these base pairings led to a more energetically favorable formation. 

By prioritizing stem formation and elongation we are able to easily capture nearest neighbor and stacking interactions, a feature which Nussinov’s algorithm lacks. We also show that in cases where computational space complexity is not a limitation, our proposed algorithm is favored for simple structures.


### License
MIT

