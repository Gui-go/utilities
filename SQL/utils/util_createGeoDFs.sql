# Queries to create geo_dfs:

CREATE OR REPLACE TABLE mydataset.geo_mun AS (
  SELECT DISTINCT
    CAST(cd_mun AS STRING) AS cd_mun,
    CAST(nm_mun AS STRING) AS nm_mun,
    CAST(cd_micro AS STRING) AS cd_micro,
    CAST(nm_micro AS STRING) AS nm_micro,
    CAST(cd_meso AS STRING) AS cd_meso,
    CAST(nm_meso AS STRING) AS nm_meso,
    CAST(cd_rgime AS STRING) AS cd_rgime,
    CAST(nm_rgime AS STRING) AS nm_rgime,
    CAST(cd_rgint AS STRING) AS cd_rgint,
    CAST(nm_rgint AS STRING) AS nm_rgint,
    CAST(cd_uf AS STRING) AS cd_uf,
    CAST(sg_uf AS STRING) AS sg_uf,
    CAST(nm_uf AS STRING) AS nm_uf,
    CAST(cd_rg AS STRING) AS cd_rg,
    CAST(sg_rg AS STRING) AS sg_rg,
    CAST(nm_rg AS STRING) AS nm_rg
  FROM `saoproj.mydataset.mytable2`
);

CREATE OR REPLACE TABLE mydataset.geo_micro AS (
  SELECT DISTINCT
    CAST(cd_micro AS STRING) AS cd_micro,
    CAST(nm_micro AS STRING) AS nm_micro,
    CAST(cd_meso AS STRING) AS cd_meso,
    CAST(nm_meso AS STRING) AS nm_meso,
    CAST(cd_uf AS STRING) AS cd_uf,
    CAST(sg_uf AS STRING) AS sg_uf,
    CAST(nm_uf AS STRING) AS nm_uf,
    CAST(cd_rg AS STRING) AS cd_rg,
    CAST(sg_rg AS STRING) AS sg_rg,
    CAST(nm_rg AS STRING) AS nm_rg
  FROM mydataset.geo_mun
);

CREATE OR REPLACE TABLE mydataset.geo_meso AS (
  SELECT DISTINCT
    CAST(cd_meso AS STRING) AS cd_meso,
    CAST(nm_meso AS STRING) AS nm_meso,
    CAST(cd_uf AS STRING) AS cd_uf,
    CAST(sg_uf AS STRING) AS sg_uf,
    CAST(nm_uf AS STRING) AS nm_uf,
    CAST(cd_rg AS STRING) AS cd_rg,
    CAST(sg_rg AS STRING) AS sg_rg,
    CAST(nm_rg AS STRING) AS nm_rg
  FROM mydataset.geo_mun
);

CREATE OR REPLACE TABLE mydataset.geo_rgime AS (
  SELECT DISTINCT
    CAST(cd_rgime AS STRING) AS cd_rgime,
    CAST(nm_rgime AS STRING) AS nm_rgime,
    CAST(cd_rgint AS STRING) AS cd_rgint,
    CAST(nm_rgint AS STRING) AS nm_rgint,
    CAST(cd_uf AS STRING) AS cd_uf,
    CAST(sg_uf AS STRING) AS sg_uf,
    CAST(nm_uf AS STRING) AS nm_uf,
    CAST(cd_rg AS STRING) AS cd_rg,
    CAST(sg_rg AS STRING) AS sg_rg,
    CAST(nm_rg AS STRING) AS nm_rg
  FROM mydataset.geo_mun
);

CREATE OR REPLACE TABLE mydataset.geo_rgint AS (
  SELECT DISTINCT
    CAST(cd_rgint AS STRING) AS cd_rgint,
    CAST(nm_rgint AS STRING) AS nm_rgint,
    CAST(cd_uf AS STRING) AS cd_uf,
    CAST(sg_uf AS STRING) AS sg_uf,
    CAST(nm_uf AS STRING) AS nm_uf,
    CAST(cd_rg AS STRING) AS cd_rg,
    CAST(sg_rg AS STRING) AS sg_rg,
    CAST(nm_rg AS STRING) AS nm_rg
  FROM mydataset.geo_mun
);
