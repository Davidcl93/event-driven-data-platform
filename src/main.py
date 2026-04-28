rows_to_insert = [{
        "user_id": event.get("user_id"),
        "event_type": event.get("event_type"),
        "product_id": event.get("product_id"),
        "price": event.get("price"),
        "timestamp": event.get("timestamp")
    }]

    errors = client.insert_rows_json(TABLE_ID, rows_to_insert)

    if errors:
        print("Error inserting:", errors)
        return ("Error", 500)

    return ("OK", 200)