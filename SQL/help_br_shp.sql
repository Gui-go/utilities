
/* .shp to psql */
shp2pgsql -s SRID br_shp_dir/BR_UF_2019.dbf geo_br | psql -h localhost -d db-example -U postgres;



/* SQL pipe to BR polygon transformation */
SELECT gid AS index,
       cd_uf,
       nm_uf,
       sigla_uf,
       nm_regiao,
       ST_Area(geom) AS area,
       ST_AsText(ST_Centroid(geom)) AS polygon_centroid 
INTO geoBR_psql_table
FROM geo_br
ORDER BY polygon_centroid DESC;

/* SQL pipe to BR polygon transformation */
SELECT gid AS index,
       cd_uf,
       nm_uf,
       sigla_uf,
       nm_regiao,
       ST_Area(geom) AS area,
       ST_AsGeoJSON(geom) AS polygonA 
INTO geoBR_psql_table2
FROM ashp
ORDER BY polygonA DESC;

SELECT ST_AsGeoJSON(ST_Transform(geom_polygon,4326)) from ashp limit 1;