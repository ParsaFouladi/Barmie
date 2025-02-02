# Binding Affinity Ranking at the Molecular Initiating Event (BARMIE)

**An open-source computational pipeline for ecological hazard ranking of endocrine disrupting chemicals.**

The BARMIE pipeline is designed for high-throughput computational docking and binding affinity prediction. It includes:

1. **Docking Script**: Optimized for multi-CPU usage to efficiently process large datasets.
2. **Preprocessing Scripts**: Tools for preparing protein and ligand files for docking.

### Features
- **High-Throughput Docking**: Efficiently processes large datasets with multi-CPU support.
- **Flexible Preprocessing**: Supports various input formats for proteins and ligands.
- **Modular Design**: Components can be used independently or as part of larger workflows.

### Repository Structure
- **/docking**: Contains the docking script and the corresponding slurm file
- **/scripts**: Contains the scripts that can be used to preprocess the protein and ligand files, such as file format conversion, pocket filtering, protein alignment and etc.
- **/docs**: Contains related documentations and examples

### Applications
Originally developed for ecological hazard ranking, the pipeline is also suitable for:
- Drug discovery
- Environmental toxicology
- Molecular docking studies



