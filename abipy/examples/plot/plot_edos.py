#!/usr/bin/env python
"""
This example shows how to compute the gaussian DOS from
the eigenvalues stored in the WFK file.
"""
import abipy.data as abidata
from abipy.abilab import abiopen

# Open the wavefunction file computed with a homogeneous sampling of the BZ
# and extract the band structure on the k-mesh.
with abiopen(abidata.ref_file("si_scf_WFK.nc")) as gs_wfk:
    gs_ebands = gs_wfk.ebands

# Compute the DOS with the Gaussian method.
edos = gs_ebands.get_edos(method="gaussian", step=0.01, width=0.1)

# Plot electron DOS and IDOS
edos.plot(title="DOS of Silicon")

# Plot electron DOS and IDOS
edos.plot_dos_idos(title="DOS and Integrated DOS")
