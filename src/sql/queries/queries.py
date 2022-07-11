
with open('./sql/queries/insert_people_final.sql', 'r') as file:
    INSERT_PEOPLE_FINAL = file.read()

with open('./sql/queries/view_people_by_country.sql', 'r') as file:
    VIEW_PEOPLE_BY_COUNTRY = file.read()