#!/usr/bin/env python3
"""
Module: my_module

This module provides stats about Nginx logs stored in MongoDB.
"""

import pymongo


def nginx_logs_stats(mongo_db, collection_name):
    """
    Display stats about Nginx logs stored in MongoDB.

    :param mongo_db: pymongo database object
    :type mongo_db: pymongo.database.Database
    :param collection_name: Name of the MongoDB collection storing Nginx logs
    :type collection_name: str
    """
    # Get the specified collection
    collection = mongo_db[collection_name]

    # Total number of logs
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs where {total_logs}"
          "is the number of documents in this collection")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{count} documents with method={method}")

    # Number of documents with method=GET and path=/status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"\t{status_count} documents with method=GET and path=/status")
