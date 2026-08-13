def read_books():
    books_dict = {}

    with open('books.txt', 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(', ')
                title = parts[0]
                author = parts[1]
                year = parts[2]
                rating = parts[3]
                books_dict[title] = {
                    'title': title,
                    'author': author,
                    'year': year,
                    'rating': rating
                }

print(f"{'Title':<70}  {'Author':<50}  {'Year':<6}  {'Rating':<6}")

   
read_books()
