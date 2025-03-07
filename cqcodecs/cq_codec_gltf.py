import os, tempfile
from cadquery import exporters
import cadquery as cq
import cqcodecs.codec_helpers as helpers

def convert(build_result, output_file=None, error_file=None, output_opts=None):
    # Create a temporary file to put the STL output into
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "temp_gltf.gltf")

    # The exporters will add extra output that we do not want, so suppress it
    with helpers.suppress_stdout_stderr():
        # Put the GLTF output into the temp file
        # Check to see if we are dealing with an assembly or a single object
        if type(build_result.first_result.shape).__name__ == "Assembly":
            build_result.first_result.shape.save(temp_file, binary=False)
        else:
            raise ValueError("GLTF export is only available for CadQuery assemblies at this time")

    # Read the GLTF output back in
    with open(temp_file, 'r') as file:
        gltf_str = file.read()

    return gltf_str