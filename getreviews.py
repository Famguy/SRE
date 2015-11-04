import goodreads.client as client

gc = client.GoodreadsClient("6KLeSpdJh07FdIx48QkyNg", "7FrusdYkPsRmkXG9oPLyk3fGTC8Zy7yBJjOTwy9iwZY")
book = gc.book(105576)
print book






