// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({ "name": "Jane Austen", "nationality": "British", "bio": { "short": "English novelist known for novels about the British landed gentry.", "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development." } })

// Task 4: update to add birthday
db.authors.updateOne({"name":"Jane Austen"},{ $set: { "birthday" : "1775-12-16" }})

// Task 5: insert four more authors
db.authors.insertMany([ { "name": "Mark Twain", "nationality": "American", "bio": { "short": "American writer and humorist.", "long": "Mark Twain was an American writer best known for The Adventures of Tom Sawyer and Adventures of Huckleberry Finn." }, "birthday": "1835-11-30" }, { "name": "Charles Dickens", "nationality": "British", "bio": { "short": "Victorian English writer.", "long": "Charles Dickens created some of the world's most well-known fictional characters and wrote novels including Oliver Twist and A Christmas Carol." }, "birthday": "1812-02-07" }, { "name": "Haruki Murakami", "nationality": "Japanese", "bio": { "short": "Japanese contemporary writer.", "long": "Haruki Murakami is known for blending surrealism with everyday life in novels like Norwegian Wood and Kafka on the Shore." }, "birthday": "1949-01-12" }, { "name": "Jane Eyre", "nationality": "British", "bio": { "short": "English novelist.", "long": "Charlotte Brontë wrote under the pen name Currer Bell and authored the famous novel Jane Eyre." }, "birthday": "1816-04-21" }])

// Task 6: total count
db.authors.countDocuments({})

// Task 7: British authors, sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })
