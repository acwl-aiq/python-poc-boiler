CREATE TABLE test (
    unique_id VARCHAR(36) PRIMARY KEY,
    some_value VARCHAR(36) NOT NULL,
    update_time TIMESTAMPTZ NOT NULL
);