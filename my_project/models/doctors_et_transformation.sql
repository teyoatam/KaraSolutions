-- models/doctors_et_transformation.sql

SELECT
    message_id,
    date,
    LOWER(text) AS text  -- Example transformation
FROM
    {{ ref('doctors_et') }}
WHERE
    message_id IS NOT NULL AND date IS NOT NULL