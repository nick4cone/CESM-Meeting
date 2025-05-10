#!/glade/work/nforcone/conda-envs/High-Resolution/bin/python

from plot_unstructured import global_plot, regional_plot

global_plot('~/CESM-Meeting/Mesh/derecho-EXODUS.g', '~/CESM-Meeting/Mesh/derecho-grid-global-visual')
regional_plot('~/CESM-Meeting/Mesh/derecho-EXODUS.g', '~/CESM-Meeting/Mesh/derecho-grid-regional-visual')
