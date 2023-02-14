from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileData,Dict
from pyscf import gto,scf
from pyscf.geomopt.berny_solver import optimize

class OptCalculation(CalcJob):
    """AiiDA calculation plugin for optimization by PsSCF"""

    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        # yapf: disable
        # super(OptCalculation, cls).define(spec)
        super().define(spec)

        # new ports
        spec.input("parameters", valid_type=Dict, help="Input parameters for PySCF")
        spec.input("structure", valid_type=SinglefileData, help="Input structure in XYZ format")
        spec.output("output", valid_type=Dict, help="Output data")
        #spec.input('atom', valid_type=SinglefileData, help='Atom structure in .xyz')
        #spec.input('basis', valid_type=Str, help='Basis set for the calculation')
        #spec.output('atom_coords', valid_type=str, help='Optmized structure')
        
        #spec.input('metadata.options.output_filename', valid_type=str, default='optimized')
        #spec.inputs['metadata']['options']['resources'].default ={
        #        'num_machines': 1,
        #        'num_mpiprocs_per_machine': 1,
        #        }
        #spec.inputs['metadata']['options']['parser_name'].default = 'optimization'

        #spec.exit_code(300, 'ERROR_MISSING_OUTPUT_FILES',
         #       message='Calculation did not produce all expected output files.')


    def prepare_for_submission(self, folder):
        """
        Create input files.

        :param folder: an `aiida.common.folders.Folder` where the plugin should temporarily place
            all the calculation.
        :return: `aiida.common.datastructures.CalcInfo` instance
        """
        #codeinfo = datastructures.CodeInfo()
        #codeinfo.cmdline_params = [self.inputs.atom.filename, self.inputs.file2.filename]
        #codeinfo.code_uuid = self.inputs.code.uuid
        #codeinfo.stdout_name = self.metadata.options.output_filename
        #mol = gto.M(atom=self.inputs.atom.filename, basis = self.inputs.basis)
        #mf = scf.RHF(mol)
        #moq_eq = optimize(mf, maxstep = 100)
        
        parameters = self.inputs.parameters.get_dict()
        structure = self.inputs.structure

        # structure_path = folder.get_abs_path('N2.xyz')
        # structure.get_file().copyfile(structure_path)
    
        mol = gto.M(
            atom = 'H 0 0 0; F 0 0 1.1', # in Angstrom
            basis = 'ccpvdz',
            symmetry = True,
            )
        myhf = scf.HF(mol)
        myhf.kernel()

        # First, get the atoms from the structure file:
        #atoms = structure.get_content().strip().split('\n')[2:]

        # Then, write them to an input file in PySCF format:
        #input_data = f'''
        #0 1
        #{'\n'.join(atoms)}
        #'''
        #with open(folder.get_abs_path('input.dat'), 'w') as f:
        #    f.write(input_data)

        # Finally, set up the command line arguments for PySCF:
        # cmd = ["python3", "-i", "input.dat", "-o", "output.dat"]
        

        # Prepare a `CalcInfo` to be returned to the engine
        #calcinfo = datastructures.CalcInfo()
        #calcinfo.codes_info = [codeinfo]
        #calcinfo.local_copy_list = [
        #        (self.inputs.file1.uuid, self.inputs.file1.filename, self.inputs.file1.filename),
        #        (self.inputs.file2.uuid, self.inputs.file2.filename, self.inputs.file2.filename),
        #]
        #calcinfo.retrieve_list = [self.metadata.options.output_filename]

        # with folder.open("filename", 'w') as handle:
        #   handle.write("file content")

        #return calcinfo


