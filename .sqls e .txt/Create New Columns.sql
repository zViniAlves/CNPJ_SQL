USE CNPJ

ALTER TABLE Estabelecimentos ADD CNPJ VARCHAR(255);
ALTER TABLE Estabelecimentos ADD str_motivo_situacao_cadastral VARCHAR(255);
ALTER TABLE Estabelecimentos ADD str_pais VARCHAR(255);
ALTER TABLE Estabelecimentos ADD str_cnae_fiscal VARCHAR(255);
ALTER TABLE Estabelecimentos ADD str_municipio VARCHAR(255);

ALTER TABLE Empresas ADD str_natureza_juridica VARCHAR(255);
ALTER TABLE Empresas ADD str_qualificação_responsavel VARCHAR(255);

ALTER TABLE Socios ADD str_qualificacao_socios VARCHAR(255);
ALTER TABLE Socios ADD str_qualificacao_representante VARCHAR(255);
ALTER TABLE Socios ADD str_pais VARCHAR(255);