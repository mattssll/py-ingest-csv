SELECT
    place.country,
    COUNT(people.id) AS ct
FROM
    places pl
LEFT JOIN
    peoplefinal pf ON pf.place_id = pl.id
GROUP BY
    pl.country
ORDER BY COUNT(pf.id) DESC;