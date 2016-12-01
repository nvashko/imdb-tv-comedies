#!/usr/bin/env python3

def extract():
	import psycopg2

	conn = psycopg2.connect(
		"dbname=imdb"
		)
	conn.autocommit = True
	cur = conn.cursor()

	#sql_stmt = 'select * from shows'
	#sql_stmt = 
	cur.execute(
		"""insert into shows_test values (%s);""",
		('my_example_insert')
		)
	cur.fetchone()
	return

	#result = cur.fetchall()

	#return result



def main():
	data = extract()
	print(data)

if __name__ == '__main__':
	main()