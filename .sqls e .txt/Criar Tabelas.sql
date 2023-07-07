USE CNPJ;

CREATE TABLE Empresas(
    cnpj_basico VARCHAR(10),
    razao_social VARCHAR(255),
    cód_natureza_juridica VARCHAR(255),
    cód_qualificacao_responsavel VARCHAR(255),
    capital_social_str VARCHAR(255),
    porte_empresa VARCHAR(255),
    ente_federativo_responsavel VARCHAR(255));

CREATE TABLE Estabelecimentos(
    cnpj_basico VARCHAR(10),
    cnpj_ordem VARCHAR(7),
    cnpj_dv VARCHAR(4),
    matriz_filial VARCHAR(4),
    nome_fantasia VARCHAR(255),
    situacao_cadastral VARCHAR(255),
    data_situacao_cadastral VARCHAR(255),
    cód_motivo_situacao_cadastral VARCHAR(255),
    nome_cidade_exterior VARCHAR(255),
    cód_pais VARCHAR(255),
    data_inicio_atividades VARCHAR(255),
    cód_cnae_fiscal VARCHAR(255),
    cnae_fiscal_secundaria VARCHAR(MAX),
    tipo_logradouro VARCHAR(255),
    logradouro VARCHAR(MAX),
    numero VARCHAR(255),
    complemento VARCHAR(MAX),
    bairro VARCHAR(255),
    cep VARCHAR(255),
    uf VARCHAR(255),
    cód_municipio VARCHAR(255),
    ddd1 VARCHAR(255),
    telefone1 VARCHAR(255),
    ddd2 VARCHAR(255),
    telefone2 VARCHAR(255),
    ddd_fax VARCHAR(255),
    fax VARCHAR(255),
    correio_eletronico VARCHAR(MAX),
    situacao_especial VARCHAR(255),
    data_situacao_especial VARCHAR(255));

CREATE TABLE Socios(
    cnpj_basico VARCHAR(10),
    identificador_de_socio VARCHAR(255),
    nome_socio VARCHAR(255),
    cnpj_cpf_socio VARCHAR(255),
    cód_qualificacao_socio VARCHAR(255),
    data_entrada_sociedade VARCHAR(255),
    cód_pais VARCHAR(255),
    representante_legal VARCHAR(255),
    nome_representante VARCHAR(255),
    cód_qualificacao_representante_legal VARCHAR(255),
    faixa_etaria VARCHAR(255));

CREATE TABLE Simples(
    cnpj_basico VARCHAR(10),
    opcao_simples VARCHAR(255),
    data_opcao_simples VARCHAR(255),
    data_exclusao_simples VARCHAR(255),
    opcao_mei VARCHAR(255),
    data_opcao_mei VARCHAR(255),
    data_exclusao_mei VARCHAR(255));

CREATE TABLE cnae(
	cód_cnae VARCHAR(255),
	cnae_str VARCHAR(255))

CREATE TABLE motivos(
	cód_motivo VARCHAR(255),
	motivo_str VARCHAR(255))

CREATE TABLE municipios(
	cód_municipios VARCHAR(255),
	municipios_str VARCHAR(255))

CREATE TABLE natureza(
	cód_natureza VARCHAR(255),
	natureza_str VARCHAR(255))

CREATE TABLE pais(
	cód_pais VARCHAR(255),
	pais_str VARCHAR(255))

CREATE TABLE qualificação(
	cód_qualificação VARCHAR(255),
	qualificação_str VARCHAR(255))