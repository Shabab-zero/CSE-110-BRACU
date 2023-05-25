# Task-4

book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)

for catagory, book_name, number_of_votes in book_info:
    print(f"{book_name} won the '{catagory}' catagory with {number_of_votes} votes")