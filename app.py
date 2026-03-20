def generate_sql(query):
    query = query.lower()

    if "all users" in query:
        return "SELECT * FROM users;"
    
    elif "orders" in query:
        return "SELECT * FROM orders;"
    
    elif "users older than" in query:
        age = ''.join(filter(str.isdigit, query))
        return f"SELECT * FROM users WHERE age > {age};"
    
    else:
        return "Query not recognized."

# Test examples
print(generate_sql("Show all users"))
print(generate_sql("Show orders"))
print(generate_sql("Show users older than 25"))
