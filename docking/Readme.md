# README: Multi-CPU Docking Script

## Overview
This Python script is a high-throughput docking pipeline designed to facilitate the docking of protein-ligand pairs using **AutoDock Vina**. It supports multi-CPU parallel processing, enabling efficient handling of large datasets. The script automates preprocessing steps, docking calculations, and result management.

## Features
- **Multi-CPU Support**: Utilizes Python's multiprocessing library to maximize computational efficiency.
- **Flexible Docking Parameters**: Allows users to customize docking parameters such as exhaustiveness, center coordinates, and box size.
- **Automated File Management**: Removes spaces from file names and organizes output files systematically.
- **Comprehensive Logging**: Logs docking progress and errors for easy troubleshooting.

## Requirements
- Python 3.6+
- AutoDock Vina
- `vina` Python package
- Multiprocessing library (default in Python)
- Having your ligand and protein files in pdbqt format

## Installation
1. Install Python dependencies:
   ```bash
   pip install vina
   ```
2. Ensure AutoDock Vina is installed and accessible from your system's PATH.
3. Clone or download this repository to your local machine.

## Usage
Run the script with the following arguments:

```bash
python docking_pipeline.py \
    --receptor_folder PATH_TO_RECEPTOR_FOLDER \
    --ligand_folder PATH_TO_LIGAND_FOLDER \
    --output_folder PATH_TO_OUTPUT_FOLDER \
    --exhaustiveness 32 \
    --center 5 2 -15 \
    --box_size 20 20 20 \
    --num_cpus 4
```
You can see an example of slurm file in docs folder

### Arguments
- `--receptor_folder`: Path to the folder containing receptor files in `.pdbqt` format.
- `--ligand_folder`: Path to the folder containing ligand files in `.pdbqt` format.
- `--output_folder`: Path to the folder where docking results will be saved.
- `--exhaustiveness` (`-e`): Controls the thoroughness of the search (default: `32`).
- `--center` (`-c`): Center coordinates for the docking box (default: `[5, 2, -15]`).
- `--box_size` (`-b`): Dimensions of the docking box (default: `[20, 20, 20]`).
- `--num_cpus` (`-n`): Number of CPUs to use for parallel processing (default: all available CPUs).

### Example
```bash
python docking_pipeline.py \
    --receptor_folder ./receptors \
    --ligand_folder ./ligands \
    --output_folder ./results \
    --exhaustiveness 16 \
    --center 0 0 0 \
    --box_size 25 25 25 \
    --num_cpus 8
```

## Output
- Docking results are saved in the specified output folder as `.pdbqt` files, named in the format `receptor_ligand_vina_out.pdbqt`.
- Logs of the docking process are saved as `docking_log_<date>.log` in the current directory.



