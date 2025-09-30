#Eduardo Torres

My favorite coding language is currently SQL ! 
SQL is fun to use and it feels like a puzzle each time I have to find
a query. 

## Example Code

'''
SELECT count(Gender)
FROM DS219
WHERE mood LIKE 'Happy'
GROUP BY student
'''

### Code Explanation
This code above will returns the count of happy students seperated by gender.
Assume there is an imaginary table based on the people from DS219. SELECT selects the gender column. FROM is the table were looking at which is currently DS219. WHERE selects the attribute, in this case where people have the happy attribute. GROUP BY, groups our return results by people only with the student status. Oh and count() is an aggregate function which returns the total students
