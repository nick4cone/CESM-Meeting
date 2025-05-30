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
