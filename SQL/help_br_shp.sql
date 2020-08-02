
/* .shp to psql */
shp2pgsql -s SRID br_shp_dir/BR_UF_2019.dbf geo_br | psql -h localhost -d db-example -U postgres;



/* SQL pipe to BR polygon transformation */
SELECT gid AS index,
       cd_uf,
       nm_uf,
       sigla_uf,
       nm_regiao,
       ST_Area(geom) AS area,
       ST_AsText(ST_Centroid(geom)) AS geom_polygon 
INTO geo_psql
FROM geo_br
ORDER BY geom_polygon DESC;

