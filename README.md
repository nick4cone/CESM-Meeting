# CESM-Meeting
Hosts all model configuration scripts and analysis scripts for StormSPEED presentation at CESM 2025 Meeting.
## Mesh creation
[SQuadGen](https://github.com/ClimateGlobalChange/squadgen)

[V-R mesh creation instructions](https://acme-climate.atlassian.net/wiki/spaces/DOC/pages/1028128773/Generate+the+Grid+Mesh+Exodus+File+for+a+new+Regionally-Refined+Grid)

## ne240 runs
| case name | nsteps | physics tstep | simulation time | se_tstep | n nodes | runtime |
| -- | -- | -- | -- | -- | -- | -- |
| test6_uniform_ne240 | 15 | 600 seconds | 9000 seconds | 30 seconds | 8 | tbd |

## Notes (reorganize later)
```ATM_NCPL=144```  
```ROF_NCPL=48```   
```./xmlchange --append --file env_build.xml --id CAM_CONFIG_OPTS --val="-nlev=58"```

```
  <model_grid alias="ne0MIDWESTne30x5_ne0MIDWESTne30x5" not_compset="_POP">
    <grid name="atm">ne0np4.MIDWEST.ne30x5</grid>
    <grid name="lnd">ne0np4.MIDWEST.ne30x5</grid>
    <grid name="ocnice">ne0np4.MIDWEST.ne30x5</grid>
    <mask>tx0.1v2</mask>
  </model_grid>
```
```
  <domain name="ne0np4.MIDWEST.ne30x5">
    <nx>381674</nx> <ny>1</ny>
    <mesh>/glade/u/home/nforcone/CESM-Meeting/Mesh/midwest-ncf-ESMF.nc</mesh>
    <desc>Spectral Elem 1-deg grid with 5 refinement levels over the Midwest</desc>
  </domain>
```
