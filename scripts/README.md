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
