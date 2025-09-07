-- models/ddl.sql
CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    fiscal_period VARCHAR(10)
);

CREATE TABLE dim_cedente (
    cedente_id VARCHAR PRIMARY KEY,
    nome VARCHAR,
    cnpj_masked VARCHAR,
    segmento VARCHAR,
    risk_score NUMERIC
);

CREATE TABLE dim_produto (
    produto_id VARCHAR PRIMARY KEY,
    tipo_produto VARCHAR,
    prazo INT,
    condicao_pagamento VARCHAR
);

CREATE TABLE fact_recebiveis (
    id BIGSERIAL PRIMARY KEY,
    date_id DATE REFERENCES dim_date(date_id),
    cedente_id VARCHAR REFERENCES dim_cedente(cedente_id),
    produto_id VARCHAR REFERENCES dim_produto(produto_id),
    valor_bruto NUMERIC,
    taxa_pct NUMERIC,
    valor_liquido NUMERIC,
    data_processamento TIMESTAMP,
    quantidade_documentos INT
);