# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..model import MRISPreproc


def test_MRISPreproc_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fsgd_file=dict(argstr='--fsgd %s',
    xor=(u'subjects', u'fsgd_file', u'subject_file'),
    ),
    fwhm=dict(argstr='--fwhm %f',
    xor=[u'num_iters'],
    ),
    fwhm_source=dict(argstr='--fwhm-src %f',
    xor=[u'num_iters_source'],
    ),
    hemi=dict(argstr='--hemi %s',
    mandatory=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    num_iters=dict(argstr='--niters %d',
    xor=[u'fwhm'],
    ),
    num_iters_source=dict(argstr='--niterssrc %d',
    xor=[u'fwhm_source'],
    ),
    out_file=dict(argstr='--out %s',
    genfile=True,
    ),
    proj_frac=dict(argstr='--projfrac %s',
    ),
    smooth_cortex_only=dict(argstr='--smooth-cortex-only',
    ),
    source_format=dict(argstr='--srcfmt %s',
    ),
    subject_file=dict(argstr='--f %s',
    xor=(u'subjects', u'fsgd_file', u'subject_file'),
    ),
    subjects=dict(argstr='--s %s...',
    xor=(u'subjects', u'fsgd_file', u'subject_file'),
    ),
    subjects_dir=dict(),
    surf_area=dict(argstr='--area %s',
    xor=(u'surf_measure', u'surf_measure_file', u'surf_area'),
    ),
    surf_dir=dict(argstr='--surfdir %s',
    ),
    surf_measure=dict(argstr='--meas %s',
    xor=(u'surf_measure', u'surf_measure_file', u'surf_area'),
    ),
    surf_measure_file=dict(argstr='--is %s...',
    xor=(u'surf_measure', u'surf_measure_file', u'surf_area'),
    ),
    target=dict(argstr='--target %s',
    mandatory=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    vol_measure_file=dict(argstr='--iv %s %s...',
    ),
    )
    inputs = MRISPreproc.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_MRISPreproc_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = MRISPreproc.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value