CREATE TABLE product (
    product_id VARCHAR(25) NULL,
    product_length FLOAT NULL,
    product_depth FLOAT NULL,
    product_width FLOAT NULL,
    cluster_id VARCHAR(25) NULL,
    hierarchy1_id VARCHAR(25) NULL,
    hierarchy2_id VARCHAR(25) NULL,
    hierarchy3_id VARCHAR(25) NULL,
    hierarchy4_id VARCHAR(25) NULL,
    hierarchy5_id VARCHAR(25) NULL,
    CONSTRAINT  product_pk PRIMARY KEY (product_id)
);

CREATE TABLE store_cities (
    store_id VARCHAR(25) NULL,
    storetype_id VARCHAR(25) NULL,
    store_size FLOAT NULL,
    city_id VARCHAR NULL,
    CONSTRAINT  store_cities_pk PRIMARY KEY (store_id)
);

CREATE TABLE sales (
    product_id VARCHAR(25) NULL,
    store_id VARCHAR(25) NULL,
    date DATE NULL,
    sales FLOAT NULL,
    revenue FLOAT NULL,
    stock FLOAT NULL,
    price FLOAT NULL,
    promo_type_1 VARCHAR(25) NULL,
    promo_bin_1 VARCHAR(25) NULL,
    promo_type_2 VARCHAR(25) NULL,
    promo_bin_2 VARCHAR(25) NULL,
    promo_discount_2 VARCHAR(25) NULL,
    promo_discount_type_2 VARCHAR(25) NULL,
    CONSTRAINT fk_store
        FOREIGN KEY (store_id)
        REFERENCES store_cities(store_id)
);
