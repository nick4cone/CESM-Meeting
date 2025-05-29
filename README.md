# CESM-Meeting
Hosts all model configuration scripts and analysis scripts for StormSPEED presentation at CESM 2025 Meeting.
## Mesh creation
[SQuadGen](https://github.com/ClimateGlobalChange/squadgen)

[V-R mesh creation instructions](https://acme-climate.atlassian.net/wiki/spaces/DOC/pages/1028128773/Generate+the+Grid+Mesh+Exodus+File+for+a+new+Regionally-Refined+Grid)

## Uniform ne240
```
<domain name="ne0np4.POLARCAP.ne30x4">
  <nx>186194</nx> <ny>1</ny>
  <mesh>$DIN_LOC_ROOT/share/meshes/POLARCAP_ne30x4_np4_ESMFmesh_cdf5_c20240222.nc</mesh>
  <desc>ne0np4.POLARCAP.ne30x4 is a Spectral Elem 1-deg grid with a 1/4 deg refined region over the Arctic and Antarctica:</desc>
  <support>Test support only</support>
</domain>
```
