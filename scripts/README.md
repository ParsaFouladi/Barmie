# Scripts Folder

The `scripts` folder contains a comprehensive set of Python scripts designed to support various stages of the computational docking workflow. These scripts facilitate key processes such as data preparation, file format conversion, protein-ligand alignment, and post-docking analysis.

Each script is modular and can be executed independently or integrated into larger pipelines, providing flexibility for a range of computational tasks. This structured approach ensures efficiency, consistency, and scalability, making the scripts suitable for both small-scale studies and high-throughput docking projects.

## File Conversion Scripts

The folder includes several scripts dedicated to converting molecular file formats, essential for preparing data for docking and analysis. These conversion scripts cover common formats such as PDB, PDBQT, MOL2, and SDF.

### Available Conversion Scripts:
- `pdb_to_pdbqt.py` - Converts PDB files to PDBQT format.
- `pdbqt_to_mol2.py` - Converts PDBQT files to MOL2 format.
- `pdbqt_to_pdb.py` - Converts PDBQT files back to PDB format.
- `sdf_to_pdbqt.py` - Converts SDF files to PDBQT format.

### Usage
All file conversion scripts follow the same command-line structure for consistency:

```bash
python from_to.py input_folder output_folder


## Protein Alignment Script

The `alignment.py` script is designed to align multiple protein structures to a reference protein using PyMOL’s structural alignment capabilities. This is particularly useful when preparing proteins for docking or structural comparison studies.

### Features:
- Aligns multiple proteins to a specified reference structure.
- Outputs aligned structures in PDB format for downstream analysis.

### Requirements:
- **PyMOL** must be installed and accessible within your Python environment.

### Usage:
```bash
python alignment.py input_folder output_folder reference_protein.pdb
```

- **`input_folder`**: Folder containing the protein files to be aligned.
- **`output_folder`**: Destination folder where the aligned files will be saved.
- **`reference_protein.pdb`**: The reference protein structure to which all other proteins will be aligned.

### Example:
```bash
python alignment.py ./proteins ./aligned_proteins reference.pdb
```

This command will align all proteins in the `./proteins` folder to `reference.pdb` and save the aligned structures in the `./aligned_proteins` folder.

**Note:** Ensure that **PyMOL** is correctly installed in your Python environment to run this script successfully. Without PyMOL, the alignment functionalities will not work.
