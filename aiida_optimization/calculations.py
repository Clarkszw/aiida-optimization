from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileDatai
from pyscf import gto,scf
from pyscf.geomopt.berny_solver import optimize

class OptCalculation(CalcJob):
    """AiiDA calculation plugin for optimization by PsSCF"""

    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        # yapf: disable
        super(OptCalculation, cls).define(spec)

        # new ports
        spec.input('atom', valid_type=SinglefileData, help='Atom structure in .xyz')
        spec.input('basis', valid_type=str, help='Basis set for the calculation')
        spec.output('atom_coords', valid_type=str, help='Optmized structure')
        
        spec.input('metadata.options.output_filename', valid_type=str, default='optimized')
        spec.inputs['metadata']['options']['resources'].default ={
                'num_machines': 1,
                'num_mpiprocs_per_machine': 1,
                }
        spec.inputs['metadata']['options']['parser_name'].default = 'Optimization'

        spec.exit_code(300, 'ERROR_MISSING_OUTPUT_FILES',
                message='Calculation did not produce all expected output files.')


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
        mol = gto.M(atom=self.inputs.atom.filename, basis = self.inputs.basis)
        mf = scf.RHF(mol)
        moq_eq = optimize(mf, maxstep = 100)

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


