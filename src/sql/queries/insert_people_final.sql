INSERT INTO peoplefinal
(given_name, family_name, date_of_birth, place_id)
SELECT
    given_name,
    family_name,
    date_of_birth,
    pl.id
FROM
    peopleraw pr
INNER JOIN
    places pl ON pl.city = pr.place_of_birth
;