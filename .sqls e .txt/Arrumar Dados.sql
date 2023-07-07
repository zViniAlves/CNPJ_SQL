USE CNPJ

UPDATE Simples
SET data_exclusao_mei = CONCAT(
	SUBSTRING(data_exclusao_mei, 1, 4), '/', 
    SUBSTRING(data_exclusao_mei, 5, 2), '/', 
    SUBSTRING(data_exclusao_mei, 7, 2)
);
	
UPDATE Simples
SET data_exclusao_simples = CONCAT(
	SUBSTRING(data_exclusao_simples, 1, 4), '/', 
    SUBSTRING(data_exclusao_simples, 5, 2), '/', 
    SUBSTRING(data_exclusao_simples, 7, 2)
);
	
UPDATE Simples
SET data_opcao_mei = CONCAT(
	SUBSTRING(data_opcao_mei, 1, 4), '/', 
    SUBSTRING(data_opcao_mei, 5, 2), '/', 
    SUBSTRING(data_opcao_mei, 7, 2)
);
	
UPDATE Simples
SET data_opcao_simples = CONCAT(
	SUBSTRING(data_opcao_simples, 1, 4), '/', 
    SUBSTRING(data_opcao_simples, 5, 2), '/', 
    SUBSTRING(data_opcao_simples, 7, 2)
);
	
UPDATE Empresas
SET str_natureza_juridica = (
    SELECT t.natureza_str
    FROM natureza t
    WHERE Empresas.c�d_natureza_juridica = t.c�d_natureza);

UPDATE Empresas
SET str_qualifica��o_responsavel = (
    SELECT t.qualifica��o_str
    FROM qualifica��o t
    WHERE Empresas.c�d_qualificacao_responsavel = t.c�d_qualifica��o);

UPDATE Empresas
SET porte_empresa = 
    CASE 
        WHEN porte_empresa = '00' THEN 'N�o informado'
        WHEN porte_empresa = '01' THEN 'Micro Empresa'
        WHEN porte_empresa = '03' THEN 'Empresa de Pequeno Porte'
		WHEN porte_empresa = '05' THEN 'Demais'
        ELSE porte_empresa
    END;

UPDATE Socios
SET identificador_de_socio =
	CASE 
        WHEN identificador_de_socio = '1' THEN 'Pessoa J�ridica'
        WHEN identificador_de_socio = '2' THEN 'Pessoa F�sica'
        WHEN identificador_de_socio = '3' THEN 'Estrangeiro'
        ELSE identificador_de_socio
    END;

UPDATE Socios
SET faixa_etaria =
	CASE 
        WHEN faixa_etaria = '1' THEN '0 a 12 Anos'
		WHEN faixa_etaria = '2' THEN '13 a 20 Anos'
		WHEN faixa_etaria = '3' THEN '21 a 30 Anos'
		WHEN faixa_etaria = '4' THEN '31 a 40 Anos'
		WHEN faixa_etaria = '5' THEN '41 a 50 Anos'
		WHEN faixa_etaria = '6' THEN '51 a 60 Anos'
		WHEN faixa_etaria = '7' THEN '61 a 70 Anos'
		WHEN faixa_etaria = '8' THEN '71 a 80 Anos'
		WHEN faixa_etaria = '9' THEN 'Mais de 80 Anos'
		WHEN faixa_etaria = '0' THEN 'N�o Aplica '
        ELSE identificador_de_socio
    END;

UPDATE Socios
SET str_qualificacao_socios = (
	SELECT t.qualifica��o_str
    FROM qualifica��o t
    WHERE Socios.c�d_qualificacao_socio = t.c�d_qualifica��o);

UPDATE Socios
SET str_qualificacao_representante = (
	SELECT t.qualifica��o_str
    FROM qualifica��o t
    WHERE Socios.c�d_qualificacao_representante_legal = t.c�d_qualifica��o);

UPDATE Socios
SET str_pais = (
	SELECT t.pais_str
    FROM pais t
    WHERE Socios.c�d_pais = t.c�d_pais);

UPDATE Socios
SET data_entrada_sociedade = CONCAT(
	SUBSTRING(data_entrada_sociedade, 1, 4), '/', 
    SUBSTRING(data_entrada_sociedade, 5, 2), '/', 
    SUBSTRING(data_entrada_sociedade, 7, 2)
);
	
UPDATE Estabelecimentos
SET CNPJ = CONCAT(cnpj_basico, '/',cnpj_ordem, '-', cnpj_dv);
	
UPDATE Estabelecimentos
SET situacao_cadastral =
	CASE 
        WHEN situacao_cadastral = '01' THEN 'Nula'
        WHEN situacao_cadastral = '02' THEN 'Ativa'
        WHEN situacao_cadastral = '03' THEN 'Suspensa'
		WHEN situacao_cadastral = '04' THEN 'Inapta'
		WHEN situacao_cadastral = '08' THEN 'Baixada'
        ELSE situacao_cadastral
    END;

UPDATE Estabelecimentos
SET str_motivo_situacao_cadastral = (
	SELECT t.motivo_str
    FROM motivos t
    WHERE Estabelecimentos.c�d_motivo_situacao_cadastral = t.c�d_motivo);

UPDATE Estabelecimentos
SET str_pais = (
	SELECT t.pais_str
    FROM pais t
    WHERE Estabelecimentos.c�d_pais = t.c�d_pais);

UPDATE Estabelecimentos
SET str_cnae_fiscal = (
	SELECT t.cnae_str
    FROM cnae t
    WHERE Estabelecimentos.c�d_cnae_fiscal = t.c�d_cnae);

UPDATE Estabelecimentos
SET str_municipio = (
	SELECT t.municipios_str
    FROM municipios t
    WHERE Estabelecimentos.c�d_municipio = t.c�d_municipios);

UPDATE Estabelecimentos
SET data_inicio_atividades = CONCAT(
	SUBSTRING(data_inicio_atividades, 1, 4), '/', 
    SUBSTRING(data_inicio_atividades, 5, 2), '/', 
    SUBSTRING(data_inicio_atividades, 7, 2)
);

UPDATE Estabelecimentos
SET data_situacao_cadastral = CONCAT(
	SUBSTRING(data_situacao_cadastral, 1, 4), '/', 
    SUBSTRING(data_situacao_cadastral, 5, 2), '/', 
    SUBSTRING(data_situacao_cadastral, 7, 2)
);

UPDATE Estabelecimentos
SET data_situacao_especial = CONCAT(
	SUBSTRING(data_situacao_especial, 1, 4), '/', 
    SUBSTRING(data_situacao_especial, 5, 2), '/', 
    SUBSTRING(data_situacao_especial, 7, 2)
);