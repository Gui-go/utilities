SELECT
  *,
  (Lula + Bolsonaro) AS TotalV,
  (Lula + Bolsonaro + Branco + Nulo) AS TotalBN,
  COALESCE(Lula / NULLIF((Lula + Bolsonaro), 0), 0) * 100 AS txv_lula,
  COALESCE(Bolsonaro / NULLIF((Lula + Bolsonaro), 0), 0) * 100 AS txv_bolsonaro,
  COALESCE(Lula / NULLIF((Lula + Bolsonaro + Branco + Nulo), 0), 0) * 100 AS txbn_lula,
  COALESCE(Bolsonaro / NULLIF((Lula + Bolsonaro + Branco + Nulo), 0), 0) * 100 AS txbn_Bolsonaro,
  COALESCE(Branco / NULLIF((Lula + Bolsonaro + Branco + Nulo), 0), 0) * 100 AS txbn_branco,
  COALESCE(Nulo / NULLIF((Lula + Bolsonaro + Branco + Nulo), 0), 0) * 100 AS txbn_nulo
FROM (
  SELECT 
    SG_UF, 
    CD_MUNICIPIO, 
    NM_MUNICIPIO,
    NR_ZONA, 
    NR_SECAO, 
    IFNULL(_13, 0) AS Lula, 
    IFNULL(_22, 0) AS Bolsonaro, 
    IFNULL(_95, 0) AS Branco, 
    IFNULL(_96, 0) AS Nulo,
  FROM (
    SELECT 
      SG_UF, 
      CD_MUNICIPIO, 
      NM_MUNICIPIO, 
      NR_ZONA, 
      NR_SECAO, 
      NR_VOTAVEL, 
      QT_VOTOS
    FROM `projelections.df_elections.votacao_secao_2022_BR3` 
    WHERE (DT_ELEICAO = "2022-10-30")
      AND (CD_TIPO_ELEICAO = 2)
      AND (NR_TURNO = 2)
    )
  PIVOT(
    SUM(QT_VOTOS) 
    FOR NR_VOTAVEL IN (13, 22, 95, 96)
  )
);


