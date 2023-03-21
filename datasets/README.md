# Datasets Download and Pre-processing in BEAR

We provide download and pre-processing approaches for all 18 datasets here. It should be noted that for [UAV-Human](), [ToyotaSmarthome]() and [MUVIM](MUVIM/README.md), there are no direct downloading scripts, since the data access must be requested from the owners of the datasets and there shall be no redistribution of these datasets.



- The general folder structure for BEAR datasets should be as follows:
  ```
  ./data/
  |
  |───dataset1/
  │    └───videos/
  │    └───annotations/
  └───dataset2
  │    └───videos/
  │    └───annotations/
  └───dataset3/
  │    └───videos/
  │    └───annotations/
  └───...
  ```