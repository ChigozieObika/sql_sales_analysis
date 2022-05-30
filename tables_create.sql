CREATE TABLE product (
    product_id VARCHAR(25) NULL,
    product_length FLOAT NULL,
    product_depth FLOAT NULL,
    product_width FLOAT NULL,
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
    CONSTRAINT sales_pk PRIMARY KEY (product_id, store_id),
    CONSTRAINT fk_product 
        FOREIGN KEY (product_id)
        REFERENCES product(product_id),
    CONSTRAINT fk_store
        FOREIGN KEY (store_id)
        REFERENCES store_cities(store_id)
)


